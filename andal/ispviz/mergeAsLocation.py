import json

json_data_locator = open("generated/locationData.json").read();

parsed_json = json.loads(json_data_locator);

merged_json_nodes = [];
merged_json_links = [];
#ignoring the data if it's AS number is -1 - needs processing
for i in parsed_json['nodes']:
    if(i['AS'] != -1):
      merged_json_nodes.append(i);

for i in parsed_json['links']:
    merged_json_links.append(i);

#Merge nodes based on the same AS & Location(latitude & longitude)
#Generate a new graph file: {"nodes": [network_group], "links": [network_link]}
#Verify All routers that belong to the same AS shares the same ISP name
#Verify if they are at the same location, they share the same city, region, and country info.
#Record the number of all nodes that is in the ISP at a certain location in "number" in the
#following network group info.

# example: Network group: {
#               "name": ISP,
#               "AS": Asnumber,
#               "latitude": latitude,
#               "longitude": longitude,
#               "city": city,
#               "region": region,
#               "country": country,
#               "number": #}

merged_group_AS =[];
#print len(merged_json_nodes);
count = 0;

#first step: group based on AS & location

#counts occurrences and add the number attribute
for i in merged_json_nodes:
    number = 0;
    count = 0;
    for j in merged_json_nodes:
        if(i['AS'] == j['AS']) and i['longitude'] == j['longitude'] and i['latitude'] == j['latitude']:
            if(count == 0):
                number = 1;
                count = 1;
            else:
                number = number + 1;
        i['number'] = number;


count = 0;
found = 0;
index = -1;
#creates new json with node as nodegroups
for i in merged_json_nodes:
    found = 0;
    index = index + 1;
    m = {};
    if(i['number'] == 1):
        m['name'] = i['ISP'];
        m['AS'] = i['AS'];
        m['latitude'] = i['latitude'];
        m['longitude'] = i['longitude'];
        m['city'] = i['city'];
        m['region'] = i['region'];
        m['country'] = i['country'];
        m['number'] = i['number'];
        m['nodeIndices'] = [];
        m['nodeIndices'].append(index);
        merged_group_AS.append(m);
    else:
        #check if node exists in merged_group_AS already, else add it
        if(count == 0):
            m = {};
            m['name'] = i['ISP'];
            m['AS'] = i['AS'];
            m['latitude'] = i['latitude'];
            m['longitude'] = i['longitude'];
            m['city'] = i['city'];
            m['region'] = i['region'];
            m['country'] = i['country'];
            m['number'] = i['number'];
            m['nodeIndices'] = [];
            m['nodeIndices'].append(index);
            merged_group_AS.append(m);
            count = 1;
        else:
             for j in merged_group_AS:
                 if (i['AS'] == j['AS']) and i['longitude'] == j['longitude'] and i['latitude'] == j['latitude']:
                     j['nodeIndices'].append(index);
                     found = 1;
                     break;

             if (found == 0):
                 m = {};
                 m['name'] = i['ISP'];
                 m['AS'] = i['AS'];
                 m['latitude'] = i['latitude'];
                 m['longitude'] = i['longitude'];
                 m['city'] = i['city'];
                 m['region'] = i['region'];
                 m['country'] = i['country'];
                 m['number'] = i['number'];
                 m['nodeIndices'] = [];
                 m['nodeIndices'].append(index);
                 merged_group_AS.append(m);



#Merge the links into network group,
#All links that are connected to nodes in a network group are considered connecting to the network group.
#Similarly, count the number of all links that connect nodes in two network groups

#example:  Network Link: {
#               "group": "inter",     //is "intra" if source and target network groups are within same AS, otherwise, it is "inter"
#               "count": #,           //The number of links that connect routers in two network groups
#               "target": 1,          //Denote the target network group index in the "nodes" list that contains all network groups
#               "source": 2          //Denote the source network group index in the "nodes" list that contains all network groups
#               }

#mark links which have source nodes as the nodes we are inspecting
#mark links which have target nodes as the nodes we are inspecting
#inspect AS of each node, its source's and target's to figure out if it's inter or intra group link

merged_group_links = [];
print len(merged_json_links);

indexi = 0;
indexj = 0;
iter = 1;

for i in merged_group_AS:
    count = 0;
    indexj = 0;
    for j in merged_group_AS:
        for k in i['nodeIndices']:
            for l in j['nodeIndices']:
                if(indexi != indexj):
                    for m in merged_json_links:
                        #if((k == m['source'] and l == m['target']) or (l == m['source'] and k == m['target'])):
                        if ((k == m['source'] and l == m['target'])):
                            o = {};
                            count = count + 1;
                            o['count'] = count;
                            o['source'] = indexi;
                            o['target'] = indexj;
                            o['group'] = "inter"; #need to determine this
                            if(iter == 1):
                                merged_group_links.append(o);
                                iter = 0;
                            else:
                                for a in merged_group_links:
                                    if(a['source'] == o['source'] and a['target'] == o['target']):
                                        a['count'] = a['count'] + 1;
                                        break;
                                    else:
                                        merged_group_links.append(o);
                                        break;

        indexj = indexj + 1;
    indexi = indexi + 1;


final_json = {};
final_json['nodes'] = merged_group_AS;
final_json['links'] = merged_group_links;
print len(merged_group_AS);
print len(merged_group_links);

# write json into a file
with open('generated/final.json', 'w') as outfile:
     json.dump(final_json, outfile);