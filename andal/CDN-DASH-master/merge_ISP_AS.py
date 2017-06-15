import urllib, json, os
import numpy

dir = './results/peerings/ISP_AS/';

globalISPASMap = [];
IspAsMap = {};

for filename in os.listdir(dir):

    path = dir + filename;

    parsed_json = json.loads(open(path).read());

    for elem in parsed_json:
        IspAsMap[elem['AS']] = elem['ISP'];

print IspAsMap

dest = './results/peerings/ISP_AS/' + "ISP_AS.json";
with open(dest, 'w') as outfile:
    json.dump(IspAsMap, outfile);
    print("Writing File Job Done! " + dest);

