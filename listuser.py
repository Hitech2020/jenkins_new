import boto3
import sys

accesskey = sys.argv[1]
secretkey = sys.argv[2]

client = boto3.client('iam', aws_access_key_id=accesskey,aws_secret_access_key=secretkey)

var_List_users = client.list_users()
#print (var_List_users['Users'])

for new_var in var_List_users['Users']:
	print (new_var['UserName'], new_var['CreateDate'])
#test
