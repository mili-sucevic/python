import boto3
import json

def create_iam_user(user_name):
    iam = boto3.client("iam")
    response = iam.create_user(
        UserName=user_name
    )
    
    print(json.dumps(response, indent=4))

create_iam_user("my-new-user")
