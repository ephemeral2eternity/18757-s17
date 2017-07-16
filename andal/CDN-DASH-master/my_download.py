import os
import urllib2, socket, urlparse, httplib
import json
from time import time

cache_response = [];
i = 0;

'''
http://az.cmu-agens.com/videos/BBB/video/9/seg-0.m4f
http://az.cmu-agens.com/videos/BBB/video/5/seg-0.m4f
http://az.cmu-agens.com/videos/BBB/video/1/seg-0.m4f
'''

while i < 10:
    try:
        resp = {}
        t1=time()

        url = 'http://aws.cmu-agens.com/videos/BBB/video/9/seg-84.m4f'

        resp["url"] = url
        u = urllib2.urlopen(url)
        srv_ip_addr = socket.gethostbyname(urlparse.urlparse(u.geturl()).hostname)

        t2 = time()
        resp_time = t2 - t1
        resp["response_time"] = resp_time

        resp["server_ip"] = srv_ip_addr

        cache_response.append(resp)
        i += 1;
    except:
        pass

    try:
        resp = {}
        t1=time()

        url = 'http://az.cmu-agens.com/videos/BBB/video/5/seg-0.m4f'
        resp["url"] = url

        u = urllib2.urlopen(url)
        srv_ip_addr = socket.gethostbyname(urlparse.urlparse(u.geturl()).hostname)

        t2 = time()
        resp_time = t2 - t1
        resp["response_time"] = resp_time

        resp["server_ip"] = srv_ip_addr

        cache_response.append(resp)
        i += 1;
    except:
        pass

    try:
        resp = {}
        t1=time()

        url = 'http://az.cmu-agens.com/videos/BBB/video/1/seg-0.m4f'
        resp["url"] = url

        u = urllib2.urlopen(url)
        srv_ip_addr = socket.gethostbyname(urlparse.urlparse(u.geturl()).hostname)

        t2 = time()
        resp_time = t2 - t1
        resp["response_time"] = resp_time

        resp["server_ip"] = srv_ip_addr

        cache_response.append(resp)
        i += 1;
    except:
        pass

print cache_response

dest = './results/' + "cache_results.json";
with open(dest, 'w') as outfile:
    json.dump(cache_response, outfile);
    print("Writing File Job Done! " + dest);
