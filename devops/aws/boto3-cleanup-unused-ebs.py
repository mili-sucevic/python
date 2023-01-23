import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get a list of all EBS volumes
response = ec2.describe_volumes()
volumes = response['Volumes']

# Iterate through the list of volumes
for volume in volumes:
    # Check if the volume is in "available" state
    if volume['State'] == 'available':
        # Get the volume's attachments
        attachments = volume['Attachments']

        # If the volume has no attachments
        if len(attachments) == 0:
            # Delete the volume
            ec2.delete_volume(VolumeId=volume['VolumeId'])
