I want to be able to deploy code on the cloud without concerning myself with acquiring the infrastructure every time I deploy.  For that reason, I am leaning toward serverless technologies.  Serverless technologies also should also allow me to scale my application to reduce worries about the underlying infrastructure cost.  

I'm going to start with AWS Lambda, but I'm also going to look at AWS Bedrock, which is a new service that allows you to deploy multimodal vision and lightweight models.  

I want to implement an Infrastructure as Code model, deployed via GITOps.

To start out, I'm a control plane on a minikube cluster to bootstrap a more robust dev ops process
[Here's my setup for Crossplane on minikube](./docs/devops/DEVOPS_CROSSPLANE_CONTROL_PLANE.md)


