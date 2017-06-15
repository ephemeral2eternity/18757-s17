import boto.ec2
import sys
from boto.manage.cmdshell import sshclient_from_instance

ip_do_not_touch = '54.149.85.236'

# Connect to your region of choice
keys_map = {'us-east-1': 'sindhu-n-virginia.pem', 'us-east-2': 'sindhu-ohio.pem', 'us-west-1': 'us-west-1-sindhu.pem',
            'us-west-2': 'sindhu-us-west-2.pem', 'ca-central-1': 'sindhu-ca-central-1.pem',
            'ap-south-1': 'sindhu-ap-south-1.pem', 'ap-northeast-2': 'sindhu-ap-northeast-2.pem',
            'ap-northeast-1': 'sindhu-ap-northeast-1.pem', 'ap-southeast-1': 'sindhu-ap-southeast-1.pem',
            'ap-southeast-2': 'sindhu-ap-southeast-2.pem', 'eu-central-1': 'sindhu-eu-central-1.pem',
            'eu-west-1': 'sindhu-eu-west-1.pem', 'eu-west-2': 'sindhu-eu-west-2.pem',
            'sa-east-1': 'sindhu-sa-east-1.pem'}
# regions=['us-east-1','us-east-2','us-west-1','us-west-2','ca-central-1','ap-south-1','ap-northeast-2','ap-northeast-1','ap-southeast-1','ap-southeast-2','eu-central-1','eu-west-1','eu-west-2','sa-east-1']
regions = ['us-east-1']
ip_addresses = []
args_tarpath = 'collaborative/CDN-DASH/client_thread.py'

for region in regions:

    # conn = boto.ec2.connect_to_region('us-east-1')
    try:
        conn = boto.ec2.connect_to_region(region)
        key_path = 'aws-30-us-west-2-keys/' + keys_map[region]
        reservations = conn.get_all_instances()
        for i in reservations:
            instance = i.instances
            for j in instance:
                if (j.ip_address != '54.202.114.94' and j.state != "running"):
                    # ssh_client = boto.manage.cmdshell.sshclient_from_instance(j, key_path,host_key_file='~/.ssh/known_hosts', user_name='ubuntu')
                    # ssh_client.put_file(args_tarpath,"/home/ubuntu/collaborative/CDN-DASH/client_thread.py" )
                    j.start()
    except:
        e = sys.exc_info()[0]
        print str(e)
        print region
        pass
