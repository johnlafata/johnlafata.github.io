Crossplane is a Kubernetes add-on that allows you to manage cloud infrastructure using Kubernetes.  

I'm going to create a control plane on [minikube](../../infrastructure/k8s/minikube/gettingStarted-minikube.md) to start but migrate the control plane to a cloud provider when I am ready to scale it up.

I want to be able to create test accounts automatically for development and demo environments and destroy them when I'm done with them.   

Eventually, I may want to create a production account and manage it with similarly.


-----------  continue here ------------


I want to leverage service accounts that adhere to the principle or least privilege necessary to perform their function.  

I want to use a secrets manager to store the secrets necessary to access the services.

Create a admin profile.

Decide on a structure for service accounts.  Should I setup a unique service account for each applications or for each resources type or the combination of both?


# Some references for crossplane providers that might be useful 
### crossplane AWS provider
https://docs.crossplane.io/latest/getting-started/provider-aws/

# Crossplane AWS provider authentication library (manage resources on AWS)
https://github.com/crossplane-contrib/provider-aws/blob/master/AUTHENTICATION.md

# crossplane github provider
https://github.com/crossplane-contrib/provider-github [deprecated, use following]
https://github.com/crossplane-contrib/provider-upjet-github