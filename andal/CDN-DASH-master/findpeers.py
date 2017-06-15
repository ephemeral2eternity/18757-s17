import urllib, json, os

dir = './results/routeData/testPeering/';

#Also determining cloud ISP's to calculate performance for direct peerings
cloudISPs = [];
ASToISP = [];

final = [];
for filename in os.listdir(dir):
    data = [];
    #print filename;

    path = dir + filename;
    json_data = open(path).read();
    parsed_json = json.loads(json_data);

    #print parsed_json;

    for elem in parsed_json:
        if(elem == 'route'):
            for i in parsed_json[elem]:
                detail = {};
                detail['index'] = i;
                detail['ip'] = parsed_json[elem][i]['ip'];
                data.append(detail);

    # print data;

    #find peers
    peers = [];
    maxIndex = 0;
    cloudIP = 0;
    for elem in data:
        peering = [];

        i = elem['index'];
        prev = int(i) - 1;
        next = int(i) + 1;

        if int(i) > maxIndex:
            maxIndex = int(i);
            cloudIP = elem['ip'];

        currIP = elem['ip'];
        if(currIP != '*'):
            peering.append(currIP);
            prevIP = {};
            nextIP = {};
            #now find valid before and after elements
            for recElem in data:
                if (prev > 0 and prev == int(recElem['index'])):
                    prevIP = recElem['ip'];
                    if prevIP != {} and prevIP != '*':
                       peering.append(prevIP);
                if (next < data.__len__() and next == int(recElem['index'])):
                   nextIP = recElem['ip'];
                   if nextIP != {} and nextIP != '*':
                       peering.append(nextIP);

        peers.append(peering);

    # print maxIndex
    # print cloudIP
    # print peers;

    #get ISP information of each peerings
    collabs = [];
    for elem in peers:
        # print elem;
        possiblePeer = [];
        i = 0;
        while i < len(elem):
            url = "http://manage.cmu-agens.com/nodeinfo/get_node" + "?ip=" + elem[i];
            response = urllib.urlopen(url);
            data = json.loads(response.read());
            possiblePeer.append(data['AS']);

            as_isp = {
                'AS': data['AS'],
                'ISP': data['ISP']
            };

            if as_isp not in ASToISP:
                ASToISP.append(as_isp);

            # if(cloudIP == elem[i]):
            #     if(data['AS'] not in cloudISPs):
            #         cloudISPs.append(data['AS']);

            i = i + 1;

        # peer = {};
        # if(len(possiblePeer) == 2 or len(possiblePeer) == 3):
        #     if possiblePeer[0] != possiblePeer[1]:
        #         peer = {possiblePeer[0], possiblePeer[1]};
        #
        # if (len(possiblePeer) == 3):
        #     if possiblePeer[1] != possiblePeer[2]:
        #         peer = {possiblePeer[1], possiblePeer[2]};
        #
        # if peer not in collabs:
        #     if peer != {}:
        #         collabs.append(peer);

    # print collabs;

    # for elem in collabs:
    #     newElem = {};
    #     newElem['AS1'] = elem.pop();
    #     newElem['AS2'] = elem.pop();
    #     if newElem not in final:
    #         temp = {};
    #         temp['AS1'] = newElem['AS2'];
    #         temp['AS2'] = newElem['AS1'];
    #         if temp not in final:
    #             final.append(newElem);

# print final;
#
# dest = './results/routeData/testPeering/' + "colloborators.json";
# with open(dest, 'w') as outfile:
#     json.dump(final, outfile);
#     print("Writing File Job Done! " + dest);
#
# print cloudISPs;
# dest = './results/routeData/testPeering/' + "cloudISPs.json";
# with open(dest, 'w') as outfile:
#     json.dump(cloudISPs, outfile);
#     print("Writing File Job Done! " + dest);


print ASToISP;
dest = './results/routeData/testPeering/' + "ISPMapAS.json";
with open(dest, 'w') as outfile:
    json.dump(ASToISP, outfile);
    print("Writing File Job Done! " + dest);
