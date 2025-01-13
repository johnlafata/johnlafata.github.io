# Infrastructure
This page documents the infrastructure management tasks.

I think the best practice to follow is to leverage an Infrastructure As Code model.  This will allow me to manage my infrastructure in a repeatable and consistent way.  I'm going to use Terraform to manage my infrastructure.

## Baseline Development Infrastructure
### Repo Security

This link presents my evaluation of github hooks for [secret scanning](./doc/security/REPO-SECURITY-README.md). I'm going to use this as a starting point for protecting myself from accidentally deploying secrets or tokens to my repos.

### Integrate with a secrets manager to make things work
While working on my laptop, I currently am using environment variables stored on my local desktop to specify secrets, in time I will incorporate a secrets manager.  

### Identity management
When I deploy to the cloud I'd like to ensure that I have a good identity management strategy.  

I'm going to start with AWS Cognito, but I'm also going to look at Okta and Auth0.  

# Cloud Infrastructure

## AWS

### Network

### Compute

### Storage

## Azure

### Network

### Compute

### Storage

