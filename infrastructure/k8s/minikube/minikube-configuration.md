# configure minikube

## Reference:
https://darkowlzz.github.io/post/minikube-config/


# Minikube Configuration
`vi ~/.minikube/config/config.json`

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

`minikube config view`
