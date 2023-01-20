# Chaos Monkey

By headintheclouds

## Python Script
This program is a simple script that runs inside a Kubernetes cluster, interacts with the Kubernetes API server, and deletes one pod at random in a particular namespace on a schedule. It is commonly referred to as a "chaos monkey," as it intentionally causes random failures in the cluster to test the resilience and availability of the system.

The script starts by loading the Kubernetes configuration and creating a client to interact with the API server. Then it defines two variables, namespace and interval, which are used to specify the target namespace where the pods are located and the schedule interval for when the script should run and delete a random pod.

It then defines a function called delete_random_pod() which uses the Kubernetes API client to list all the pods in the specified namespace. If there are any pods, it selects one at random and deletes it using the v1.delete_namespaced_pod() method. If there are no pods, the function will print a message indicating that no pods were found in the namespace.

Finally, the script uses the schedule library to schedule the delete_random_pod() function to run every interval minutes. The script then enters an infinite loop where it repeatedly calls the schedule.run_pending() method and sleeps for 1 second between iterations.

## Usage
1. Build the container image:
```bash
chmod +x 01-chaos-monkey-docker-image.sh
./01-chaos-monkey-docker-image.sh
```

2. Create RBAC:
```bash
kubectl apply -f 02-chaos-monkey-rbac.yml
``` 

3. Deploy chaos-monkey in a default namespace:
```bash
kubectl apply -f 03-chaos-monkey-deploy.yml
```

4. Deploy demo workload in workloads namespace:
```bash
kubectl apply -f 04-chaos-monkey-demo-workload.yml
```

5. Delete all resources
```bash
chmod +x 05-delete-all-k8s-resources.sh
./05-delete-all-k8s-resources.sh
```

Customize the schedule interval and namespace in chaos-monkey.py and rebuild the image.

Verify that the script is running and deleting pods as expected.

## Note
- This script is intended for testing and development purposes only. Do not use it in a production environment without proper testing and validation.
- This script uses the schedule library which is not an official python library, if you face any issues with it, you can use other scheduling libraries.
- Be careful when using this script, as it can cause significant disruptions to your system and lead to data loss.
- Make sure you have the right permissions to interact with the kubernetes api server
- Customize the script and the manifests according to your needs
