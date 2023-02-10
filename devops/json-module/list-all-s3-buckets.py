import boto3
import json

def list_s3_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    
    buckets = response["Buckets"]
    for bucket in buckets:
        print(json.dumps(bucket, indent=4))

list_s3_buckets()
