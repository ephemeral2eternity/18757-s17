## this program does analysis of the trace route and the QoE data from the
## video streaming results and report parameters like location of the video
## server, AS number and QoE experience
import urllib, json, os
from collections import defaultdict

#####Processing QoE Data
rootJson = {};
servers = [];
uniqIPs = [];
count = 0;
dir = './dataQoE/';
for filename in os.listdir(dir):
    path = dir + filename;

    json_data = open(path).read();
    parsed_json = json.loads(json_data);

    for elem in parsed_json:
        ip = parsed_json[elem]['Server'];
        node = {};
        if (ip != '*'):
            url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
            response = urllib.urlopen(url);
            data = json.loads(response.read());

            if(ip not in uniqIPs):
                uniqIPs.append(ip);
                node['lat'] = data['latitude'];
                node['lon'] = data['longitude'];
                node['netID'] = count;
                node['type'] = "server";
                node['netsize'] = 1;
                node['asn'] = "AS " + str(data['AS']);
                node['name'] = data['ip'];
                node['QoE'] = parsed_json[elem]['QoE2'];
                node['ChunksToServerNumber'] = 1;
                servers.append(node);
            else:
                for server in servers:
                    if(server['name'] == ip):
                        server['QoE'] = (server['QoE'] + parsed_json[elem]['QoE2']);
                        server['ChunksToServerNumber'] = server['ChunksToServerNumber'] + 1;

for server in servers:
    if(server['ChunksToServerNumber'] > 0):
        server['QoE'] = server['QoE']/server['ChunksToServerNumber'];

print servers;
rootJson['server'] = servers;
dest = './results/furtherAnalysis/' + "cloudProviders.json";
with open(dest, 'w') as outfile:
    json.dump(rootJson, outfile);
    print("Writing File Job Done! " + dest);


####Processing Route Data
#dir = './results/routeData/';
# for filename in os.listdir(dir):
#     #print filename;
#     path = dir + filename;
#
#     json_data = open(path).read();
#     parsed_json = json.loads(json_data);
#
#     clientName = parsed_json['name'];
#
#     indices = [];
#     for elem in parsed_json['route']:
#         indices.append(int(elem));
#
#     indices.sort(reverse=True);
#     #print indices[0];
#
#     ip = parsed_json['route'][str(indices[0])]['ip'];
#
#     node = {};
#     if (ip != '*'):
#         url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
#         response = urllib.urlopen(url);
#         data = json.loads(response.read());
#
#         node['lat'] = data['latitude'];
#         node['lon'] = data['longitude'];
#         node['netID'] = count;
#         node['type'] = "server";
#         node['netsize'] = 1;
#         node['asn'] = "AS " + str(data['AS']);
#         node['name'] = data['ip'];
#         servers.append(node);
#
#         count = count + 1;
#
# rootJson['server'] = servers;
# dest = './results/furtherAnalysis/' + "cloudProviders.json";
# with open(dest, 'w') as outfile:
#     json.dump(rootJson, outfile);
#     print("Writing File Job Done! " + dest);
