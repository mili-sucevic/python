import boto3
import json

def describe_instance(instance_id):
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances(
        InstanceIds=[
            instance_id
        ]
    )
    
    instance = response["Reservations"][0]["Instances"][0]
    print(json.dumps(instance, indent=4))

describe_instance("i-0123456789abcdef0")
