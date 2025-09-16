# Getting Started with Amazon EKS - using eksctl

### installation of ekscli
https://eksctl.io/installation/

### install on macOS
```
brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
```

### create a basic cluster in minutes
```
eksctl create cluster
```
response
```
...
2025-05-31 15:42:01 [✔]  EKS cluster "fabulous-sheepdog-1748719678" in "us-east-1" region is ready
```

### verify the clusters
```
eksctl get cluster --name fabulous-sheepdog-1748719678 --region us-east-1
```

### get kubernetes configure  [ this is done at cluster creation time, but if needed again this will set kubeconfig ]
```
eksctl utils write-kubeconfig --cluster fabulous-sheepdog-1748719678
```

### teardown the cluster
```
eksctl delete cluster fabulous-sheepdog-1748719678 --region us-east-1
```
