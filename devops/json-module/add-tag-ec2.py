import boto3
import json

def add_tag_to_instance(instance_id, key, value):
    ec2 = boto3.client("ec2")
    response = ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {
                "Key": key,
                "Value": value
            }
        ]
    )
    
    print(json.dumps(response, indent=4))

add_tag_to_instance("i-0123456789abcdef0", "Environment", "Production")
