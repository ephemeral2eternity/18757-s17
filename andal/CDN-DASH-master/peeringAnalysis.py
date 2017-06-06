import urllib, json, os

dir = './results/routeData/';

sessionDetails = [];
id = 0;
for filename in os.listdir(dir):

    path = dir + filename;
    json_data = open(path).read();
    parsed_json = json.loads(json_data);

    session = {};
    #session ID to identify sessions
    session['id'] = id;
    id+= 1;
    numberOfHops = 0;
    for hop in parsed_json['route']:
        for info in parsed_json['route'][hop]:
            if(info == 'ip'):
                numberOfHops+= 1;

    session['pathLength'] = numberOfHops;
    sessionDetails.append(session);

dest = './results/peerings/' + "pathLengthOfSessions.json";
with open(dest, 'w') as outfile:
    json.dump(sessionDetails, outfile);
    print("Writing File Job Done! " + dest);