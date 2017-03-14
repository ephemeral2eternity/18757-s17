import json

json_data_locator = open("generated/locationData.json").read();

parsed_json = json.loads(json_data_locator);

print "AS that needs to be fixed"
for i in parsed_json:
    if(i['AS'] == -1):
     print i['ip'];







