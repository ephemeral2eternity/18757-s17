from dash.fault_tolerance import *
from dash.utils import *
from qoe.dash_chunk_qoe import *
from utils.client_utils import *
from multiprocessing import freeze_support
from multiprocessing import Process
from threading import Timer

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

def print_time():
    print "From print_time", time.strftime("%m%d%H%M")

srv_addr = 'az.cmu-agens.com'
def print_some_times():
    print time.strftime("%m%d%H%M")
    #for i in range(0, 19):
    Timer(1, fork_cache_client_info1, (srv_addr,)).start()
    #for i in range(0, 19):
    Timer(2, fork_ping_client, (srv_addr, 3)).start()
    #time.sleep(11)  # sleep while time-delay events execute
    #print time.time()

if __name__ == '__main__':
	t0 = time.time()
	print t0;
	#print_some_times()
	time.sleep(10);
	t1 = time.time()
	print t1;
	diff = t1 - t0
	print diff
