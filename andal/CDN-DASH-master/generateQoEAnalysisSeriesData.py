import urllib, json, os
import numpy, math

dir = './results/peerings/clients_QoE/';

series = [];

for filename in os.listdir(dir):
    print filename;

    obj = {};
    obj['name'] = (filename.split('_')[2]).split('.')[0];
    print obj['name'];
    data = [];

    path = dir + filename;
    json_data = open(path).read();
    parsed_json = json.loads(json_data);

    for elem in parsed_json:
        data.append(round(elem['QoE'],2))

    obj['data'] = data;

    series.append(obj);

print series;


def mean(data):
    return sum(data) / len(data)


def variance(data):
    # Use the Computational Formula for Variance.
    n = len(data)
    ss = sum(x ** 2 for x in data) - (sum(data) ** 2) / n
    return ss / (n - 1)


def standard_deviation(data):
    return math.sqrt(variance(data))


print "Mean: ", numpy.mean(data);
print "Median: ", numpy.median(data);
print "Variance: ", variance(data);
print "Std Deviation: ", standard_deviation(data);
#
# dest = './results/peerings/clients_QoE/' + "series.json";
# with open(dest, 'w') as outfile:
#     json.dump(series, outfile);
#     print("Writing File Job Done! " + dest);