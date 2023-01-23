import boto3
import datetime

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get a list of all AMIs
response = ec2.describe_images(Owners=['self'])
images = response['Images']

# Get the current date
now = datetime.datetime.now()

# Iterate through the list of images
for image in images:
    # Get the creation date of the image
    creation_date = datetime.datetime.strptime(image['CreationDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    
    # Calculate the difference between the current date and the creation date
    age = now - creation_date
    
    # If the image is older than 30 days
    if age.days > 30:
        # Deregister the image
        ec2.deregister_image(ImageId=image['ImageId'])
        
        # Get a list of associated snapshots
        for device in image['BlockDeviceMappings']:
            if 'Ebs' in device:
                snapshot_id = device['Ebs']['SnapshotId']
                # Delete the associated snapshot
                ec2.delete_snapshot(SnapshotId=snapshot_id)
