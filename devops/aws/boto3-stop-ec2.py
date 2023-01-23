import boto3

def stop_instance(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(InstanceIds=['i-01234567890abcdef0'])
