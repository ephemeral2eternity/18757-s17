import urllib, json, os

dir = './results/peerings/colloborators/collobPairs/';
id = 0;
peers = {}

for filename in os.listdir(dir):

    path = dir + filename;

    parsed_json = json.loads(open(path).read());

    AS = []
    for elem in parsed_json:
        if elem['AS1'] not in AS:
            AS.append(elem['AS1']);

        if elem['AS2'] not in AS:
            AS.append(elem['AS2']);

    AS.sort(reverse=False);

    for i in AS:
        if i not in peers:
            peers[i] = []

    for i in AS:
        for elem in parsed_json:
            if(elem['AS1'] == i):
                peers[i].append(elem['AS2']);
                peers[elem['AS2']].append(i);

#find unique, eliminate duplicates
for i in peers:
    peers[i] = list(set(peers[i]));

# print peers;

# dest = './results/pingData/' + "clients_latency.json";
# with open(dest, 'w') as outfile:
#     json.dump(clientData, outfile);
#     print("Writing File Job Done! " + dest);


###### CLOUD ISP'S - FIND PEERS AS & ISP NAMES
dir = './results/peerings/colloborators/cloudISPs/';
cloud_direct_peers_table = [];
for filename in os.listdir(dir):
    path = dir + filename;

    cloud_isps = json.loads(open(path).read());
    isp_as_mapping = json.loads(open('./results/peerings/ISP_AS/ISP_AS.json').read())

    #print peers
    cloud_peer_map = {}
    for elem in cloud_isps:
        cloud_peer_map[elem] = {
            'ispName': isp_as_mapping[str(elem)],
            'peers': []
        }
        for i in peers[elem]:
            cloud_peer_map[elem]['peers'].append({
                'AS': i,
                'ispName': isp_as_mapping[str(i)],
            })

    cloud_direct_peers_table.append({
        'ispName': filename,
        'cloud_peer_map': cloud_peer_map
    })

print json.dumps(cloud_direct_peers_table);

dest = './results/peerings/' + "cloud_direct_peers.json";
with open(dest, 'w') as outfile:
    json.dump(cloud_direct_peers_table, outfile);
    print("Writing File Job Done! " + dest);
