I want to be able to deploy code on the cloud without concerning myself with acquiring the infrastructure every time I deploy.  For that reason, I am leaning toward serverless technologies.  Serverless technologies also should also allow me to scale my application to reduce worries about the underlying infrastructure cost.  

I'm going to start with AWS Lambda, but I'm also going to look at AWS Fargate which should be better for some applications.   For AI applications, I will introduce AWS Bedrock.

I want to implement an Infrastructure as Code model with infrastructure deployed via GITOps.

To start out, I'm building out a control plane on a minikube cluster to bootstrap a more robust dev ops process later.
[Here's my setup for Crossplane on minikube](./doc/devops/DEVOPS_CROSSPLANE_CONTROL_PLANE.md)


