import boto3

def list_s3_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    for bucket in response["Buckets"]:
        print(bucket["Name"])

list_s3_buckets()
