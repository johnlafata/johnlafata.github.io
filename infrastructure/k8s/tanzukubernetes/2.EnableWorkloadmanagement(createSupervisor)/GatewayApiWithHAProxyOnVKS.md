# Using Gateway API with HAProxy on vSphere Kubernetes Services (TKGs)

This document demonstrates how to configure HTTP routing to a Python application using Gateway API with HAProxy on vSphere Kubernetes Services.

## Prerequisites

- vSphere Kubernetes Services (TKGs) cluster
- HAProxy Ingress Controller installed
- Gateway API CRDs installed

## 1. Install Gateway API CRDs

First, ensure the Gateway API CRDs are installed:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml
```

## 2. Deploy a Sample Python Application

Create a Deployment and Service for your Python application:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: python-app
    labels:
        app: python-app
spec:
    replicas: 2
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
                image: python:3.9-slim
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
    - port: 80
        targetPort: 8080
    type: ClusterIP
```

## 3. Deploy HAProxy as a Gateway

Create a GatewayClass for HAProxy:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
    name: haproxy-gateway-class
spec:
    controllerName: haproxy.org/gateway-controller
```

Create a Gateway resource:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
    name: haproxy-gateway
    namespace: default
spec:
    gatewayClassName: haproxy-gateway-class
    listeners:
    - name: http
        protocol: HTTP
        port: 80
        allowedRoutes:
            namespaces:
                from: Same
```

## 4. Create an HTTPRoute

Configure an HTTPRoute to route traffic to your Python application:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
    name: python-app-route
    namespace: default
spec:
    parentRefs:
    - name: haproxy-gateway
        kind: Gateway
        group: gateway.networking.k8s.io
    hostnames:
    - "python-app.example.com"
    rules:
    - matches:
        - path:
                type: PathPrefix
                value: /
        backendRefs:
        - name: python-app-service
            port: 80
```

## 5. Verify the Setup

Check that the Gateway and HTTPRoute resources are properly configured:

```bash
kubectl get gateway haproxy-gateway -o yaml
kubectl get httproute python-app-route -o yaml
```

Access your application via the configured hostname:

```bash
curl -H "Host: python-app.example.com" http://<LOAD_BALANCER_IP>
```

## Troubleshooting

If routes aren't working as expected:

1. Check HAProxy controller logs:
     ```bash
     kubectl logs -l app=haproxy-ingress-controller
     ```

2. Verify Gateway status:
     ```bash
     kubectl describe gateway haproxy-gateway
     ```

3. Inspect HTTPRoute status:
     ```bash
     kubectl describe httproute python-app-route
     ```