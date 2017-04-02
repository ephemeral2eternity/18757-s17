import urllib, json
from collections import defaultdict

from subprocess import call

# # Note that you have to specify path to script
# call(["node", "testscript.js"]);
#
# #json_data = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/trace-route-analysis_02060550_cache.json").read();
# json_data = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/trace-route-analysis_02130550_cache.json").read();
# parsed_json=json.loads(json_data);
#
# #Analyzing routes in cached version
# routesJson = [];
# for node in parsed_json:
#     r = {};
#     r['ip'] = node['name'];
#     r['name'] = node['id'];
#     r['timeTaken'] = node['timeTaken'];
#     r['hops'] = node['hops'];
#     r['routes'] = [];
#     for route in node['routes']:
#         o = {};
#         ip = route['id'];
#         o['ip'] = ip;
#         o['time'] = route['time'];
#         if(ip != '*'):
#             url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
#             response = urllib.urlopen(url);
#             data = json.loads(response.read());
#             o['AS']= data['AS'];
#             o['ISP'] = data['ISP'];
#         r['routes'].append(o);
#     routesJson.append(r);
#
#
# #write json into a file
# #with open('generated/routesData_02060550_cache.json', 'w') as outfile:
# with open('generated/routesData_02130550_cache.json', 'w') as outfile:
#     json.dump(routesJson, outfile);
#     print("Writing File Job Done!")

# #importing routes data and working on it
# json_data_S = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/routesData_02060550_cache.json").read();
# json_data_NS = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/routesData_02130550_cache.json").read();
# parsed_json_S=json.loads(json_data_S);
# parsed_json_NS=json.loads(json_data_NS);
#
# #Analyzing latency between links and comparing between expected busy vs non-busy days
#
# #comparing overall time taken for traceRoute between clients & servers
# for route_S in parsed_json_S:
#     for route_NS in parsed_json_NS:
#         if(route_S['ip'] == route_NS['ip']):
#             if(route_S['timeTaken'] != route_NS['timeTaken']):
#                 print(route_S['timeTaken']);
#                 print(route_NS['timeTaken']);
#
# #comparing each link latency
# for (route_S, route_NS) in zip(parsed_json_S, parsed_json_NS):
#     for (r_S, r_NS) in zip(route_S['routes'], route_NS['routes']):
#         if(r_S['ip'] == r_NS['ip']):
#             if(r_S['time'] != r_NS['time']):
#                 print r_S['ip'];
#
#
# transit = [];
# #processing number of transit networks in the route
# for route_S in parsed_json_S:
#     d = defaultdict(list);
#     o = {};
#     o['ip'] = route_S['ip'];
#     o['name'] = route_S['name'];
#     o['timeTaken'] = route_S['timeTaken'];
#     o['hops'] = route_S['hops'];
#     for r_S in route_S['routes']:
#         if 'AS' in r_S:
#             if r_S['AS']:
#                 key = r_S['AS'];
#                 d[key].append(r_S);
#         o['routes'] = d;
#     transit.append(o);
#
# with open('generated/grouped_02060550.json', 'w') as outfile:
#      json.dump(transit, outfile);
#      print("Writing File Job Done!");
#
# transit = [];
# for route_NS in parsed_json_NS:
#     d = defaultdict(list);
#     o = {};
#     o['ip'] = route_NS['ip'];
#     o['name'] = route_NS['name'];
#     o['timeTaken'] = route_NS['timeTaken'];
#     o['hops'] = route_NS['hops'];
#     for r_NS in route_NS['routes']:
#         if 'AS' in r_NS:
#             if r_NS['AS']:
#                 key = r_NS['AS'];
#                 d[key].append(r_NS);
#         o['routes'] = d;
#     transit.append(o);
#
# with open('generated/grouped_02130550.json', 'w') as outfile:
#      json.dump(transit, outfile);
#      print("Writing File Job Done!");

#calculating number of transit networks per route
json_data_transit_S = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/grouped_02060550.json").read();
json_data_transit_NS = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/grouped_02130550.json").read();
parsed_json_transit_S=json.loads(json_data_transit_S);
parsed_json_transit_NS=json.loads(json_data_transit_NS);

for r in parsed_json_transit_S:
    count = 0;
    print r['name'];
    for a in r['routes']:
        count=count + 1;
    print count;


for r in parsed_json_transit_NS:
    count = 0;
    print r['name'];
    for a in r['routes']:
        count=count + 1;
    print count;