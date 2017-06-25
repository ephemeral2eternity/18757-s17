import urllib, json, os
import time
import datetime

REGION_TIME_ZONES_PATH = './results/planetlab_region.json'
DATAQOE_FILE_PATHS = {
    'AMAZON': './results/stability/weekday/amazon/dataQoE/',
    'AZURE': './results/stability/weekday/azure/dataQoE/',
    'GOOGLE': './results/stability/weekday/google/dataQoE/'
}

'''
{
    "North America": {
        "Central Daylight Time": [
          "ricepl-5.cs.rice.edu", ## planetLab clients...
          "planetlab1.tsuniv.edu",
         ]
    }
}
'''

# DONE: Go through REGION_TIME_ZONES_PATH data
# 1.1: For each planetLab client, filter the files from the DATAQOE_FILE_PATHS for each Cloud Provider
# 1.2 filter files for the sessions that ran during peak hours

# DONE: With the filtered session files, calculate average QoE across session

'''
JSON Output Format:
{
    "Amazon": {
            "North America Central Daylight Time": 4.99,
            "North America Eastern Daylight Time": 3.50,
             ...
        }
    "Azure": {
            "North America Central Daylight Time": 4.99,
            "North America Eastern Daylight Time": 3.50,
             ...
        }
    "Google": {
            "North America Central Daylight Time": 4.99,
            "North America Eastern Daylight Time": 3.50,
             ...
        }
}
'''
# TODO 3: Prepare JSON in the Highcharts format to represent in the Graph

'''
{
    "North America": {
        "Central Daylight Time": [
          { client_name: "ricepl-5.cs.rice.edu",
            providers: {
             'Amazon': [file1, file2, ..],
             'Azure': [file1, file2, ..],
             'Google': [file1, file2, ..]
          },
          { client_name: ""planetlab1.tsuniv.edu",
            providers: {
             'Amazon': [file1, file2, ..],
             'Azure': [file1, file2, ..],
             'Google': [file1, file2, ..]
          },
          ....
         ]
    }
}
'''

def get_hours_type_from_session_file_name(file_name):
    session_data_json = json.loads(open(file_name).read());
    '''
    {
        "0": {
            "Buffer": 4.925218105316162,
            "Freezing": 0,
            "QoE1": 2.5672479960559107,
            "QoE2": 0.1344959921118212,
            "Representation": "1",
            "Response": 0.07282686233520508,
            "Server": "54.230.7.44",
            "TS": 1498034912.52486,
            "curBitRate": 313769
        }
    }
    '''
    timestamp = session_data_json["0"]['TS'];
    # print timestamp
    hours = int(datetime.datetime.fromtimestamp(int(timestamp)).strftime('%H'));
    return {
        'is_peak_hours': 8 <= hours and hours <= 10,
        'is_non_peak_hours': hours <= 2
    }

def get_mean_qoe(session_file_paths):

    if len(session_file_paths) == 0:
        return 0;

    qoe_values = [];
    for session_file in session_file_paths:
        session_data = json.loads(open(session_file).read());
        mean_qoe = 0;
        for chunk in session_data:
            mean_qoe += session_data[chunk]['QoE2'];

        qoe_values.append(mean_qoe/120);

    mean_qoe = 0;
    for chunk in qoe_values:
        mean_qoe += chunk;
    return mean_qoe / len(qoe_values)

def get_dataQoE_files_for_client(pl_client):
    print "------------------------------------------------------"
    print "Gathering session files for providers for ", pl_client
    provider_files_map = {};
    for provider in DATAQOE_FILE_PATHS:
        provider_files_map[provider] = {
            "peak_hours": [],
            "non_peak_hours": []
        };
        # pl_client
        # provider
        for session_file in os.listdir(DATAQOE_FILE_PATHS[provider]):
            # ricepl-5.cs.rice.edu_06210600_aws.cmu - agens.com.json
            # print session_file
            session_file_full_path = DATAQOE_FILE_PATHS[provider] + session_file
            if session_file.startswith(pl_client):
                hours_type = get_hours_type_from_session_file_name(session_file_full_path)
                if(hours_type['is_peak_hours']):
                    provider_files_map[provider]["peak_hours"].append(session_file_full_path);
                if (hours_type['is_non_peak_hours']):
                    provider_files_map[provider]["non_peak_hours"].append(session_file_full_path);

        # Find QOE means
        provider_files_map[provider]["peak_hours_mean_QOE"] = get_mean_qoe(provider_files_map[provider]["peak_hours"])
        provider_files_map[provider]["non_peak_hours_mean_QOE"] = get_mean_qoe(provider_files_map[provider]["non_peak_hours"])

        del provider_files_map[provider]["peak_hours"]
        del provider_files_map[provider]["non_peak_hours"]

    # print provider_files_map

    return provider_files_map;

def getMeanFromList(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def get_mean_qoe_for_provider(data, provider):
    providerQOEs = []
    for client_data in data:
        providerQOEs.append(client_data['providers'][provider])

    result = {
        'peak_hours_qoe': getMeanFromList(map(lambda e: e['peak_hours_mean_QOE'] ,providerQOEs)),
        'non_peak_hours_qoe': getMeanFromList(map(lambda e: e['non_peak_hours_mean_QOE'] ,providerQOEs)),
    }
    return result

def aggregate_qoe_across_time_zones(planetlab_nodes):
    for region in planetlab_nodes:
        for timezone in planetlab_nodes[region]:
            qoes = {
                'AMAZON': get_mean_qoe_for_provider(planetlab_nodes[region][timezone], 'AMAZON'),
                'AZURE': get_mean_qoe_for_provider(planetlab_nodes[region][timezone], 'AZURE'),
                'GOOGLE': get_mean_qoe_for_provider(planetlab_nodes[region][timezone], 'GOOGLE')
            }
            planetlab_nodes[region][timezone] = qoes;

    print planetlab_nodes


def init():
    planetlab_nodes = json.loads(open(REGION_TIME_ZONES_PATH).read());

    for region in planetlab_nodes:
        # print region
        for timezone in planetlab_nodes[region]:
            # print "-- " +  timezone
            for i in range(len(planetlab_nodes[region][timezone])):
                # print "----- " + planetlab_nodes[region][timezone][i]
                pl_client = planetlab_nodes[region][timezone][i];
                planetlab_nodes[region][timezone][i] = {
                    "client_name": pl_client,
                    "providers": get_dataQoE_files_for_client(pl_client)
                }

    aggregate_qoe_across_time_zones(planetlab_nodes);

    dest = './results/stability/conclusions/' + "qoe_peak_non_peak.json";
    with open(dest, 'w') as outfile:
        json.dump(planetlab_nodes, outfile);
        print("Writing File Job Done! " + dest);

init()

# aggregate_qoe_across_time_zones(json.loads(open('./results/qoe_peak_non_peak_aggregate.json').read()))
