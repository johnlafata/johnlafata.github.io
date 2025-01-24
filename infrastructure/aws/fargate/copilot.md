# Using  AWS Copilot to deploy to Fargate

### prerequisites
- ensure that you have an ECR registry in AWS
- AWS CLI installed
- Docker Desktop installed
- AWS copilot installed
- non root account AWS_ACCESS_KEY and AWS_ACCESS_KEY_SECRET in AWS Profile
  - instructions: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html 
  - for example: create an alternate IAM user via the console, 
```
export AWS_PROFILE=my-app
```
- OPENAI_API_KEY, ANTHROPIC_API_KEY, GROQ_API_KEY in .env file
- also in the .env file, set OLLAMA_INCLUDED=False [this code only supports Ollama from local workspace at present]


### Usage
These are the basic stages to fargate deployment with AWS copilot

This is a good reference: https://aosolorzano.medium.com/spring-boot-native-microservice-on-ecs-fargate-using-aws-copilot-cli-for-cross-account-deployment-73b1836f21f7

This one is one that incorporates cognito
https://aosolorzano.medium.com/implementing-a-multi-account-environment-with-aws-organizations-and-the-iam-identity-center-d1cdb40bdf4d

`copilot init` to create the app

`copilot svc init` to create the service

`copilot env init` to create the environment

`copilot app deploy` to deploy the app to the environment

You can pass the parameters in the command line if you want as follows, when prompted to create the environment, say no.

```
copilot init                                   \
  --app          planning                      \
  --name         planning                      \
  --type         'Load Balanced Web Service'   \
  --dockerfile   './Dockerfile'                \
  --port         7860                          \
  --tag          '1.0.0'
```

Response:
```
Note: It's best to run this command in the root of your Git repository.
Welcome to the Copilot CLI! We're going to walk you through some questions
to help you get set up with a containerized application on AWS. An application is a collection of
containerized services that operate together.

Ok great, we'll set up a Load Balanced Web Service named planning in application planning.

✔ Proposing infrastructure changes for stack planning-infrastructure-roles
- Creating the infrastructure for stack planning-infrastructure-roles                           [create complete]  [44.2s]
  - A StackSet admin role assumed by CloudFormation to manage regional stacks                   [create complete]  [19.4s]
  - An IAM role assumed by the admin role to create ECR repositories, KMS keys, and S3 buckets  [create complete]  [17.3s]
✔ The directory copilot will hold service manifests for application planning.

Note: Architecture type arm64 has been detected. We will set platform 'linux/x86_64' instead. If you'd rather build and run as architecture type arm64, please change the 'platform' field in your workload manifest to 'linux/arm64'.
✔ Wrote the manifest for service planning at copilot/planning/manifest.yml
Your manifest contains configurations like your container size and port.

- Update regional resources with stack set "planning-infrastructure"  [succeeded]  [0.0s]
All right, you're all set for local development.
Deploy: No

No problem, you can deploy your service later:
- Run `copilot env init` to create your environment.
- Run `copilot deploy` to deploy your service.
- Be a part of the Copilot ✨community✨!
  Ask or answer a question, submit a feature request...
  Visit 👉 https://aws.github.io/copilot-cli/community/get-involved/ to see how!
```


### create environment

Use the appropriate AWS Profile for your configuration in the following

```
copilot env init              \
  --app 'planning'            \
  --name 'qa'                  \
  --profile 'fargate-sandbox'         \
  --container-insights          \
  --default-config
```
Response:
```
✔ Wrote the manifest for environment qa at copilot/environments/qa/manifest.yml
- Update regional resources with stack set "planning-infrastructure"  [succeeded]  [0.0s]
- Update regional resources with stack set "planning-infrastructure"  [succeeded]           [39.0s]
  - Update resources in region "us-east-1"                            [create complete]     [40.6s]
    - KMS key to encrypt pipeline artifacts between stages            [create complete]     [19.4s]
    - ECR container image repository for "planning"                   [create complete]     [0.0s]
    - S3 Bucket to store local artifacts                              [create in progress]  [3.3s]
✔ Proposing infrastructure changes for the planning-qa environment.
- Creating the infrastructure for the planning-qa environment.  [create complete]  [43.0s]
  - An IAM Role for AWS CloudFormation to manage resources      [create complete]  [20.1s]
  - An IAM Role to describe resources in your environment       [create complete]  [19.5s]
✔ Provisioned bootstrap resources for environment qa in region us-east-1 under application planning.
Recommended follow-up actions:
  - Update your manifest copilot/environments/qa/manifest.yml to change the defaults.
  - Run `copilot env deploy --name qa` to deploy your environment.
```


