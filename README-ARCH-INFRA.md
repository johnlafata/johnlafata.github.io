# Application Architecture and Infrastructure Management

## Application Architecture
The following presents a typical GEN AI application Architecture.

![Typical Gen AI Application Architecture](images/knowledgeBase-application.png)

## Infrastructure
This section documents the infrastructure management

Infrastructure As Code model.  Using Terraform to manage infrastructure provisioned on AWS lambda, AWS API Gateway and AWS Fargate.


## Baseline Development Infrastructure
### Repo Security

This link presents my evaluation of github hooks for [secret scanning](./doc/security/REPO-SECURITY-README.md). I'm going to use this as a starting point for protecting myself from accidentally deploying secrets or tokens to my repos.

### Integrate with a secrets manager to make things work
While working on my laptop, I currently am using environment variables stored on my local desktop to specify secrets, in time I will incorporate a secrets manager.  

### Identity management
When I deploy to the cloud I'd like to ensure that I have a good identity management strategy.  

I'm going to start with AWS Cognito, but I'm also going to look at Okta and Auth0.  



