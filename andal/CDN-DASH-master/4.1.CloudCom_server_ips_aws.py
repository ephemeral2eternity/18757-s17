'''
extract server IP's serving traffic across requests for AWS
'''

import json, os

DATA_QOE_FILES_PATH = './results/scalability/google/dataQoE/'
DESTINATION_PATH = './results/scalability/conclusions/' + "server_ips_google.json";
server_ips = [];

#
# for filename in error_files:
#     print filename
#     data_qoe_json = json.loads(open(filename).read())
#
#     for chunk in data_qoe_json:
#         if data_qoe_json[chunk]['Server'] not in server_ips:
#             server_ips.append(data_qoe_json[chunk]['Server'])


for filename in os.listdir(DATA_QOE_FILES_PATH):
    print filename

    file_path = DATA_QOE_FILES_PATH + filename
    print file_path

    try:
        data_qoe_json = json.loads(open(file_path).read())

        for chunk in data_qoe_json:
            if data_qoe_json[chunk]['Server'] not in server_ips:
                server_ips.append(data_qoe_json[chunk]['Server'])

    except ValueError:
        print file_path

print len(server_ips)

with open(DESTINATION_PATH, 'w') as outfile:
    json.dump(server_ips, outfile);
    print("Writing File Job Done! " + DESTINATION_PATH);