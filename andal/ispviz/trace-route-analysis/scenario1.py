#runs the javascript "testscipt.js" which does initial processing of the json data and generates files
#trace_route_analysis_files for the data inputted.
#It processes the trace route files generated and create RouteData prefixed files which is then used to
#generated files grouped by AS and eventually the transitNetworks.json that has data client by client
#which all transit networks it uses.

import urllib, json, os
from collections import defaultdict

# from subprocess import call
#
# # Note that you have to specify path to script
# call(["node", "testscript.js"]);

# ######################################################################################################
# ## processes each trace route data and fetches location, AS information for each hop
# ######################################################################################################

#dir = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/traceRouteStep1Extraction/';
dir = "./generated/traceRouteStep1Extraction/";
for filename in os.listdir(dir):
    #print filename;
    path = dir + filename;
    extract_suffix = filename.split("trace-route-analysis",1)[1];

    if(extract_suffix == "_planetlab3.rutgers.edu_02060550_cache.json"):
        #print "Ignoring planetlab3 rutgers"
        continue;

    flag = 0;
    dest_dir = './generated/RouteDataLocationExtraction/';
    dest = './generated/RouteDataLocationExtraction/' + "routesData" + extract_suffix;
    for route_file in os.listdir(dest_dir):
        route_file = dest_dir + route_file;
        if(route_file == dest):
            #print('breaking');
            flag = 1;
            break;

    if(flag == 0):
	try:
	   json_data = open(path).read();
           parsed_json=json.loads(json_data);
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
           #print 'Decoding JSON has failed'
	   continue;
        #Analyzing routes in cached version
        routesJson = [];
        for node in parsed_json:
            r = {};
            r['ip'] = node['name'];
            r['name'] = node['id'];
            r['timeTaken'] = node['timeTaken'];
            r['hops'] = node['hops'];
            r['routes'] = [];
            for route in node['routes']:
                o = {};
                ip = route['id'];
                o['ip'] = ip;
                o['time'] = route['time'];
                if(ip != '*'):
                    url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
                    response = urllib.urlopen(url);
                    data = json.loads(response.read());
                    o['AS']= data['AS'];
                    o['ISP'] = data['ISP'];
                r['routes'].append(o);
            routesJson.append(r);

        #write json into a file
        #dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/' + "routesData" + extract_suffix;
        dest = './generated/RouteDataLocationExtraction/' + "routesData" + extract_suffix;
        with open(dest, 'w') as outfile:
            json.dump(routesJson, outfile);
            #print("Writing File Job Done! " + "routesData" + extract_suffix);

################ Trace Route Ordering Maintained Until Here ###########################
#
# ######################################################################################################
# ## processes each route data file and groups them as per AS
# ######################################################################################################
# #validating if every trace route file there exists route data file
#
# #importing routes data and working on it
# dir = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/RouteDataLocationExtraction/';
# for filename in os.listdir(dir):
#     print filename;
#     extract_suffix = filename.split("routesData", 1)[1];
#     print extract_suffix;
#     path = dir + filename;
#     json_data_S = open(path).read();
#     parsed_json_S=json.loads(json_data_S);
#
#     transit = [];
#     #processing number of transit networks in the route
#     for route_S in parsed_json_S:
#         d = defaultdict(list);
#         o = {};
#         o['ip'] = route_S['ip'];
#         o['name'] = route_S['name'];
#         o['timeTaken'] = route_S['timeTaken'];
#         o['hops'] = route_S['hops'];
#         for r_S in route_S['routes']:
#             if 'AS' in r_S:
#                 if r_S['AS']:
#                     key = r_S['AS'];
#                     d[key].append(r_S);
#             o['routes'] = d;
#         transit.append(o);
#
#     dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/GroupedDataByAS/' + "grouped" + extract_suffix;
#     with open(dest, 'w') as outfile:
#         json.dump(transit, outfile);
#         print("Writing File Job Done!");
#
# ######################################################################################################
# ## module to figure out nodes with discrepant AS
# ######################################################################################################
#
# # discrepancy_nodes = [];
# # dir = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/RouteDataLocationExtraction/';
# # for filename in os.listdir(dir):
# #     print filename;
# #     extract_suffix = filename.split("routesData", 1)[1];
# #     print extract_suffix;
# #     path = dir + filename;
# #     json_data_S = open(path).read();
# #     parsed_json_S=json.loads(json_data_S);
# #
# #     #processing number of transit networks in the route
# #     for route_S in parsed_json_S:
# #         for r_S in route_S['routes']:
# #             if 'AS' in r_S:
# #                 if r_S['AS']:
# #                     if(r_S['AS'] == -1):
# #                         if r_S['ip'] not in discrepancy_nodes:
# #                             discrepancy_nodes.append(r_S['ip']);
# #
# # dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/discrepant_AS.json';
# # with open(dest, 'w') as outfile:
# #     json.dump(discrepancy_nodes, outfile);
# #     print("Writing File Job Done!");
#
# ######################################################################################################
# ## calculating number of transit networks per route
# ######################################################################################################
# dir = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/GroupedDatabyAS/';
# t = [];
# as_isp_name_graph = [];
# isp_vs_routers_graph = [];
# for filename in os.listdir(dir):
#     path = dir + filename;
#     extract_suffix = (filename.split("_", 1)[1]).split("_", 1)[0];
#     # print extract_suffix;
#     json_data_transit_S = open(path).read();
#     parsed_json_transit_S = json.loads(json_data_transit_S);
#
#     o = {};
#     o['client'] = extract_suffix;
#     l = [];
#
#     for r in parsed_json_transit_S:
#         count = 0;
#         isp = [];
#         m = {};
#         m['server'] = r['name'];
#         for a in r['routes']:
#             as_i = {};
#             isp_r = {};
#             # k = {};
#             # k['ISP'] = r['routes'][a][0]['ISP'];
#             # k['AS'] = r['routes'][a][0]['AS'];
#             isp.append(r['routes'][a][0]['AS']);
#             count=count + 1;
#             as_i['AS'] = r['routes'][a][0]['AS'];
#             as_i['ISP'] = r['routes'][a][0]['ISP'];
#             isp_r['AS'] = r['routes'][a][0]['AS'];
#             isp_r['ISP'] = r['routes'][a][0]['ISP'];
#             isp_router = 0;
#             for ir in r['routes'][a]:
#                 isp_router = isp_router + 1;
#             isp_r['routerCount'] = isp_router;
#             found = 0;
#
#             for i in isp_vs_routers_graph:
#                 if(i['AS'] == isp_r['AS']):
#                     found = 1;
#                     if(i['routerCount'] < isp_r['routerCount']):
#                         i['routerCount'] = isp_r['routerCount'];
#                     break;
#
#             if(found == 0):
#                 isp_vs_routers_graph.append(isp_r);
#
#             if as_i not in as_isp_name_graph:
#                 as_isp_name_graph.append(as_i);
#
#         m['transit'] = count;
#         m['ISPs'] = isp;
#         l.append(m);
#
#     o['routes'] = l;
#     t.append(o);
#
# #print t;
# print isp_vs_routers_graph;
#
# dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/transitNetworks.json';
# with open(dest, 'w') as outfile:
#     json.dump(t, outfile);
#     print("Writing File Job Done!");
#
# dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/AS_ISP.json';
# with open(dest, 'w') as outfile:
#     json.dump(as_isp_name_graph, outfile);
#     print("Writing File Job Done!");
#
# dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/ISP_Routers.json';
# with open(dest, 'w') as outfile:
#     json.dump(isp_vs_routers_graph, outfile);
#     print("Writing File Job Done!");
#
