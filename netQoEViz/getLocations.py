import urllib

import json
json_data = open("generated/mergedData.json").read();

parsed_json=json.loads(json_data);

location_json = [];
for node in parsed_json['nodes']:
    ip = node['ip'];
    url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
    response = urllib.urlopen(url);
    data = json.loads(response.read());
    location_json.append(data);

locationData = {};
locationData['nodes'] = location_json;
locationData['links'] = parsed_json['links'];

#write json into a file
with open('generated/locationData.json', 'w') as outfile:
    json.dump(locationData, outfile);