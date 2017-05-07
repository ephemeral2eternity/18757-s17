## this program does analysis of the trace route data
## based on latency and the path the client has taken
## to get to the server to determine the location of
## the cache server

import os, json
import urllib
from ipinfo.ipinfo import *

# dir = './results/routeData/';
# for filename in os.listdir(dir):
#     print filename
#     path = dir + filename;
#
#     json_data = open(path).read();
#     parsed_json = json.loads(json_data);
#     print parsed_json;
#
#     clientName = parsed_json['name'];
#
#     indices = [];
#     for elem in parsed_json['route']:
#         indices.append(int(elem));
#
#     indices.sort(reverse=False);
#     print indices
#
#     for i in range(indices.__len__()):
#         print "time taken by the hop:", parsed_json['route'][str(indices[i])]['time'];
#         ip = parsed_json['route'][str(indices[i])]['ip'];
#         url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
#         response = urllib.urlopen(url);
#         data = json.loads(response.read());
#         print "latitude: ", data['latitude']
#         print "longitude: ", data['longitude']
#
#     ###### TODO: After this need to form a matrix of N * N known hosts, their locations, their latencies
#     ###### to communicate with each other. Use the matrix as a reference for known locations and approximate
#     ###### where the servers are.

dir = './results/dataQoE/';
clientData = [];
for filename in os.listdir(dir):
    clientDetail = {};
    #print filename
    clientName = filename.split('_')[0];
    #print clientName;
    ip = host2ip(clientName);
    url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
    response = urllib.urlopen(url);
    data = json.loads(response.read());

    #recording location
    clientDetail['name'] = ip;
    clientDetail['lon'] = data['longitude'];
    clientDetail['lat'] = data['latitude'];
    clientDetail['netsize'] = 1;
    clientDetail['netID'] = 0;
    clientDetail['type'] = "client";
    clientDetail['asn'] = data['AS'];
    clientDetail['QoE'] = 0;

    #print clientDetail;

    path = dir + filename;
    json_data = open(path).read();
    parsed_json = json.loads(json_data);
    for elem in parsed_json:
       clientDetail['QoE']+= parsed_json[elem]['QoE2'];

    clientDetail['QoE'] = clientDetail['QoE']/120;
    clientData.append(clientDetail);

dest = './results/furtherAnalysis/' + "clients.json";
with open(dest, 'w') as outfile:
    json.dump(clientData, outfile);
    print("Writing File Job Done! " + dest);

