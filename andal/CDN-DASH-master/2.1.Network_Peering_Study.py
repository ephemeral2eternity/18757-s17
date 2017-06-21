# TO FIND:
# Determine Mean of session QoE for sessions going
# through a certain <ISP, Cloud> peering.
# (Only consider the direct peers of Cloud providers)

# SOLUTION APPROACH:
# 1. For every peering of type (e.g [ {16509, 3582}, {16509, 1299} .. ], Go through each Route Data
#    file for a given Cloud Provider (results/routeData/azure_routeData.json) and identify all files
#    that contain a given peering
#       1. a. From the filenames of the route data files, identify the timestamp
#            ( xyz.aws.cmu-agens.com_05050327.json => 05050327)
#       1. b. Go through the dataQoE folder, and find sessions with the same timestamp
#            (xyz_05050243_aws.cmu-agens.com.json => 05050243)
#       1. c. Determine mean of session QoE for all the sessions that is using this peering
#             and represent in a graph format

import urllib, json, os

PEERINGS_MAP_PATH = './results/peerings/cloud_direct_peers.json'
ROUTE_DATA_FILES_PATH = './results/routeData/sample_route_data/'
DATA_QOE_FILES_PATH = './results/dataQoE/'
GET_NODE_URL_PATH = 'http://manage.cmu-agens.com/nodeinfo/get_node'
peering_json = json.loads(open(PEERINGS_MAP_PATH).read());
FILE_CACHE = {}
meanQoE = [];
meanQoEValuesSpread = [];

def get_as_for_hops(routeDataFile):
    # 1. make the manage.cmu-agens call to get AS information for each hop
    #   in the route date file
    route_data_json = json.loads(open(routeDataFile).read());

    # get the keys of route_data_json.route and sort them
    keys = dict.keys(route_data_json['route']);

    as_for_hops = {};
    for key in keys:
        ip = route_data_json['route'][key]['ip']
        if ip == '*':
            continue
        url =  GET_NODE_URL_PATH + '?ip=' + ip;
        if url not in FILE_CACHE:
            response = urllib.urlopen(url);
            data = json.loads(response.read());
            FILE_CACHE[url] = data

        #print len(dict.keys(FILE_CACHE));

        as_for_hops[key] = {
            'ip': ip,
            'AS': FILE_CACHE[url]['AS']
        };

    return as_for_hops
    # {
    #     "0": {
    #         "ip": "128.8.126.111",
    #         "AS": 2341
    #     },
    #     "1": {
    #         "ip": "128.8.126.111",
    #         "AS": 23423
    #     }
    # };


def sort_ids(items):
    items = list(map(lambda x: int(x), items));
    items.sort();
    return list(map(lambda x: str(x), items));

def get_route_data_files(as1, as2):
    route_data_files = [];
    # 1. find combinations for as1 + as2 in route data files
    for filename in os.listdir(ROUTE_DATA_FILES_PATH):
        as_for_hops = get_as_for_hops(ROUTE_DATA_FILES_PATH + filename);
        hop_ids = sort_ids(dict.keys(as_for_hops));

        as_for_hops_sorted = []
        for hop_id in hop_ids:
            as_for_hops_sorted.append(as_for_hops[hop_id]);

        for i in range(len(as_for_hops_sorted) - 1):
            cmpAS1 = as_for_hops_sorted[i]['AS']
            cmpAS2 = as_for_hops_sorted[i + 1]['AS']
            if cmpAS1 == cmpAS2:
                continue
            # check if pair (as1, as2) occurs in this route file
            if ((cmpAS1 == as1 and cmpAS2 == as2) or (cmpAS1 == as2 and cmpAS2 == as1)):
                # record the route file name for this peering pair
                route_data_files.append(filename);

    #print 'File Cache: ', FILE_CACHE
    #FILE_CACHE = {}
    return route_data_files

