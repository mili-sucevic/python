import boto3
import json

def create_s3_bucket(bucket, file):
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket=bucket)
    
    with open(file, "r") as f:
        data = json.load(f)
    
    s3.put_object(Bucket=bucket, Key=file, Body=json.dumps(data))

create_s3_bucket("my-bucket", "data.json")
