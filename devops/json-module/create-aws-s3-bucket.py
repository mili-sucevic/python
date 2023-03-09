import boto3
import json

def create_s3_bucket(bucket_name):
    s3 = boto3.client("s3")
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": "us-west-2"
        }
    )
    
    print(json.dumps(response, indent=4))

create_s3_bucket("my-new-bucket")
