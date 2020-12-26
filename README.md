# Kubernetes Shared Volume Mount Testing

This is a simple K8s deployment for testing shared volume mount between multiple pods. The deployment includes:

- ConfigMap as a file mount
- Secret as a file mount
- Shared volume to be used by multiple pods in RW mode

## Requirements

- [Minikube](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/)

## Usage

```bash
# Change docker environment to Minikube's
eval $(minikube -p minikube docker-env)

# Built app container image
make

# Create Persistent Volume
make pv

# Deploy application components
make deploy

# Connect to pod shell
kubectl exec --stdin --tty shell-demo -- /bin/bash

# Expose service
minikube service todo-api-service

# Delete deployment
make remove

minikube service todo-api-service -n todos
```

## References

- [Kubernetes - Using ConfigMap SubPaths to Mount Files](https://dev.to/joshduffney/kubernetes-using-configmap-subpaths-to-mount-files-3a1i)
- [Kubernetes size definitions: What's the difference of “Gi” and “G”?](https://stackoverflow.com/questions/50804915/kubernetes-size-definitions-whats-the-difference-of-gi-and-g)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
