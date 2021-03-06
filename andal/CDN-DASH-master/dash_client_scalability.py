from dash.fault_tolerance import *
from dash.utils import *
from qoe.dash_chunk_qoe import *
from utils.client_utils import *
from multiprocessing import freeze_support
from multiprocessing import Process
from threading import Timer

## ==================================================================================================
# define the simple client agent that only downloads videos from denoted server
# @input : srv_addr ---- the server name address
#		   video_name --- the string name of the requested video
## ==================================================================================================
def dash_client(srv_addr, video_name, method=None):
	procs = [];
	## Define all parameters used in this client
	#TODO - what is alpha used for?
	alpha = 0.5
	#chunk retry number in case of failure, before giving up
	retry_num = 10

	## CDN SQS
	#TODO - where is this CDN SQS (queuing I guess), component used in the code?
	CDN_SQS = 5.0
	uniq_srvs = []

	## ==================================================================================================
	## Client name and info
	client = getMyName()
	cur_ts = time.strftime("%m%d%H%M")
	if method is not None:
		client_ID = client + "_" + cur_ts + "_" + method
	else:
		client_ID = client + "_" + cur_ts + "_" + srv_addr

	## ==================================================================================================
	## Parse the mpd file for the streaming video
	## ==================================================================================================
	rsts, srv_ip = ft_mpd_parser(srv_addr, retry_num, video_name)
	if not rsts:
		return

	### ===========================================================================================================
	## Read parameters from dash.mpd_parser
	### ===========================================================================================================
	vidLength = int(rsts['mediaDuration'])
	minBuffer = num(rsts['minBufferTime'])
	reps = rsts['representations']

	# Get video bitrates in each representations
	vidBWs = {}
	for rep in reps:
		if not 'audio' in rep:
			vidBWs[rep] = int(reps[rep]['bw'])
	print vidBWs

	sortedVids = sorted(vidBWs.items(), key=itemgetter(1))

	# Start streaming from the minimum bitrate
	minID = sortedVids[0][0]
	vidInit = reps[minID]['initialization']
	maxBW = sortedVids[-1][1]

	# Read common parameters for all chunks
	timescale = int(reps[minID]['timescale'])
	chunkLen = int(reps[minID]['length']) / timescale
	chunkNext = int(reps[minID]['start'])

	## ==================================================================================================
	# Start downloading the initial video chunk
	## ==================================================================================================
	curBuffer = 0
	chunk_download = 0

	## Traces to write out
	client_tr = {}
	http_errors = {}

	## Download initial chunk
	loadTS = time.time()
	print "[" + client_ID + "] Start downloading video " + video_name + " at " + \
		  datetime.datetime.fromtimestamp(int(loadTS)).strftime("%Y-%m-%d %H:%M:%S") + \
		  " from server : " + srv_addr

	(vchunk_sz, chunk_srv_ip, error_codes) = ft_download_chunk(srv_addr, retry_num, video_name, vidInit)
	http_errors.update(error_codes)
	if vchunk_sz == 0:
		## Write out traces after finishing the streaming
		writeTrace(client_ID + "_cdn", client_tr)
		writeHTTPError(client_ID, http_errors)
		return

	startTS = time.time()

	tr_proc = fork_cache_client_info1(srv_addr);
	procs.append(tr_proc);

	ping_proc = fork_ping_client(srv_addr, 3);
	procs.append(ping_proc);

	print "[" + client_ID + "] Start playing video at " + datetime.datetime.fromtimestamp(int(startTS)).strftime("%Y-%m-%d %H:%M:%S")
	est_bw = vchunk_sz * 8 / (startTS - loadTS)
	print "|-- TS --|-- Chunk # --|- Representation -|-- Linear QoE --|-- Cascading QoE --|-- Buffer --|-- Freezing --|-- Selected Server --|-- Chunk Response Time --|"
	preTS = startTS
	chunk_download += 1
	curBuffer += chunkLen

	## trace route and ping timer
	tr_time = time.time()
	ping_time = time.time()
	## ==================================================================================================
	# Start streaming the video
	## ==================================================================================================
	while (chunkNext * chunkLen < vidLength):

		measure_cur_time = time.time();
		diff_tr_time = int(measure_cur_time - tr_time);
		diff_ping_time = int(measure_cur_time - ping_time);

		nextRep = findRep(sortedVids, est_bw, curBuffer, minBuffer)
		vidChunk = reps[nextRep]['name'].replace('$Number$', str(chunkNext))
		loadTS = time.time()
		(vchunk_sz, chunk_srv_ip, error_codes) = ft_download_chunk(srv_addr, retry_num, video_name, vidChunk)
		http_errors.update(error_codes)
		if vchunk_sz == 0:
			## Write out traces after finishing the streaming
			writeTrace(client_ID, client_tr)
			writeHTTPError(client_ID, http_errors)
			return

		curTS = time.time()
		rsp_time = curTS - loadTS
		est_bw = vchunk_sz * 8 / rsp_time
		time_elapsed = curTS - preTS

		# Compute freezing time
		if time_elapsed > curBuffer:
			freezingTime = time_elapsed - curBuffer
			curBuffer = 0
		# print "[AGENP] Client freezes for " + str(freezingTime)
		else:
			freezingTime = 0
			curBuffer = curBuffer - time_elapsed

		# Compute QoE of a chunk here
		curBW = num(reps[nextRep]['bw'])
		chunk_linear_QoE = computeLinQoE(freezingTime, curBW, maxBW)
		chunk_cascading_QoE = computeCasQoE(freezingTime, curBW, maxBW)

		CDN_SQS = (1 - alpha) * CDN_SQS + alpha * chunk_cascading_QoE
		print CDN_SQS

		# print "Chunk Size: ", vchunk_sz, "estimated throughput: ", est_bw, " current bitrate: ", curBW

		print "|---", str(curTS), "---|---", str(chunkNext), "---|---", nextRep, "---|---", str(chunk_linear_QoE), "---|---", \
			str(chunk_cascading_QoE), "---|---", str(curBuffer), "---|---", str(curBW), "---|---", str(freezingTime), "---|---", chunk_srv_ip, "---|---", str(rsp_time), "---|"

		client_tr[chunkNext] = dict(TS=curTS, Representation=nextRep, curBitRate = curBW,  QoE1=chunk_linear_QoE, QoE2=chunk_cascading_QoE, Buffer=curBuffer, \
									Freezing=freezingTime, Server=chunk_srv_ip, Response=rsp_time)

		if chunk_srv_ip not in uniq_srvs:
			uniq_srvs.append(chunk_srv_ip)

		# Update iteration information
		curBuffer = curBuffer + chunkLen
		if curBuffer > 30:
			time.sleep(curBuffer - 30)

		preTS = curTS
		chunk_download += 1
		chunkNext += 1

	## Write out traces after finishing the streaming
	writeTrace(client_ID, client_tr)
	writeTrace(client_ID + "_httperr", http_errors)
	for p in procs:
		p.join(timeout=100)
	return client_ID, CDN_SQS, uniq_srvs


