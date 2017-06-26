import urllib, json, os
import time
import datetime, numpy

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

# TODO 1: Go through REGION_TIME_ZONES_PATH data
# 1.1: For each planetLab client, filter the files from the DATAQOE_FILE_PATHS for each Cloud Provider
# 1.2  Get QoE data per hour. In total you would have 24 points per <CP, TimeZone, Region> combination

# TODO 2: Plot the data from TODO 1 on time series graph. calculate average QoE, std deviation across
# <CP, TimeZone, Region> combination

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
             'Amazon': [hr1_qoe, hr2_qoe, ... hr23_qoe],
             'Azure': [hr1_qoe, hr2_qoe, ... hr23_qoe],
             'Google': [hr1_qoe, hr2_qoe, ... hr23_qoe]
          },
          { client_name: ""planetlab1.tsuniv.edu",
            providers: {
             'Amazon': [hr1_qoe, hr2_qoe, ... hr23_qoe],
             'Azure': [hr1_qoe, hr2_qoe, ... hr23_qoe],
             'Google': [hr1_qoe, hr2_qoe, ... hr23_qoe]
          },
          ....
         ]
    }
}
'''

def get_hourly_qoe(session_file_paths):

    if len(session_file_paths) == 0:
        return [];

    qoe_values = [];
    for session_file in session_file_paths:
        session_data = json.loads(open(session_file).read());
        mean_qoe = 0;
        for chunk in session_data:
            mean_qoe += session_data[chunk]['QoE2'];

        qoe_val = {
            'qoe': mean_qoe / 120,
            'ts': session_data['0']['TS'],
            'hours': int(datetime.datetime.fromtimestamp(int(session_data['0']['TS'])).strftime('%H')),
            'anomaly': (mean_qoe/120) < 2
        }

        qoe_values.append(qoe_val);

        hourly_qoe_list = []
        # aggregate the duplicate hours
        for i in range(0, 23):
            hour_qoe = filter(lambda e: e['hours'] == i, qoe_values)

            if(len(hour_qoe) > 0):
                hour_qoe = reduce( lambda a, b: {
                    'hours': a['hours'],
                    'ts': a['ts'],
                    'anomaly': ((a['anomaly'] or b['anomaly'])),
                    'qoe': (a['qoe'] + b['qoe'])/2
                }, hour_qoe)
                hourly_qoe_list.append(hour_qoe)

    return hourly_qoe_list

def get_dataQoE_files_for_client(pl_client):
    # print "------------------------------------------------------"
    # print "Gathering session files for providers for ", pl_client
    provider_files_map = {};
    for provider in DATAQOE_FILE_PATHS:
        provider_files_map[provider] = [];
        # pl_client
        # provider
        for session_file in os.listdir(DATAQOE_FILE_PATHS[provider]):
            # ricepl-5.cs.rice.edu_06210600_aws.cmu - agens.com.json
            # print session_file
            session_file_full_path = DATAQOE_FILE_PATHS[provider] + session_file
            if session_file.startswith(pl_client):
                # hours_type = get_hours_type_from_session_file_name(session_file_full_path)
                provider_files_map[provider].append(session_file_full_path);

        # Find QOE means
        provider_files_map[provider] = get_hourly_qoe(provider_files_map[provider])

    # print provider_files_map
    return provider_files_map;

def getMeanFromList(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def get_mean_qoe_for_provider_per_hour(data, provider):
    providerQOEs = []
    for client_data in data:
        if(len(client_data['providers'][provider]) > 0):
            providerQOEs.append(client_data['providers'][provider])

    if(len(providerQOEs) == 0):
        return []
    providerQOEs = numpy.concatenate(providerQOEs)
    # print providerQOEs

    aggregated_qoe_list = []
    for i in range(0, 23):
        hour_qoe = filter(lambda e: e['hours'] == i, providerQOEs)
        if (len(hour_qoe) > 0):
            hour_qoe = reduce(lambda a, b: {
                'ts': a['ts'],
                'hours': a['hours'],
                'qoe': (a['qoe'] + b['qoe']) / 2,
                'anomaly': a['anomaly'] or b['anomaly']
            }, hour_qoe)
            aggregated_qoe_list.append(hour_qoe)

    # print aggregated_qoe_list
    for qoe in  aggregated_qoe_list:
        qoe['anomaly_count'] = len(filter(lambda x: x['hours'] == qoe['hours'] and x['anomaly'], providerQOEs))
    return aggregated_qoe_list

def aggregate_qoe_across_time_zones_per_hour(planetlab_nodes):
    for region in planetlab_nodes:
        for timezone in planetlab_nodes[region]:
            qoes = {
                'AMAZON': get_mean_qoe_for_provider_per_hour(planetlab_nodes[region][timezone], 'AMAZON'),
                'AZURE': get_mean_qoe_for_provider_per_hour(planetlab_nodes[region][timezone], 'AZURE'),
                'GOOGLE': get_mean_qoe_for_provider_per_hour(planetlab_nodes[region][timezone], 'GOOGLE')
            }
            planetlab_nodes[region][timezone] = qoes;

    # write to a file
    # print planetlab_nodes

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

    aggregate_qoe_across_time_zones_per_hour(planetlab_nodes);

    dest = './results/stability/conclusions/' + "qoe_anomaly_freq_24_hours.json";
    with open(dest, 'w') as outfile:
        json.dump(planetlab_nodes, outfile);
        print("Writing File Job Done! " + dest);

init()

# aggregate_qoe_across_time_zones_per_hour(json.loads(open('./results/qoe_hourly_data.json').read()))
