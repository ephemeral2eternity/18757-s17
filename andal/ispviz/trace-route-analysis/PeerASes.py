import urllib, json, os
from collections import defaultdict

################################################################################################################
## retrieving all the peer to peer connections, only counted once
################################################################################################################

peering_relationships =[];
file_count = 0;
#importing routes data and figuring out neighboring AS
dir = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/RouteDataLocationExtraction/';
for filename in os.listdir(dir):
    extract_suffix = filename.split("routesData", 1)[1];
    # print extract_suffix;
    file_count = file_count + 1;
    path = dir + filename;
    json_data_S = open(path).read();
    parsed_json_S=json.loads(json_data_S);

    #processing number of transit networks in the route
    for route_S in parsed_json_S:
        AS = [];
        for r_S in route_S['routes']:
            if(r_S['ip'] != '*'):
                AS.append(r_S['AS']);
            else:
                AS.append('*');

        #print AS;
        numberOfAS = len(AS);

        newASList = [];
        for i in range(len(AS)):
            if (newASList == []):
                newASList.append(AS[i]);
                continue;
            if (AS[i] != newASList[-1]):
                newASList.append(AS[i]);

        # print newASList;
        numberOfnewAS = len(newASList);

        for i,a in enumerate(newASList):
                c = {};
                if numberOfnewAS > 1:
                    if((i-1) < 0):
                        #handling first element
                        if((newASList[i+1] == -1 or newASList[i] == -1) or (newASList[i+1] == '*' or newASList[i] == '*')):
                            continue;
                        else:
                            c['neighborAS'] = newASList[i+1];
                            c['AS'] = newASList[i];

                            if( c != {} ):
                                if c not in peering_relationships:
                                    peering_relationships.append(c);


                    if((i+1) == numberOfnewAS):
                        #handling last element
                        if ((newASList[i - 1] == -1 or newASList[i] == -1) or (
                                newASList[i - 1] == '*' or newASList[i] == '*')):
                            continue;
                        else:
                            c['neighborAS'] = newASList[i-1];
                            c['AS'] = newASList[i];

                            if (c != {}):
                                if c not in peering_relationships:
                                    peering_relationships.append(c);

                    if( ( (i > 0) and (i < (numberOfnewAS - 1)) ) ):
                        #handling the middle elements
                        if ((newASList[i + 1] == -1 or newASList[i] == -1) or (
                                newASList[i + 1] == '*' or newASList[i] == '*')):
                            continue;
                        else:
                            c['neighborAS'] = newASList[i + 1];
                            c['AS'] = newASList[i];

                            if (c != {}):
                                if c not in peering_relationships:
                                    peering_relationships.append(c);

for a in peering_relationships:
    a['toDelete'] = 0;
    a['toBeProcessed'] = 0;

#adding indexes for reference
for i in range(len(peering_relationships)):
    peering_relationships[i]['toBeProcessed'] = 1;
    for j in range(len(peering_relationships)):
        if(i != j):
            if(peering_relationships[j]['toDelete'] != 1 and peering_relationships[j]['toBeProcessed'] != 1):
                if(peering_relationships[i]['AS'] == peering_relationships[j]['neighborAS'] and peering_relationships[i]['neighborAS'] == peering_relationships[j]['AS']):
                    peering_relationships[j]['toDelete'] = 1;

peers = [];
for i,a in enumerate(peering_relationships):
    o = {};
    o['AS'] = peering_relationships[i]['AS'];
    o['neighborAS'] = peering_relationships[i]['neighborAS'];
    if(a['toDelete'] == 1):
        peering_relationships.remove(peering_relationships[i]);
    else:
        peers.append(o);

print peers;

dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/' + "peerings.json";
with open(dest, 'w') as outfile:
    json.dump(peers, outfile);
    print("Writing File Job Done!");


################################################################################################################
## retrieving all the peer to peer connections, calculates frequency
################################################################################################################

