# Crossplane 
When using Crossplane on AWS, the required IAM profile or role is typically referred to as an "IAM Role for Service Accounts" (IRSA), which allows Crossplane pods running on your EKS cluster to assume a specific AWS IAM role with the necessary permissions to manage your AWS resources within the defined scope; essentially granting Crossplane the ability to interact with AWS services on your behalf. 

To start I'm going to try to run cross plane from my desktop using minikube and eventually use that to bootstrap a cloud based kubernetes supply chain.
[create a minikube cluster](../../../../infrastructure/k8s/minikube/gettingStarted-minikube.md)

#### prerequisites

[helm](../helm/install-helm.md)

[aws cli](../aws-cli/install-aws-cli.md)

#### Create an aws organization
Create an org and create create sub-accounts within that org for development and testing.  Create a separate sub-account for production.  Use the organization to manage the accounts and the permissions for the accounts.

### aws crossplane blue prints
This is a great resource for getting started with crossplane on AWS.
https://github.com/awslabs/crossplane-on-eks

#### references:
Review the instructions to ensure they line up with this reference instead of the next one.
https://docs.crossplane.io/latest/getting-started/provider-aws/


#### installing cross plane
```bash
kubectl create ns crossplane
helm repo add crossplane-stable https://charts.crossplane.io/stable
helm repo update
helm install crossplane crossplane-stable/crossplane --namespace crossplane
```

### verify
```
kubectl api-resources | grep crossplane
```

### Create an AWS IAM Role and Policy
created file named `crossplane-aws-policy.json`

```
{
  "Version": "2012-10-17",
  "Statement": 
   [ 
      {
       "Effect": "Allow",
       "Action": [ 
           "ec2:*",
            "rds:*",
            "s3:*",
            "iam:*",
            "lambda:*"
        ],
        "Resource": "*"
      }
    ]
}
```

# Create the IAM policy:
```
aws iam create-policy --policy-name CrossplaneAWSProviderPolicy --policy-document file://crossplane-aws-policy.json
```

#### create a role for crossplane and attach the policy
```
aws iam create-role --role-name CrossplaneAWSProviderRole --assume-role-policy-document '{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Principal": {"Service": "eks.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
aws iam attach-role-policy --role-name CrossplaneAWSProviderRole --policy-arn arn:aws:iam::YOUR_ACCOUNT_ID:policy/CrossplaneAWSProviderPolicy
```

### 
[create an access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for the role and secret

#### create an access key for the kubernetes secret with the AWS credentials
```
aws iam create-access-key --user-name YOUR_IAM_USER
```
example
```
aws iam create-access-key --user-name jl-admin-user
```

### create a secret manifest `aws-creds-secret.yaml`

### encode the credentials 
```
echo -n '[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY' | base64
```

Replace `BASE64_ENCODED_AWS_CREDENTIALS` in `aws-creds-secret.yaml` with the encoded string and apply the manifest

``` 
kubectl apply -f aws-creds-secret.yaml
```

### configure the aws provider
```
kubectl apply -f - <<EOF
apiVersion: aws.crossplane.io/v1beta1
kind: ProviderConfig
metadata:
  name: default
spec:
  credentials:
    source: Secret
    secretRef:
      namespace: crossplane-system
      name: aws-creds
      key: creds
EOF
```
### verify
```
kubectl get providerconfig
```

### test that the provider works  - create an s3 bucket
```
kubectl apply -f test-crossplane-s3-bucket-creation.yaml
```

### verify the status of the operation
```
kubectl get bucket example-bucket -o yaml
```

### Verify that the bucket is created successfully in your AWS account.


### delete the s3 bucket - cleanup ( only created the bucket as a test )
kubectl delete bucket example-bucket
