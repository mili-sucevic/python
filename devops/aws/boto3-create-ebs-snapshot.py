import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get a list of all EBS volumes
response = ec2.describe_volumes()
volumes = response['Volumes']

# Iterate through the list of volumes
for volume in volumes:
    # Create a snapshot of the volume
    response = ec2.create_snapshot(
        VolumeId=volume['VolumeId'],
        Description='Snapshot of volume ' + volume['VolumeId']
    )
    print('Snapshot created with ID: ', response['SnapshotId'])
