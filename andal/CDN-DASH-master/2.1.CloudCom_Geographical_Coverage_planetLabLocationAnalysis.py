import urllib, json, os
import time
from ipinfo.ipinfo import *

PLANETLAB_NODES_PATH = './results/planetLabNodes/'
GET_NODE_URL_PATH = 'http://manage.cmu-agens.com/nodeinfo/get_node'
#https://maps.googleapis.com/maps/api/timezone/json?location=37.77492950,-122.41941550&timestamp=1498353091&sensor=false
MAP_TIMEZONE_API = 'https://maps.googleapis.com/maps/api/timezone/json?location='
planetlab_region = {};
country_codes = [];
cities = [];
regions = ['North America', 'South America', 'Europe', 'Asia', 'Australia']

for filename in os.listdir(PLANETLAB_NODES_PATH):
    print filename

    planetlab_nodes = open(PLANETLAB_NODES_PATH + filename).read();

    planetlab_region['North America'] = {};
    planetlab_region['South America'] = {};
    planetlab_region['Europe'] = {};
    planetlab_region['Asia'] = {};
    planetlab_region['Australia'] = {};

    with open((PLANETLAB_NODES_PATH + filename)) as f:
        for line_terminated in f:
            line = line_terminated.rstrip('\n')
            #print line

            ip = host2ip(line);
            print ip
            url = GET_NODE_URL_PATH + '?ip=' + ip;
            response = urllib.urlopen(url);
            data = json.loads(response.read());

            location = data['latitude'] + "," + data['longitude']

            timeZoneName = 'unknown'
            map_url = MAP_TIMEZONE_API + location + "&timestamp=" + str(time.time()) + "&sensor=false";
            response = urllib.urlopen(map_url);
            map_data = json.loads(response.read());
            if map_data['status'] == 'OK':
                timeZoneName = map_data['timeZoneName']

            if data['country'] not in country_codes:
                country_codes.append(data['country']);

            if data['region'] not in cities:
                cities.append(data['region']);

            if data['country'] != {}:
                if(data['country'] in ['US', 'CA', 'United States', 'Canada'] ):
                    if timeZoneName not in planetlab_region['North America']:
                        planetlab_region['North America'][timeZoneName] = [];

                    if line not in planetlab_region['North America'][timeZoneName]:
                        planetlab_region['North America'][timeZoneName].append(line)

                if(data['country'] == 'BR'):
                    if timeZoneName not in planetlab_region['South America']:
                        planetlab_region['South America'][timeZoneName] = [];

                    if line not in planetlab_region['South America'][timeZoneName]:
                        planetlab_region['South America'][timeZoneName].append(line)

                if (data['country'] in ['PT', 'Czech Republic', 'SW', 'PL', 'CZ', 'FR', 'FI',
                                        'BE', 'IT', 'AR', 'NO', 'DE', 'ES', 'SE'] ):
                    if timeZoneName not in planetlab_region['Europe']:
                        planetlab_region['Europe'][timeZoneName] = [];

                    if line not in planetlab_region['Europe'][timeZoneName]:
                        planetlab_region['Europe'][timeZoneName].append(line)

                if (data['country'] in ['AU', 'NZ']):
                    if timeZoneName not in planetlab_region['Australia']:
                        planetlab_region['Australia'][timeZoneName] = [];

                    if line not in planetlab_region['Australia'][timeZoneName]:
                        planetlab_region['Australia'][timeZoneName].append(line)

                if (data['country'] in ['CN', 'JP', 'SG', 'Japan', 'RU']):
                    if timeZoneName not in planetlab_region['Asia']:
                        planetlab_region['Asia'][timeZoneName] = [];

                    if line not in planetlab_region['Asia'][timeZoneName]:
                        planetlab_region['Asia'][timeZoneName].append(line)

                if (data['country'] not in ['US', 'CA', 'United States', 'BR','PT', 'Czech Republic',
                                            'SW', 'PL', 'CZ', 'AU', 'NZ', 'CN', 'JP', 'SG', 'Japan',
                                            'FR', 'FI', 'BE', 'Canada', 'IT', 'AR', 'NO', 'DE', 'ES',
                                            'SE', 'RU']):
                    print line, ip, data['country']

dest = './results/' + "planetlab_region.json";
with open(dest, 'w') as outfile:
    json.dump(planetlab_region, outfile);
    print("Writing File Job Done! " + dest);

#print planetlab_region
#print cities
#print country_codes
#print regions

# for region in regions:
#     nodes = planetlab_region[region]['zone1'];
#     print nodes;