import urllib, json, os

dir = './results/peerings/pingData/';

series = [];

for filename in os.listdir(dir):
    obj = {};
    obj['name'] = (filename.split('_')[2]).split('.')[0];
    print obj['name'];

    data = [];

    path = dir + filename;
    json_data = open(path).read();
    parsed_json = json.loads(json_data);

    for elem in parsed_json:
        data.append(elem['latency'])

    obj['data'] = data;

    series.append(obj);

print series;

dest = './results/peerings/pingData/' + "series.json";
with open(dest, 'w') as outfile:
    json.dump(series, outfile);
    print("Writing File Job Done! " + dest);