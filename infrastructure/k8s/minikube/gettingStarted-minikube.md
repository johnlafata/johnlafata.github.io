[Get Started!](https://minikube.sigs.k8s.io/docs/start/)

### for mac (m3)
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64

sudo install minikube-darwin-arm64 /usr/local/bin/minikube
````

### get a kubectl version appropriate to minikube version
```bash
minikube kubectl
```

### verify
```bash
kubectl version
```


### create a cluster 
```bash
minikube start
```
#### response
```bash
😄  minikube v1.34.0 on Darwin 14.4.1 (arm64)
✨  Automatically selected the docker driver
📌  Using Docker Desktop driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.45 ...
💾  Downloading Kubernetes v1.31.0 preload ...
    > preloaded-images-k8s-v18-v1...:  307.61 MiB / 307.61 MiB  100.00% 12.93 M
    > gcr.io/k8s-minikube/kicbase...:  441.45 MiB / 441.45 MiB  100.00% 17.02 M
🔥  Creating docker container (CPUs=2, Memory=12200MB) ...
🐳  Preparing Kubernetes v1.31.0 on Docker 27.2.0 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass

❗  /usr/local/bin/kubectl is version 1.29.1, which may have incompatibilities with Kubernetes 1.31.0.
    ▪ Want kubectl v1.31.0? Try 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

## to reconfigure with different cpu or memory settings
minikube stop
minikube delete

minikube kubectl

minikube start  --cpus='4'   --memory=12200MB