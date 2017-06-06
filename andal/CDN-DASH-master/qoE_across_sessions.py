import urllib, json, os
from ipinfo.ipinfo import *

dir = './results/dataQoE/';
clientData = [];
id = 0;
for filename in os.listdir(dir):
    clientDetail = {};

    clientDetail['sNo'] = id;
    clientDetail['QoE'] = 0;

    #print clientDetail;

    path = dir + filename;
    json_data = open(path).read();
    parsed_json = json.loads(json_data);
    for elem in parsed_json:
       clientDetail['QoE']+= parsed_json[elem]['QoE2'];

    clientDetail['QoE'] = clientDetail['QoE']/120;
    clientData.append(clientDetail);
    id+= 1;

print clientData;

# dest = './results/furtherAnalysis/' + "clients.json";
# with open(dest, 'w') as outfile:
#     json.dump(clientData, outfile);
#     print("Writing File Job Done! " + dest);

