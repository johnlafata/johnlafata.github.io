# Setting up OpenID Connect (OIDC) as an External Identity Provider for Kubernetes

This guide explains how to configure Kubernetes to use OpenID Connect (OIDC) for authentication, allowing external identity management.

## Prerequisites
- A running Kubernetes cluster
- Access to modify kube-apiserver configuration
- An OIDC provider (e.g., Keycloak, Auth0, Okta, Azure AD, etc.)

## Configuration Steps

### 1. Set up your OIDC Provider
- Create a client application in your OIDC provider
- Configure redirect URLs
- Obtain client ID, client secret, and issuer URL

### 2. Configure the Kubernetes API Server
Update the kube-apiserver flags with OIDC-specific parameters:
- `--oidc-issuer-url`: The URL of the OIDC provider (must be HTTPS)
- `--oidc-client-id`: Client ID for the OIDC provider
- `--oidc-username-claim`: Claim to use as the username (typically 'sub' or 'email')
- `--oidc-groups-claim`: Claim to use for user groups (optional)
- `--oidc-ca-file`: CA certificate for the OIDC provider's certificate (if not publicly trusted)

### 3. Configure kubectl for OIDC Authentication
Set up kubectl to use the OIDC authentication plugin:

```bash
# Install kubectl plugin for OIDC authentication
brew install kubectl-oidc-login   # macOS with Homebrew
# OR
go install github.com/int128/kubelogin@latest   # Using Go

# Configure kubectl to use
# Configuring kubectl to use OIDC

This guide demonstrates how to configure kubectl to use OpenID Connect (OIDC) for authentication to Kubernetes clusters.

## Prerequisites

- kubectl installed
- Access to an OIDC provider (like Google, Azure AD, Okta, etc.)
- A Kubernetes cluster configured with OIDC authentication

## Configuration Steps

1. Add the OIDC credentials to your kubectl config file using the following parameters:
    - `--client-id`: The OAuth2 client ID
    - `--client-secret`: The OAuth2 client secret
    - `--issuer-url`: The OIDC issuer URL
    - `--id-token`: Your ID token (if using directly)
    - `--refresh-token`: Your refresh token for getting new ID tokens

2. Set the appropriate user configuration in your kubeconfig with authentication details.

3. Configure kubectl to use this user when connecting to your cluster.

## Example Usage
