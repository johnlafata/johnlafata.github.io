# Certificate Authentication for Kubernetes User Access

This document outlines the steps to create a user authenticated with certificate authentication and grant them access to the `foo` namespace.

## 1. Generate a Private Key

First, generate a private key for the user:

```bash
openssl genrsa -out user.key 4096
```

## 2. Create a Certificate Signing Request (CSR)

Create a CSR for the user with their details:

```bash
openssl req -new -key user.key -out user.csr -subj "/CN=user/O=group"
```

Replace `user` with the username and `group` with the group name you want to assign.

## 3. Sign the CSR with the Kubernetes CA

You need to sign the CSR using the Kubernetes CA certificates:

```bash
openssl x509 -req -in user.csr -CA /path/to/kubernetes/ca.crt -CAkey /path/to/kubernetes/ca.key \
    -CAcreateserial -out user.crt -days 365
```

> Note: The CA files are typically located in `/etc/kubernetes/pki/` on the master node.

## 4. Create a Role or ClusterRole

Create a Role that provides the necessary permissions in the `foo` namespace:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
    namespace: foo
    name: foo-access
rules:
- apiGroups: [""]
    resources: ["pods", "services", "configmaps", "secrets"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

## 5. Create a RoleBinding

Bind the Role to the user:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
    name: foo-access-binding
    namespace: foo
subjects:
- kind: User
    name: user  # Must match the CN in the certificate
    apiGroup: rbac.authorization.k8s.io
roleRef:
    kind: Role
    name: foo-access
    apiGroup: rbac.authorization.k8s.io
```

## 6. Configure kubectl for the User

Create a new context for the user:

```bash
kubectl config set-credentials user --client-certificate=/path/to/user.crt --client-key=/path/to/user.key
kubectl config set-context user-context --cluster=your-cluster-name --namespace=foo --user=user
kubectl config use-context user-context
```

## 7. Verify Access

Verify that the user has the correct access:

```bash
kubectl get pods -n foo
```

## Troubleshooting

- Ensure all certificate paths are correct
- Verify that the CN in the certificate matches the user name in the RoleBinding
- Check if the namespace `foo` exists
- Verify the Kubernetes CA files are accessible