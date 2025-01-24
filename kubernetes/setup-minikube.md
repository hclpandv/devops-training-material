## Running `minikube`

## Install 

```bash
# Installation 
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# start the cluster
minikube start

# check kubectl working 
kubectl version --short

# metrics-server addon needed for dashboard
minikube addons enable metrics-server

# Install dashboard
# Start a new terminal, and leave this running.
minikube dashboard --url 

# Troubleshoot the dashboard issue with similar command like below 
kubectl logs pod/kubernetes-dashboard-5c5cfc8747-42fb2 --namespace=kubernetes-dashboard

# Stop cluster
minikube stop

```

