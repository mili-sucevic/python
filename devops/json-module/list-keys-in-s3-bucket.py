import boto3
import json

def list_s3_bucket_keys(bucket):
    s3 = boto3.client("s3")
    result = s3.list_objects(Bucket=bucket)
    
    keys = [content["Key"] for content in result.get("Contents", [])]
    
    print(json.dumps(keys, indent=4))

list_s3_bucket_keys("my-bucket")
