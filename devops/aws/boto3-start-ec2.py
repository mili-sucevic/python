import boto3

def start_instance(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.start_instances(InstanceIds=['i-01234567890abcdef0'])
