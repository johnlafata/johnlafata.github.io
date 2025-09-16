## Pre-requisites:
* Kubernetes cluster up and running (e.g., TKG, EKS, etc.)
* kubectl access with admin privileges
* HAProxy installed and configured on a VM 

## Example: HAProxy Configuration for Kubernetes Ingress

Below is a sample ingress deployment YAML for an application with ClusterIP service:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
    name: sample-ingress
    namespace: default
    annotations:
        # HAProxy specific annotations
        kubernetes.io/ingress.class: "haproxy"
        ingress.kubernetes.io/ssl-redirect: "false"
spec:
    rules:
    - host: myapp.example.com
        http:
            paths:
            - path: /
                pathType: Prefix
                backend:
                    service:
                        name: myapp-service
                        port:
                            number: 80
```

And here's the corresponding ClusterIP service:

```yaml
apiVersion: v1
kind: Service
metadata:
    name: myapp-service
    namespace: default
spec:
    type: ClusterIP
    selector:
        app: myapp
    ports:
    - port: 80
        targetPort: 8080
```

### HAProxy Configuration

Your HAProxy configuration should include:

```
frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    server k8s-api <KUBERNETES_API_IP>:6443 ssl verify none
    server-template k8s-node 3 <KUBERNETES_NODE_IP_PREFIX>:30000 check
```

Replace `<KUBERNETES_API_IP>` and `<KUBERNETES_NODE_IP_PREFIX>` with your actual Kubernetes cluster IP addresses.