for pair in peers:
    pair['number'] = 0;
    dir = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/RouteDataLocationExtraction/';
    for filename in os.listdir(dir):
        extract_suffix = filename.split("routesData", 1)[1];
        path = dir + filename;
        json_data_S = open(path).read();
        parsed_json_S = json.loads(json_data_S);

        # processing number of transit networks in the route
        for route_S in parsed_json_S:
            AS = [];
            for r_S in route_S['routes']:
                if (r_S['ip'] != '*'):
                    AS.append(r_S['AS']);
                else:
                    AS.append('*');

            # print AS;
            numberOfAS = len(AS);

            newASList = [];
            for i in range(len(AS)):
                if (AS[i] != -1 and AS[i] != '*'):
                    if (newASList == []):
                        if (AS[i] != -1 and AS[i] != '*'):
                            newASList.append(AS[i]);
                            continue;
                    if (AS[i] != newASList[-1]):
                        if (AS[i] != -1 and AS[i] != '*'):
                            newASList.append(AS[i]);

            numberOfnewAS = len(newASList);

            for i, a in enumerate(newASList):
                c = {};
                if numberOfnewAS > 1:
                    if ((i - 1) < 0):
                        # handling first element
                        c['neighborAS'] = newASList[i + 1];
                        c['AS'] = newASList[i];

                        if ((c['neighborAS'] == pair['neighborAS'] and c['AS'] == pair['AS']) or (
                                c['neighborAS'] == pair['AS'] and c['AS'] == pair['neighborAS'])):
                            pair['number'] = pair['number'] + 1;

                    if ((i + 1) == numberOfnewAS):
                        # handling last element
                        c['neighborAS'] = newASList[i - 1];
                        c['AS'] = newASList[i];

                        if ((c['neighborAS'] == pair['neighborAS'] and c['AS'] == pair['AS']) or (
                                c['neighborAS'] == pair['AS'] and c['AS'] == pair['neighborAS'])):
                            pair['number'] = pair['number'] + 1;

                    if (((i > 0) and (i < (numberOfnewAS - 1)))):
                        # handling the middle elements
                        c['neighborAS'] = newASList[i + 1];
                        c['AS'] = newASList[i];

                        if ((c['neighborAS'] == pair['neighborAS'] and c['AS'] == pair['AS']) or (
                                c['neighborAS'] == pair['AS'] and c['AS'] == pair['neighborAS'])):
                            pair['number'] = pair['number'] + 1;

print peers;

dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/' + "peeringswithFreq.json";
with open(dest, 'w') as outfile:
    json.dump(peers, outfile);
    print("Writing File Job Done!");

################################################################################################################
## classify if the peerings between client vs transit vs cloud isp's
################################################################################################################
json_data_cloud_isp = open('./generated/cloudISPs.json').read();
parsed_json_cloud=json.loads(json_data_cloud_isp);

json_data_client_isp = open('./generated/clientISPs.json').read();
parsed_json_client = json.loads(json_data_client_isp);

json_data_transit_isp = open('./generated/transitISPs.json').read();
parsed_json_transit = json.loads(json_data_transit_isp);

json_data_peers = open('./generated/peeringswithFreq.json').read();
parsed_json_peers = json.loads(json_data_peers);

cloud_CDN = [];
transit_client =[];
transit_transit = [];

for peer in parsed_json_peers:
    if( peer['AS'] in parsed_json_cloud and peer['neighborAS'] in parsed_json_transit or
                    peer['neighborAS'] in parsed_json_cloud and peer['AS'] in parsed_json_transit):
        cloud_CDN.append(peer);

    if (peer['AS'] in parsed_json_transit and peer['neighborAS'] in parsed_json_client or
                    peer['neighborAS'] in parsed_json_transit and peer['AS'] in parsed_json_client):
        transit_client.append(peer);

    if (peer['AS'] in parsed_json_transit and peer['neighborAS'] in parsed_json_transit or
                    peer['neighborAS'] in parsed_json_transit and peer['AS'] in parsed_json_transit):
        transit_transit.append(peer);
#
# print cloud_CDN;
# print transit_client;
# print transit_transit;

dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/' + "peering_cloud_CDN.json";
with open(dest, 'w') as outfile:
    json.dump(cloud_CDN, outfile);
    print("Writing File Job Done!");


dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/' + "peering_transit_client.json";
with open(dest, 'w') as outfile:
    json.dump(transit_client, outfile);
    print("Writing File Job Done!");

dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/' + "peering_transit_transit.json";
with open(dest, 'w') as outfile:
    json.dump(transit_transit, outfile);
    print("Writing File Job Done!");