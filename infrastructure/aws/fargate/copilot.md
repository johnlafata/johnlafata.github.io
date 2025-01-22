# aws copilot
## reference: 

https://aws.github.io/copilot-cli/docs/overview/

more reference: 

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/copilot-deploy.html

## installation

Homebrew: brew install aws/tap/copilot-cli

## docs

Docs: https://aws.github.io/copilot-cli/

## feedback

Feedback & Requests: https://github.com/aws/copilot-cli/issues/new


## integration with cognito

https://aws.github.io/copilot-cli/ja/blogs/release-v118/#pipeline_1 

## usage - deploy to fargate with copilot
```shell
copilot init
Note: It's best to run this command in the root of your Git repository.
Welcome to the Copilot CLI! We're going to walk you through some questions
to help you get set up with a containerized application on AWS. An application is a collection of
containerized services that operate together.

Note: Looks like you're creating an application using credentials set by environment variables.
Copilot will store your application metadata in this account.
We recommend using credentials from named profiles. To learn more:
https://aws.github.io/copilot-cli/docs/credentials/

Application name: test
Workload type: Load Balanced Web Service
Service name: test-service
Dockerfile: ./Dockerfile
Ok great, we'll set up a Load Balanced Web Service named test-service in application test.

✔ Proposing infrastructure changes for stack test-infrastructure-roles
- Creating the infrastructure for stack test-infrastructure-roles                               [create complete]  [41.5s]
  - A StackSet admin role assumed by CloudFormation to manage regional stacks                   [create complete]  [20.4s]
  - An IAM role assumed by the admin role to create ECR repositories, KMS keys, and S3 buckets  [create complete]  [17.5s]
✔ The directory copilot will hold service manifests for application test.

Note: Architecture type arm64 has been detected. We will set platform 'linux/x86_64' instead. If you'd rather build and run as architecture type arm64, please change the 'platform' field in your workload manifest to 'linux/arm64'.
✔ Wrote the manifest for service test-service at copilot/test-service/manifest.yml
Your manifest contains configurations like your container size and port.

- Update regional resources with stack set "test-infrastructure"  [succeeded]  [0.0s]
All right, you're all set for local development.
Deploy: Yes
Only found one option, defaulting to: Create a new environment
Environment name: qa
Environment qa does not yet exist in application test; initializing it.
✔ Wrote the manifest for environment qa at copilot/environments/qa/manifest.yml
- Update regional resources with stack set "test-infrastructure"  [succeeded]  [0.0s]
- Update regional resources with stack set "test-infrastructure"  [succeeded]           [39.9s]
  - Update resources in region "us-east-1"                        [create complete]     [38.3s]
    - KMS key to encrypt pipeline artifacts between stages        [create complete]     [15.6s]
    - ECR container image repository for "test-service"           [create complete]     [2.1s]
    - S3 Bucket to store local artifacts                          [create in progress]  [3.9s]
✔ Proposing infrastructure changes for the test-qa environment.
- Creating the infrastructure for the test-qa environment.  [create complete]  [45.3s]
  - An IAM Role for AWS CloudFormation to manage resources  [create complete]  [17.7s]
  - An IAM Role to describe resources in your environment   [create complete]  [18.6s]
✔ Provisioned bootstrap resources for environment qa in region us-east-1 under application test.
✔ Provisioned bootstrap resources for environment qa.
✘ get template version of environment qa: get metadata for stack test-qa: get template summary: AccessDenied: Roles may not be assumed by root accounts.
        status code: 403, request id: 5e934559-fa53-4f97-b454-1d573ec85c98
(venv) johnlafata@Lafata-MacBook-Pro flask % 
```


## shell to container
https://aws.amazon.com/blogs/containers/connecting-to-an-interactive-shell-on-your-containers-running-in-aws-fargate-using-aws-copilot/

```shell
copilot svc exec
```