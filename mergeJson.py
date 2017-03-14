import json
json_data_locator_1 = open("data/get_router_graph_json_13.78.81.193.json").read();
json_data_locator_2 = open("data/get_router_graph_json_13.93.223.198.json").read();
json_data_locator_3 = open("data/get_router_graph_json_13.94.154.128.json").read();
json_data_locator_4 = open("data/get_router_graph_json_23.96.248.142.json").read();
json_data_locator_5 = open("data/get_router_graph_json_40.117.35.106.json").read();

parsed_json_1=json.loads(json_data_locator_1);
parsed_json_2=json.loads(json_data_locator_2);
parsed_json_3=json.loads(json_data_locator_3);
parsed_json_4=json.loads(json_data_locator_4);
parsed_json_5=json.loads(json_data_locator_5);

#
# print(parsed_json_1["links"]);
# print(len(parsed_json_1["links"]));
#
# print(parsed_json_2["links"]);
# print(len(parsed_json_2["links"]));
#
# print(parsed_json_3["links"]);
# print(len(parsed_json_3["links"]));
#
# print(parsed_json_4["links"]);
# print(len(parsed_json_4["links"]));
#
# print(parsed_json_5["links"]);
# print(len(parsed_json_5["links"]));

#find number of links in each json
links_json1 = len(parsed_json_1["links"]);
links_json2 = len(parsed_json_2["links"]);
links_json3 = len(parsed_json_3["links"]);
links_json4 = len(parsed_json_4["links"]);
links_json5 = len(parsed_json_5["links"]);

totalNumberOfLinks = links_json1 + links_json2+ links_json3 + links_json4 + links_json5;
print "Total Number of Links";
print totalNumberOfLinks;

#find number of nodes in each json
nodes_json1 = len(parsed_json_1["nodes"]);
nodes_json2 = len(parsed_json_2["nodes"]);
nodes_json3 = len(parsed_json_3["nodes"]);
nodes_json4 = len(parsed_json_4["nodes"]);
nodes_json5 = len(parsed_json_5["nodes"]);


print nodes_json1;
print nodes_json2;
print nodes_json3;
print nodes_json4;
print nodes_json5;

#index for nodes should translate from how many nodes the previous json has
totalNumberOfNodes = nodes_json1 + nodes_json2 + nodes_json3 + nodes_json4 + nodes_json5;
print "Total Number of Nodes";
print totalNumberOfNodes;

#object for merged links
mergedLinks =  [];
mergedNodes = [];
mergedJson = {};

for link in parsed_json_1['links']:
    mergedLinks.append(link);

# print "Links from the locator agent 1";
# print mergedLinks;
# print len(mergedLinks);

for node in parsed_json_1['nodes']:
    mergedNodes.append(node);

#take the number of nodes in the previous json and start numbering the nodes in the current one
#change the indices in the links accordingly
#for example, add the nodes_json1 number to all link values in json2

#merging nodes is easy
for node in parsed_json_2['nodes']:
    mergedNodes.append(node);

#add nodes_json1 to current link source & targets
for link in parsed_json_2['links']:
    link['source'] = link['source'] + nodes_json1;
    link['target'] = link['target'] + nodes_json1;
    mergedLinks.append(link);


#merging nodes is easy
for node in parsed_json_3['nodes']:
    mergedNodes.append(node);

#add nodes_json1 & nodes_json2 to current link source & targets
for link in parsed_json_3['links']:
    link['source'] = link['source'] + nodes_json1 + nodes_json2;
    link['target'] = link['target'] + nodes_json1 + nodes_json2;
    mergedLinks.append(link);


#merging nodes is easy
for node in parsed_json_4['nodes']:
    mergedNodes.append(node);

#add nodes_json1 & nodes_json2 to current link source & targets
for link in parsed_json_4['links']:
    link['source'] = link['source'] + nodes_json1 + nodes_json2 + nodes_json3;
    link['target'] = link['target'] + nodes_json1 + nodes_json2 + nodes_json3;
    mergedLinks.append(link);


#merging nodes is easy
for node in parsed_json_5['nodes']:
    mergedNodes.append(node);

#add nodes_json1 & nodes_json2 to current link source & targets
for link in parsed_json_5['links']:
    link['source'] = link['source'] + nodes_json1 + nodes_json2 + nodes_json3 + nodes_json4;
    link['target'] = link['target'] + nodes_json1 + nodes_json2 + nodes_json3 + nodes_json4;
    mergedLinks.append(link);

mergedJson = {"links": mergedLinks, "nodes": mergedNodes};
print mergedJson['links'];
print mergedJson['nodes'];

#write json into a file
with open('generated/mergedData.json', 'w') as outfile:
    json.dump(mergedJson, outfile);