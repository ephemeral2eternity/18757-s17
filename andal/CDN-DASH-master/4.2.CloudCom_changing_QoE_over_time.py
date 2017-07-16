'''
Measure the trend with which QoE changes over time
with increasing number of clients

Processing the data for US-West Amazon Web Services

Requests were placed starting with powers of 2.
<2, 4, 8, 16, 32 .... 1024> during the night, (12 - 3 AM, PST)

'''

import os, json
import datetime

DATA_QOE_FILES_PATH = './results/scalability/amazon/dataQoE/'
DESTINATION_PATH_TS = './results/scalability/conclusions/' + "qoe_over_time_aws_with_ts.json";
DESTINATION_PATH_QOE = './results/scalability/conclusions/' + "qoe_over_time_aws_without_ts.json";
timeStamps = [];
unixTimeStamps = [];

# example file name -  "ec2-34-223-229-37.us-west-2.compute.amazonaws.com_06130826_aws.cmu-agens.com.json"

for filename in os.listdir(DATA_QOE_FILES_PATH):
    file_path = DATA_QOE_FILES_PATH + filename

    #sort based on the time stamp
    unixTimeStamps.append(int(filename.split('_')[1]));

    data_qoe_json = json.loads(open(file_path).read())

unixTimeStamps = sorted(unixTimeStamps, key=int, reverse=False);
# print unixTimeStamps
# print len(unixTimeStamps)

# for time_stamp in unixTimeStamps:
#     timeStamps.append(datetime.datetime.fromtimestamp(time_stamp).strftime('%H %M %S'))
#
# growing_qoe_over_time = {};
#

# TODO: 1. Sort all the dataQoE files based on timestamps in US-West
#      2. Based on timestamps, go into each file that matches that timestamp -
#             1.  Read the TS value in the chunk
#             2.  Accumulate the same TS value files and aggregate their QoE
#             3.  Format for this result JSON:
#                    {  "1432425452": [ list of QoE's ],
#                       "1432425452": [ list of QoE's ],
#                        ...
#                    }
# 		      4. This result JSON represents QoE over time for different set of clients over time

qoe_across_clients = {};
error_client_sessions = [];
for filename in os.listdir(DATA_QOE_FILES_PATH):
    file_path = DATA_QOE_FILES_PATH + filename

    data_qoe_json = json.loads(open(file_path).read())
    timeStamp = data_qoe_json["0"]['TS'];
    qoe_across_clients[timeStamp] = [];

for filename in os.listdir(DATA_QOE_FILES_PATH):
    file_path = DATA_QOE_FILES_PATH + filename

    data_qoe_json = json.loads(open(file_path).read())
    timeStamp = data_qoe_json["0"]['TS'];

    qoe = 0;
    chunkLength = 0
    for chunk in data_qoe_json:
        qoe += data_qoe_json[chunk]['QoE2'];
        chunkLength += 1

    if(chunkLength < 120):
        error_client_sessions.append(file_path)

    qoe = qoe /120;

    qoe_across_clients[timeStamp] = qoe

#print qoe_across_clients;
# print json.dumps(qoe_across_clients, sort_keys=True)
# print error_client_sessions

qoe_series_data = [];
for elem in qoe_across_clients:
    qoe_series_data.append(round(qoe_across_clients[elem], 2));

print qoe_series_data

with open(DESTINATION_PATH_TS, 'w') as outfile:
    json.dump(qoe_across_clients, outfile);
    print("Writing File Job Done! " + DESTINATION_PATH_TS);

with open(DESTINATION_PATH_QOE, 'w') as outfile:
    json.dump(qoe_series_data, outfile);
    print("Writing File Job Done! " + DESTINATION_PATH_QOE);
