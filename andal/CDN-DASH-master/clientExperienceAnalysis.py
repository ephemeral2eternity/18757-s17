import urllib, json, os

dir = './results/furtherAnalysis/clientExperience/';
parsed_json_amazon = [];
parsed_json_google = [];
parsed_json_azure = [];

for filename in os.listdir(dir):
    print filename;

    if(filename == "clients_amazon.json"):
        path = dir + filename;
        json_data = open(path).read();
        parsed_json_amazon = json.loads(json_data);

    if(filename == "clients_azure.json"):
        path = dir + filename;
        json_data = open(path).read();
        parsed_json_azure = json.loads(json_data);

    if(filename == "clients_google.json"):
        path = dir + filename;
        json_data = open(path).read();
        parsed_json_google = json.loads(json_data);

best_performing = [];

for elem_a in parsed_json_amazon:
    for elem_az in parsed_json_azure:
        for elem_g in parsed_json_google:
            if(elem_a['lon'] == elem_az['lon'] == elem_g['lon']):
                if (elem_a['lat'] == elem_az['lat'] == elem_g['lat']):
                    best = {};
                    if( max( [ elem_a['QoE'], elem_az['QoE'], elem_g['QoE'] ] ) == elem_a['QoE'] ):
                        elem_a['provider'] = 'Amazon';
                        best = elem_a;
                    if (max([elem_a['QoE'], elem_az['QoE'], elem_g['QoE']]) == elem_az['QoE']):
                        elem_az['provider'] = 'Azure';
                        best = elem_az;
                    if (max([elem_a['QoE'], elem_az['QoE'], elem_g['QoE']]) == elem_g['QoE']):
                        elem_g['provider'] = 'Google';
                        best = elem_g;

                    best_performing.append(best);

print best_performing;

dest = './results/furtherAnalysis/clientExperience/' + "bestPerformingCP.json";
with open(dest, 'w') as outfile:
    json.dump(best_performing, outfile);
    print("Writing File Job Done! " + dest);