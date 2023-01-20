import random
import schedule
import time
from kubernetes import client, config

# Load Kubernetes config
config.load_incluster_config()

# Create a Kubernetes API client
v1 = client.CoreV1Api()

# Set the namespace and schedule interval
namespace = "workloads"
interval = 2

# Function to delete a random pod in the namespace
def delete_random_pod():
    pods = v1.list_namespaced_pod(namespace).items
    if pods:
        random_pod = random.choice(pods)
        v1.delete_namespaced_pod(random_pod.metadata.name, namespace)
        print(f"Deleted pod {random_pod.metadata.name} in namespace {namespace}")
    else:
        print(f"No pods found in namespace {namespace}")

# Schedule the function to run every interval
schedule.every(interval).minutes.do(delete_random_pod)

while True:
    schedule.run_pending()
    time.sleep(1)
