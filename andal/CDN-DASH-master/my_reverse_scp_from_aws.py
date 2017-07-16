import boto.ec2
import sys
import ast
from boto.manage.cmdshell import sshclient_from_instance
import subprocess
import threading


ip_do_not_touch='54.149.85.236'

# Connect to your region of choice
keys_map={'us-east-1':'sindhu-n-virginia.pem','us-east-2':'sindhu-ohio.pem','us-west-1':'us-west-1-sindhu.pem','us-west-2':'sindhu-us-west-2.pem','ca-central-1':'sindhu-ca-central-1.pem','ap-south-1':'sindhu-ap-south-1.pem','ap-northeast-2':'sindhu-ap-northeast-2.pem','ap-northeast-1':'sindhu-ap-northeast-1.pem','ap-southeast-1':'sindhu-ap-southeast-1.pem','ap-southeast-2':'sindhu-ap-southeast-2.pem','eu-central-1':'sindhu-eu-central-1.pem','eu-west-1':'sindhu-eu-west-1.pem','eu-west-2':'sindhu-eu-west-2.pem','sa-east-1':'sindhu-sa-east-1.pem'}
#regions=['us-east-1','us-east-2','us-west-1','us-west-2','ca-central-1','ap-south-1','ap-northeast-2','ap-northeast-1','ap-southeast-1','ap-southeast-2','eu-central-1','eu-west-1','eu-west-2','sa-east-1']

regions=['us-west-1','us-west-2']


ip_addresses=[]
#args_tarpath='collaborative/CDN-DASH/client_thread.py'

def thread_func(region,):
	try:
		conn = boto.ec2.connect_to_region(region)
		key_path='aws-30-us-west-2-keys/'+keys_map[region]
		reservations = conn.get_all_instances()
		for i in reservations:
			instance=i.instances
			for j in instance:
				try:
					if(j.state=="running"):
						host="ubuntu@"+str(j.ip_address)+":/home/ubuntu/ANDAL/CDN-DASH-master-stability/pingData/"
						cmd=["scp", "-i", key_path, "-o","StrictHostKeyChecking=no","-r", host ,"/home/ubuntu/ANDAL/andal_tar/andal/results/scalability/"]
						subprocess.Popen(cmd)
				except:
					pass
	except:
		e = sys.exc_info()[0]
		print str(e)
		print region
		pass
workers=[]


for region in regions:
#	cmd=["mkdir","june_25_new_exp2_adaptive/"+region+"/"]
#	p=subprocess.Popen(cmd)
	try:
                my_thread = threading.Thread(target=thread_func, args=( region,))
                my_thread.start()
                workers.append(my_thread)

        except:
                e = sys.exc_info()[0]
                print str(e)
                print region
                pass
for i in range(len(workers)):
        try:
                worker = workers[i]
                worker.join()
        except:
                i = i - 1

print "done"

