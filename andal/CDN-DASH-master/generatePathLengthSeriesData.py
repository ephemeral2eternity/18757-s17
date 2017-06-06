import urllib, json, os

dir = './results/peerings/';

series = [];

for filename in os.listdir(dir):
    print filename;

    obj = {};
    obj['name'] = (filename.split('_')[1]).split('.')[0];
    data = [];

    path = dir + filename;
    json_data = open(path).read();
    parsed_json = json.loads(json_data);

    for elem in parsed_json:
        data.append(elem['pathLength'])

    obj['data'] = data;

    series.append(obj);

print series;

dest = './results/peerings/' + "series.json";
with open(dest, 'w') as outfile:
    json.dump(series, outfile);
    print("Writing File Job Done! " + dest);