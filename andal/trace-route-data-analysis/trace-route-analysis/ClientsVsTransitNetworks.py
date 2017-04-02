#Note the transitNetworks.json was generated based on the logic written in scenario1.py

import json
transit_json_data = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/transitNetworks.json").read();
parsed_json_transit=json.loads(transit_json_data);

as_json_data = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/AS_ISP.json").read();
parsed_json_as=json.loads(as_json_data);

transit_isp_json_data = open("/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/transitISPs.json").read();
parsed_json_transit_isp=json.loads(transit_isp_json_data);

clients = [];
#list all clients
#print "Listing all Clients"
for c in parsed_json_transit:
    if c not in clients:
        clients.append(c['client']);
#print clients;

clients_transit_no = [];
for a in parsed_json_as:
    if a['AS'] in parsed_json_transit_isp:
        as_info = {};
        as_info['AS'] = a['AS'];
        as_info['ISP'] = a['ISP'];
        as_info['clients'] = [];
        for c in parsed_json_transit:
            for r in c['routes']:
                if(a['AS'] in r['ISPs']):
                    if c['client'] not in as_info['clients']:
                        as_info['clients'].append(c['client']);
        clients_transit_no.append(as_info);

#print clients_transit_no;

for c in clients_transit_no:
    no_of_clients = 0;
    for n in c['clients']:
        no_of_clients = no_of_clients + 1;
    c['numberOfClients'] = no_of_clients;

dest = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/Client_ISPs.json';
with open(dest, 'w') as outfile:
    json.dump(clients_transit_no, outfile);
    print("Writing File Job Done!");
