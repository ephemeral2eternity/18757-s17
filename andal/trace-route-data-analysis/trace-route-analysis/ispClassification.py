# classifying ISP's based on if they are transit, cloud or client
import urllib, json, os
from collections import defaultdict

transit_isps = [];
client_isps = [];
cloud_isps = [];
#importing routes data and working on it
dir = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/RouteDataLocationExtraction/';
for filename in os.listdir(dir):
    #print filename;
    extract_suffix = filename.split("routesData", 1)[1];
    #print extract_suffix;
    path = dir + filename;
    json_data_S = open(path).read();
    parsed_json_S=json.loads(json_data_S);

    #processing number of transit networks in the route
    for route_S in parsed_json_S:
        iter = 0;
        number_of_routes = len(route_S['routes']);
        data_avl_route = 0;
        for r in route_S['routes']:
            if(r['ip'] != '*'):
                data_avl_route = data_avl_route + 1;
        for r in route_S['routes']:
            if(r['ip'] != '*'):
                if(iter == 0):
                    if (r['AS'] not in client_isps):
                        client_isps.append(r['AS']);
                if(iter != 0 and iter < data_avl_route - 1):
                    if ((r['AS'] not in client_isps) and (r['AS'] not in transit_isps)):
                        transit_isps.append(r['AS']);
                if(iter == (data_avl_route - 1)):
                    if (r['AS'] not in cloud_isps):
                        cloud_isps.append(r['AS']);
                    for l in reversed(transit_isps):
                        if(r['AS'] == l):
                            transit_isps.remove(l);
                        else:
                            break;
                iter = iter + 1;

# print client_isps;
# print transit_isps;
# print cloud_isps;

dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/clientISPs.json';
with open(dest, 'w') as outfile:
    json.dump(client_isps, outfile);
    print("Writing File Job Done!");

dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/cloudISPs.json';
with open(dest, 'w') as outfile:
    json.dump(cloud_isps, outfile);
    print("Writing File Job Done!");

dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/transitISPs.json';
with open(dest, 'w') as outfile:
    json.dump(transit_isps, outfile);
    print("Writing File Job Done!");
