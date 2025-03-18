configure minikube
Reference:
https://darkowlzz.github.io/post/minikube-config/

vi ~/.minikube/config/config.json

```
{
    "ingress": true,
    "memory": 8192,
    "cpus": 4
    "metrics-server": true
}
```

or at runtime

`minikube start --memory 8192`

verify

`minikube config view vm-driver`
