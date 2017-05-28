## this program does analysis of the trace route data
## based on latency and the path the client has taken
## to get to the server to determine the location of
## the cache server

import os, json
import urllib

path = './results/furtherAnalysis/clients_az.json';
regionPath = './results/furtherAnalysis/planetLabRegionsAz.json';

json_data = open(path).read();
parsed_json = json.loads(json_data);

json_data_region = open(regionPath).read();
parsed_json_region = json.loads(json_data_region);

print parsed_json_region;

#US
USQoE = 0;
countElemUS = 0;

#China
CNQoE = 0;
countElemCN = 0;

#Brazil
BRQoE = 0;
countElemBR = 0;

#New Zealand
NZQoE = 0;
countElemNZ = 0;

#Japan
JPQoE = 0;
countElemJP = 0;

#Canada
CAQoE = 0;
countElemCA = 0;

#Switerland
SWQoE = 0;
countElemSW = 0;

#Poland
PLQoE = 0;
countElemPL = 0;

#Czech
CZQoE = 0;
countElemCZ = 0;

#Australia
AUQoE = 0;
countElemAU = 0;

#Singapore
SGQoE = 0;
countElemSG = 0;

for elem in parsed_json:
    ip = elem['name'];

    url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + ip;
    response = urllib.urlopen(url);
    data = json.loads(response.read());

    if(data['country'] == 'US' or data['country'] == 'United States'):
        USQoE += elem['QoE'];
        countElemUS += 1;

    if (data['country'] == 'CN'):
        CNQoE += elem['QoE'];
        countElemCN += 1;

    if (data['country'] == 'BR'):
        BRQoE += elem['QoE'];
        countElemBR += 1;

    if (data['country'] == 'CA' or data['country'] == 'Canada'):
        CAQoE += elem['QoE'];
        countElemCA += 1;

    if (data['country'] == 'NZ'):
        NZQoE += elem['QoE'];
        countElemNZ += 1;

    if (data['country'] == 'JP'):
        JPQoE += elem['QoE'];
        countElemJP += 1;

    if (data['country'] == 'CH'):
        SWQoE += elem['QoE'];
        countElemSW += 1;

    if (data['country'] == 'PL'):
        PLQoE += elem['QoE'];
        countElemPL += 1;

    if (data['country'] == 'AU'):
        AUQoE += elem['QoE'];
        countElemAU += 1;

    if (data['country'] == 'CZ'):
        CZQoE += elem['QoE'];
        countElemCZ += 1;

    if (data['country'] == 'SG'):
        SGQoE += elem['QoE'];
        countElemSG += 1;

print "Azure US: ", USQoE/countElemUS;
print "Azure China: ", CNQoE/countElemCN;
print "Azure Brazil: ", BRQoE/countElemBR;
print "Azure Canada: ", CAQoE/countElemCA;
print "Azure New Zealand: ", NZQoE/countElemNZ;
print "Azure Japan: ", JPQoE/countElemJP;
print "Azure Switzerland: ", SWQoE/countElemSW;
print "Azure Poland: ", PLQoE/countElemPL;
print "Azure Australia: ", AUQoE/countElemAU;
print "Azure Czech: ", CZQoE/countElemCZ;
print "Azure Singapore: ", SGQoE/countElemSG;

