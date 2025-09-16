# Using Gateway API to Configure HTTPRoute to a Python Application on Minikube

This guide explains how to use Gateway API to route HTTP traffic to a Python application running in a Docker container on Minikube.

## Prerequisites

- Minikube installed and running
- kubectl configured to work with your Minikube cluster
- Docker installed

## Step 1: Start Minikube

```bash
minikube start
```

## Step 2: Install Gateway API CRDs

```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v0.8.0/standard-install.yaml
```

## Step 3: Install HAProxy as the Gateway Controller

```bash
helm repo add haproxytech https://haproxytech.github.io/helm-charts
helm repo update
helm install haproxy-gateway haproxytech/kubernetes-ingress \
    --set controller.ingressClass=haproxy \
    --set controller.service.type=NodePort
```

## Step 4: Create a Sample Python Application

Create a deployment and service for a simple Python application:

```yaml
# python-app.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: python-app
    labels:
        app: python-app
spec:
    replicas: 1
    selector:
        matchLabels:
            app: python-app
    template:
        metadata:
            labels:
                app: python-app
        spec:
            containers:
            - name: python-app
                image: python:3.9-alpine
                command: ["python", "-m", "http.server", "8080"]
                ports:
                - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
    name: python-app-service
spec:
    selector:
        app: python-app
    ports:
    - port: 8080
        targetPort: 8080
    type: ClusterIP
```

Apply the configuration:

```bash
kubectl apply -f python-app.yaml
```

## Step 5: Create a Gateway Resource

```yaml
# gateway.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
    name: haproxy-gateway
spec:
    gatewayClassName: haproxy
    listeners:
    - name: http
        protocol: HTTP
        port: 80
        allowedRoutes:
            namespaces:
                from: Same
```

Apply the gateway configuration:

```bash
kubectl apply -f gateway.yaml
```

## Step 6: Create an HTTPRoute Resource

```yaml
# http-route.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
    name: python-app-route
spec:
    parentRefs:
    - name: haproxy-gateway
    hostnames:
    - "python.app.local"
    rules:
    - matches:
        - path:
                type: PathPrefix
                value: /
        backendRefs:
        - name: python-app-service
            port: 8080
```

Apply the HTTPRoute:

```bash
kubectl apply -f http-route.yaml
```

## Step 7: Access the Application

Get the URL to access the application:

```bash
minikube service haproxy-gateway-kubernetes-ingress --url
```

Add an entry to your local /etc/hosts file:

```
<minikube_ip> python.app.local
```

Now you can access the application at http://python.app.local

## Verification

Check if everything is working correctly:

```bash
kubectl get gateway haproxy-gateway -o yaml
kubectl get httproute python-app-route -o yaml
kubectl get pods
kubectl logs -l app=python-app
```

## Troubleshooting

If you encounter issues:

1. Check if the Gateway is in a ready state
2. Verify the HTTPRoute status
3. Look at the HAProxy controller logs:
     ```bash
     kubectl logs -n default -l app.kubernetes.io/name=kubernetes-ingress
     ```
4. Ensure your /etc/hosts file is correctly configured