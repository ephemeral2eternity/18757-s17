import json
import os
for root, dirs, files in os.walk(os.curdir):
	for direc in dirs:
		os.chdir(direc)
		f=open(direc+"_13.txt","w")
		json_files = [pos_json for pos_json in os.listdir(os.curdir) if pos_json.endswith('.json')]	
		count=1
		for js in json_files:
			data=json.loads(open(js).read())
			for i in data:
				f.write(str(data[i]["QoE2"]))
				f.write("\n")
				count=count+1
		os.chdir(os.pardir)