def cache_client_info1(srv_addr):
	client_info = {};
	client_info['name'] = getMyName();
	client_info['timeStamp'] = time.time();
	route = get_route(srv_addr)
	client_info['route'] = route

	outJsonFileName = os.getcwd() + "/routeData/" + client_info['name'] + "-" + srv_addr + "_"  + time.strftime("%m%d%H%M") + ".json"
	with open(outJsonFileName, 'wb') as f:
		json.dump(client_info, f)

def ping_client_info1(ip, count):
	client_info = {};
	client_info['name'] = getMyName();
	client_info['timeStamp'] = time.time();
	rttList, srv_ip = ping(ip,count);
	client_info['rttList'] = rttList;
	client_info['serverIp'] = srv_ip;
	client_info['serverName'] = ip;

	outJsonFileName = os.getcwd() + "/pingData/" + client_info['name'] + "-" + srv_addr + "_" + time.strftime(
		"%m%d%H%M") + ".json"
	with open(outJsonFileName, 'wb') as f:
		json.dump(client_info, f)

def fork_cache_client_info1(srv_addr):
    p = Process(target=cache_client_info1, args=(srv_addr,))
    p.start()
    return p

def fork_ping_client(ip, count):
	p = Process(target=ping_client_info1, args=(ip, count))
	p.start();
	return p


if __name__ == '__main__':
	current_sys_time = time.time();

	if sys.platform == 'win32':
		freeze_support()

	if len(sys.argv) > 1:
		num_runs = int(sys.argv[1])
	else:
		num_runs = client_config.num_runs

	if len(sys.argv) > 1:
		srv_addr = sys.argv[2]
	else:
		srv_addr = client_config.cdn_host

	method = None;
	video_name = "/videos/BBB";

	dash_client(srv_addr, video_name, method);
