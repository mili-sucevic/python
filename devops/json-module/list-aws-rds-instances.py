import boto3
import json

def list_rds_instances():
    rds = boto3.client("rds")
    response = rds.describe_db_instances()
    
    instances = response["DBInstances"]
    for instance in instances:
        print(json.dumps(instance, indent=4))

list_rds_instances()
