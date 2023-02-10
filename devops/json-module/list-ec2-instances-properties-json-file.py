import boto3
import json

def list_ec2_instances(file):
    ec2 = boto3.client("ec2")
    instances = ec2.describe_instances()
    
    with open(file, "w") as f:
        json.dump(instances, f, indent=4)

list_ec2_instances("ec2_instances.json")
