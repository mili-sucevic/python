import boto3
import json

def delete_s3_bucket(bucket_name):
    s3 = boto3.client("s3")
    response = s3.delete_bucket(
        Bucket=bucket_name
    )
    
    print(json.dumps(response, indent=4))

delete_s3_bucket("my-bucket")
