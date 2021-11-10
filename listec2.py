import boto3
import sys

region = sys.argv[1]
accesskey = sys.argv[2]
secretkey = sys.argv[3]

client = boto3.client('ec2',region_name=region,aws_access_key_id =accesskey,aws_secret_access_key=secretkey)

var_list_ec2_ins = client.describe_instances()
#print (var_list_ec2_ins['Reservations'])

for i in var_list_ec2_ins['Reservations']:
	#print (i['Instances'])
	for j in i['Instances']:
		print (j['ImageId'], j['InstanceId'], j['InstanceType'], j['KeyName'], j['LaunchTime'])
