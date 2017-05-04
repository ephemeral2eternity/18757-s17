## this program does analysis of the trace route data
## based on latency and the path the client has taken
## to get to the server to determine the location of
## the cache server

import os, json
import urllib

dir = './results/routeData/';
for filename in os.listdir(dir):
    print filename
    path = dir + filename;

    json_data = open(path).read();
    parsed_json = json.loads(json_data);
    print parsed_json;

    clientName = parsed_json['name'];

    indices = [];
    for elem in parsed_json['route']:
        indices.append(int(elem));

    indices.sort(reverse=False);
    print indices

    for i in range(indices.__len__()):
        print parsed_json['route'][str(indices[i])]['time'];
        ip = parsed_json['route'][str(indices[i])]['ip'];
        url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
        response = urllib.urlopen(url);
        data = json.loads(response.read());

