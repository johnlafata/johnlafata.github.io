# Terminating Ingress TLS with HAProxy on vSphere Kubernetes Service

This configuration demonstrates how to set up TLS termination for Kubernetes Ingress resources using HAProxy on VMware vSphere Kubernetes Service (VKS).

## Prerequisites
- Running vSphere Kubernetes Service cluster
- kubectl configured to access the cluster
- Domain name with ability to configure DNS
- TLS certificate and private key for your domain

## Key Components
1. **Secret Resource**: Stores the TLS certificate and private key
2. **HAProxy ConfigMap**: Contains HAProxy-specific configurations
3. **Ingress Resource**: Defines routing rules and references the TLS secret
4. **Service**: Exposes the application internally

## Implementation Notes
- HAProxy handles TLS termination at the edge
- Traffic between HAProxy and backend services remains unencrypted inside the cluster
- Supports SNI (Server Name Indication) for hosting multiple TLS sites
- Certificate rotation requires updating the Kubernetes Secret

## Troubleshooting
- Verify certificate validity and secret creation
- Check HAProxy logs for TLS handshake errors
- Ensure DNS records point to the HAProxy ingress controller IP
- Validate that the secretName in Ingress matches the created TLS secret