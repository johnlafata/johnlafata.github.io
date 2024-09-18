https://github.com/kubernetes-sigs/kind

# on Mac
```bash
brew install kind
kind create cluster
kind delete cluster

kind get clusters
```

# on Linux
```bash
$ ssh ubuntu@192.168.86.23
## how to install??? 
```bash
brew install kind` again?
```

# create cluster 
```bash
$ kind get clusters
No kind clusters found.

$ kind create cluster
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.17.0) 🖼
 ✓ Preparing nodes 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Have a nice day! 👋

$ kind get kubeconfig >~/.kube/config
Or
$ kind get kubeconfig >>~/.kube/config
$ k config use-context kind-kind
```