## deploy the env, the --no-rollback is useful to help debug any problems if it fails, but it's optional

```
copilot env deploy      \
  --app planning        \
  --name qa              \
  --no-rollback
```
Response:
```
✔ Proposing infrastructure changes for the planning-qa environment.
- Creating the infrastructure for the planning-qa environment.                         [update complete]  [66.2s]
  - A CloudFormation nested stack for your additional AWS resources                    [create complete]  [14.8s]
  - An ECS cluster to group your services                                              [create complete]  [9.4s]
  - A security group to allow your containers to talk to each other                    [create complete]  [3.2s]
  - An Internet Gateway to connect to the public internet                              [create complete]  [16.4s]
  - A resource policy to allow AWS services to create log streams for your workloads.  [create complete]  [3.5s]
  - Private subnet 1 for resources with no internet access                             [create complete]  [0.0s]
  - Private subnet 2 for resources with no internet access                             [create complete]  [0.0s]
  - A custom route table that directs network traffic for the public subnets           [create complete]  [10.8s]
  - Public subnet 1 for resources that can access the internet                         [create complete]  [3.6s]
  - Public subnet 2 for resources that can access the internet                         [create complete]  [0.0s]
  - A private DNS namespace for discovering services within the environment            [create complete]  [45.4s]
  - A Virtual Private Cloud to control networking of your AWS resources                [create complete]  [12.7s]
✔ Successfully deployed environment qa                                
```

### deploy the app

