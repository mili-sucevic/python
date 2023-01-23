import os

# Set the device name of the volume
volume_device = "nvme1n1"

# Set the mount point directory
mount_point = "/mnt/data"

# Create the mount point directory
os.makedirs(mount_point, exist_ok=True)

# Format the volume as ext4 file system
os.system("mkfs.ext4 /dev/{}".format(volume_device))

# Mount the volume to the mount point directory
os.system("mount /dev/{} {}".format(volume_device, mount_point))

# Verify that the volume is mounted
os.system("df -h")
