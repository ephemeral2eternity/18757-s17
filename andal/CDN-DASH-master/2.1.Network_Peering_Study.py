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
ROUTE_DATA_FILES_PATH = './results/routeData/'
DATA_QOE_FILES_PATH = './results/dataQoE/'

peering_json = json.loads(open(PEERINGS_MAP_PATH).read());


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
        url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
        response = urllib.urlopen(url);
        data = json.loads(response.read());
        as_for_hops[key] = {
            'ip': ip,
            'AS': data['AS']
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

    return route_data_files

def get_dataQoE_files_by_timestamp(timestamps):
    dataQoE_files = [];
    for filename in os.listdir(DATA_QOE_FILES_PATH):
        path = DATA_QOE_FILES_PATH + filename;
        #sample: planetlab1.temple.edu_05050243_aws.cmu-agens.com.json
        if(filename.split('_')[1] in timestamps):
            dataQoE_files.append(path);

    return dataQoE_files;

meanQoE = [];
meanQoEValuesSpread = [];

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

                route_data_files = get_route_data_files(current_peer, peer)
                #route_data_files = get_route_data_files(16509, 27)
                #print route_data_files

                #find timestamp in route data files
                timestamps = [];
                for filename in route_data_files:
                    timestamps.append(filename[ filename.rfind('_') + 1 : filename.rfind('.')] );

                #find dataQoE files with the same timestamp
                dataQoE_files = get_dataQoE_files_by_timestamp(timestamps);
                #print dataQoE_files;

                #parse through each of these dataQoE files and find the mean QoE
                for filename in dataQoE_files:
                    QoE_data = json.loads(open(filename).read());

                    meanQoE_peering = 0;
                    for qoe in QoE_data:
                        meanQoE_peering += QoE_data[qoe]['QoE2'];
                    meanQoE_peering = meanQoE_peering/120;
                    pair['meanQoE'] = meanQoE_peering;
                    meanQoE.append(pair);
                    meanQoEValuesSpread.append(meanQoE_peering);
                    #print meanQoE_peering;

                print meanQoE;
                print meanQoEValuesSpread;

init()