```
copilot  deploy         \
  --app   planning      \
  --name  planning      \
  --env   qa            \
  --tag   '1.0.0'         
```
Response:
```
Checking for all required information. We may ask you some questions.
Login Succeeded
[+] Building 0.7s (15/15) FINISHED                                                                                          docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                        0.0s
 => => transferring dockerfile: 1.08kB                                                                                                      0.0s
 => [internal] load metadata for public.ecr.aws/docker/library/python:3.13.1-slim-bookworm                                                  0.5s
 => [internal] load .dockerignore                                                                                                           0.0s
 => => transferring context: 2B                                                                                                             0.0s
 => [ 1/10] FROM public.ecr.aws/docker/library/python:3.13.1-slim-bookworm@sha256:23a81be7b258c8f516f7a60e80943cace4350deb8204cf107c7993e3  0.0s
 => [internal] load build context                                                                                                           0.0s
 => => transferring context: 3.30kB                                                                                                         0.0s
 => CACHED [ 2/10] WORKDIR /app                                                                                                             0.0s
 => CACHED [ 3/10] RUN pip install -U gradio langchain langchain-ollama langchain-openai langchain-groq logging langchain-anthropic llama_  0.0s
 => CACHED [ 4/10] COPY account-planning.py ./app.py                                                                                        0.0s
 => [ 5/10] COPY chatagent_anthropic.py ./chatagent_anthropic.py                                                                            0.0s
 => [ 6/10] COPY chatagent_groq.py ./chatagent_groq.py                                                                                      0.0s
 => [ 7/10] COPY chatagent_ollama.py ./chatagent_ollama.py                                                                                  0.0s
 => [ 8/10] COPY chatagent_openai.py ./chatagent_openai.py                                                                                  0.0s
 => [ 9/10] COPY tool_llama_index_wikipedia.py ./tool_llama_index_wikipedia.py                                                              0.0s
 => [10/10] COPY .env ./.env                                                                                                                0.0s
 => exporting to image                                                                                                                      0.0s
 => => exporting layers                                                                                                                     0.0s
 => => writing image sha256:775a2c7f14dc2bb4b81f16bec0094fa273a8b8e43f547a661ca16e1b740ca8ae                                                0.0s
 => => naming to 375559983734.dkr.ecr.us-east-1.amazonaws.com/planning/planning:latest                                                      0.0s
 => => naming to 375559983734.dkr.ecr.us-east-1.amazonaws.com/planning/planning:1.0.0                                                       0.0s

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview 
The push refers to repository [375559983734.dkr.ecr.us-east-1.amazonaws.com/planning/planning]
b4777096c973: Pushed 
931c1b32b33e: Pushed 
dc3972d851fd: Pushed 
6c206769aa87: Pushed 
e838f04b94b7: Pushed 
0485aa33c3b7: Pushed 
f10453a4c9b1: Pushed 
48956586c284: Pushed 
6945eb363c02: Pushed 
955362541777: Pushed 
e47eada9597c: Pushed 
52fc15be27b4: Pushed 
f5fe472da253: Pushed 
latest: digest: sha256:9f7325dd3b2be8e12e2ae9ad3322faa9c316db61c720037b770d17fda1d1b475 size: 3028
The push refers to repository [375559983734.dkr.ecr.us-east-1.amazonaws.com/planning/planning]
b4777096c973: Layer already exists 
931c1b32b33e: Layer already exists 
dc3972d851fd: Layer already exists 
6c206769aa87: Layer already exists 
e838f04b94b7: Layer already exists 
0485aa33c3b7: Layer already exists 
f10453a4c9b1: Layer already exists 
48956586c284: Layer already exists 
6945eb363c02: Layer already exists 
955362541777: Layer already exists 
e47eada9597c: Layer already exists 
52fc15be27b4: Layer already exists 
f5fe472da253: Layer already exists 
1.0.0: digest: sha256:9f7325dd3b2be8e12e2ae9ad3322faa9c316db61c720037b770d17fda1d1b475 size: 3028
✔ Proposing infrastructure changes for stack planning-qa-planning
- Creating the infrastructure for stack planning-qa-planning                      [create complete]  [423.5s]
  - Service discovery for your services to communicate within the VPC             [create complete]  [0.0s]
  - Update your environment's shared resources                                    [update complete]  [208.0s]
    - A security group for your load balancer allowing HTTP traffic               [create complete]  [8.3s]
    - A CloudFormation nested stack for your additional AWS resources             [update complete]  [0.0s]
    - An Application Load Balancer to distribute public traffic to your services  [create complete]  [185.1s]
    - A load balancer listener to route HTTP traffic                              [create complete]  [3.7s]
  - An IAM role to update your environment stack                                  [create complete]  [17.6s]
  - An IAM Role for the Fargate agent to make AWS API calls on your behalf        [create complete]  [17.6s]
  - An HTTP listener rule for path `/` that forwards HTTP traffic to your tasks   [create complete]  [0.0s]
  - A custom resource assigning priority for HTTP listener rules                  [create complete]  [1.7s]
  - A CloudWatch log group to hold your service logs                              [create complete]  [8.2s]
  - An IAM Role to describe load balancer rules for assigning a priority          [create complete]  [17.6s]
  - An ECS service to run and maintain your tasks in the environment cluster      [create complete]  [165.8s]
    Deployments                                                                                      
               Revision  Rollout      Desired  Running  Failed  Pending                                       
      PRIMARY  1         [completed]  1        1        0       0                                             
  - A target group to connect the load balancer to your service on port 7860      [create complete]  [17.6s]
  - An ECS task definition to group your containers and run them on ECS           [create complete]  [3.4s]
  - An IAM role to control permissions for the containers in your tasks           [create complete]  [17.6s]
✔ Deployed service planning.
Recommended follow-up action:
  - Your service is accessible at http://planni-Publi-nOAWMxDz2Qta-770698395.us-east-1.elb.amazonaws.com over the internet.

```

### logs
``` 
copilot svc logs --follow
```

### teardown
```
copilot app delete --yes
```

# Create CI/CD pipeline in AWS CODEPIPELINE
```
copilot pipeline init
git add copilot
git commit -m "adds copilot"
copilot pipeline deploy
```