def get_dataQoE_files_by_timestamp(ts_client_map):
    dataQoE_files = [];
    file_list = os.listdir(DATA_QOE_FILES_PATH);
    file_list_maps = []

    def get_time_stamp(filename):
        time_stamp = filename[filename.find('_') + 1: filename.rfind('_')]
        return time_stamp

    for i in range(len(file_list)):
        obj = {
            'file_name': file_list[i],
            'time_stamp': get_time_stamp(file_list[i]),
            'prev_time_stamp': get_time_stamp(file_list[i]),
            'next_time_stamp': get_time_stamp(file_list[i])
        }
        if(i > 0):
            # find the previous timestamp
            obj['prev_time_stamp'] = get_time_stamp(file_list[i-1])

        if (i < len(file_list) - 1):
            # find the previous timestamp
            obj['next_time_stamp'] = get_time_stamp(file_list[i+1])

        file_list_maps.append(obj)

    for filename in os.listdir(DATA_QOE_FILES_PATH):
        path = DATA_QOE_FILES_PATH + filename;

        # TODO: 2. compare the extracted client name with clients in ts_client_map
        #          and compare the timestamps range and add the file to dataQoE_files
        #          only if it is within the range

        # extract client name & time stamp from the file name
        # sample file name : planetlab1.temple.edu_05050243_aws.cmu-agens.com.json
        client_name = filename[0: filename.find('_')]
        time_stamp = filename[filename.find('_') + 1 : filename.rfind('_')]

        matches = list(filter(lambda x: x['client_name'] == client_name, ts_client_map))
        if(len(matches) == 0):
            continue

        for file in file_list_maps:
            if(file['file_name'] == filename):
                prev_time_stamp = file['prev_time_stamp'];
                next_time_stamp = file['next_time_stamp'];

        if (matches[0]['time_stamp'] >= prev_time_stamp and matches[0]['time_stamp'] <= next_time_stamp):
            dataQoE_files.append(path);

    return dataQoE_files;

def init():
    for elem in peering_json:
        #print elem['ispName']
        #print '---------------'
        for current_peer in elem['cloud_peer_map']:
            if current_peer == "-1":
                continue;
            #print 'Current Peer: ' + current_peer;
            for peerObj in elem['cloud_peer_map'][current_peer]['peers']:
                peer = str(peerObj['AS']);
                if peer == "-1":
                    continue;
                #print 'Finding the relative files for the combination ' + current_peer + ' - ' + peer
                pair = {};
                pair['AS'] = [current_peer, peer];

                #route_data_files = get_route_data_files(current_peer, peer)
                route_data_files = get_route_data_files(16509, 27)
                #print route_data_files

                # find timestamp in route data files
                ts_client_names = [];
                for filename in route_data_files:
                    # salt.planetlab.cs.umd.edu-aws.cmu-agens.com_05050342.json
                    timestamp_obj = {
                        'time_stamp' : filename[ filename.rfind('_') + 1 : filename.rfind('.')],
                        'client_name': filename[0: filename.find('-')]
                    }
                    ts_client_names.append(timestamp_obj);


                #find dataQoE files with the same timestamp
                dataQoE_files = get_dataQoE_files_by_timestamp(ts_client_names);
                #print dataQoE_files;

                #parse through each of these dataQoE files and find the mean QoE
                for filename in dataQoE_files:
                    QoE_data = json.loads(open(filename).read());

                    meanQoE_peering = 0;
                    for qoe in QoE_data:
                        meanQoE_peering += QoE_data[qoe]['QoE2'];
                    meanQoE_peering = meanQoE_peering/120;
                    pair['meanQoE'] = meanQoE_peering;
                    if pair not in meanQoE:
                        meanQoE.append(pair);
                    meanQoEValuesSpread.append(meanQoE_peering);
                    #print meanQoE_peering;

    print 'meanQoE', meanQoE;
    print 'meanQoEValuesSpread', meanQoEValuesSpread;

    dest = './results/peerings/' + "meanQoEperPeering.json";
    with open(dest, 'w') as outfile:
        json.dump(meanQoE, outfile);
        print("Writing File Job Done! " + dest);

    dest = './results/peerings/' + "meanQoESpread.json";
    with open(dest, 'w') as outfile:
        json.dump(meanQoEValuesSpread, outfile);
        print("Writing File Job Done! " + dest);


init()

