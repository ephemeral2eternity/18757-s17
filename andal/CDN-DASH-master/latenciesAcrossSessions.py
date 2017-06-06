import urllib, json, os

dir = './results/pingData/';
clientData = [];
id = 0;
for filename in os.listdir(dir):
    clientDetail = {};

    clientDetail['sNo'] = id;
    clientDetail['latency'] = 0;

    #print clientDetail;

    path = dir + filename;
    json_data = open(path).read();
    parsed_json = json.loads(json_data);
    for elem in parsed_json:
       if(elem == "rttList"):
        print parsed_json[elem];
        latency = round(sum(parsed_json[elem])/3, 2);
        clientDetail['latency'] = latency;

    clientData.append(clientDetail);
    id+= 1;

print clientData;

dest = './results/pingData/' + "clients_latency.json";
with open(dest, 'w') as outfile:
    json.dump(clientData, outfile);
    print("Writing File Job Done! " + dest);

