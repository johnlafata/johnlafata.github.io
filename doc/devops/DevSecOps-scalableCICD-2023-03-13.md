# Enterprise Infrastructure as a Service project

## Introduction

An assumption that users of an enterprise application deployment tool are developers who want to deploy their applications to the cloud. The system is designed to be self-service, allowing developers to deploy their applications to the cloud without needing to interact with the operations team.  

The system is required to be flexible, allowing users to deploy their applications to a variety of cloud platforms, including AWS, Azure, and Google Cloud. The system is also designed to be secure, with built-in security features to protect user data and applications.

Deployment options initially considered are Kubernetes on premises, on AWS and on Azure.  
Users can also request deployment on AWS Fargate.   AWS Fargate deployment leverages Amazon Copilot and acquires and configures the infrastructure on demand.   Deployment to Kubenetes environments expects that the necessary supporting infrastructure is already in place.

* User adds requests to the configuration management database
* User Specifies whether they want capacity or consumption based resources (leveraging * cloud platforms on demand)
* If the user is requesting compute capacity, IaaC tools using vRealize acquire resources and point the user toward them
* If the user requested a consumption based deployment, the user specifies the github repository for the project they want to deploy
    * User specifies the target environment for the project: possible choices on prem k8s, AWS k8s or ECS, Azure
    * Specify if the project is ephemeral or can use lower priority resources? 
    * The user specifies the source code repository for the project
    * The repository  is scanned for vulnerabilities using a scanning tool
    * Some deployment options such as AWS Copilot and Tanzu Build Service automate the build process from the source code repository, others require the user to specify a container image
        * If necessary for the deployment option, a container image is built using any of the following
    * When appropriate, the container image should also be scanned.
    * Any Vulnerabilities detected in the scan must be addressed.

## scanning the source code and dependencies
The container is scanned for vulnerabilities using a scanning tool, possibly running in a Tekton pipeline as part of the CI process.

Example scanning tools frequently encounter: Snyk, Checkmarx, SonarQube, GitLab, Black Duck, Sonatype, JFrog

Here's an example of scanning by Snyk in a Tekton pipeline

### Scanning with Snyk in Tekton

Create a `scan-task.yaml`:
```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
    name: snyk-scan
spec:
    params:
        - name: SNYK_TOKEN
            description: Snyk API token
        - name: REPOSITORY_URL
            description: GitHub repository URL
    steps:
        - name: scan
            image: snyk/snyk:linux
            env:
                - name: SNYK_TOKEN
                    value: $(params.SNYK_TOKEN)
            script: |
                git clone $(params.REPOSITORY_URL) .
                snyk test --all-projects
                snyk container test
```

Create a `pipeline.yaml`:
```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
    name: security-scan
spec:
    params:
        - name: repo-url
        - name: snyk-token
    tasks:
        - name: run-scan
            taskRef:
                name: snyk-scan
            params:
                - name: REPOSITORY_URL
                    value: $(params.repo-url)
                - name: SNYK_TOKEN
                    value: $(params.snyk-token)
```

Key features:
- Scans source code and dependencies
- Detects container vulnerabilities
- Generates detailed reports
- Integrates with CI/CD workflows

## building a container image
There are lots of tools for building a container image, here are a few of them:

### build a container image using github actions
Specify a `Dockerfile` in your repository and create a workflow:
```yaml
name: Build Docker Image
on: [push]
jobs:
    build:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v4
            - name: Build and push
                uses: docker/build-push-action@v5
                with:
                    context: .
                    push: false
                    tags: myapp:latest
```
This workflow builds a Docker image on every push. For more complex scenarios:
- Use `docker/login-action` to push to registries
- Add build args with `build-args`
- Enable layer caching with `cache-from`/`cache-to`

### build a container image using Jenkins
Create a `Jenkinsfile` in your repository:
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("myapp:${env.BUILD_ID}")
                }
            }
        }
    }
}
```
For enhanced builds:
- Use `docker.withRegistry()` to push to registries
- Add build parameters with `params`
- Implement multi-stage builds
- Add vulnerability scanning with plugins

### Building Container Images with Tanzu Build Service (TBS)
Tanzu Build Service (TBS) automates container builds using Cloud Native Buildpacks. Here's how to use it:

```yaml
# Create an image configuration
apiVersion: kpack.io/v1alpha2
kind: Image
metadata:
    name: my-app
    namespace: default
spec:
    tag: registry.example.com/my-app
    serviceAccountName: registry-credentials
    builder:
        kind: ClusterBuilder
        name: default
    source:
        git:
            url: https://github.com/myorg/myapp
            revision: main
```

Key features:
- Auto-detects language and dependencies
- Rebuilds automatically when base images change
- Handles multi-stage builds
- Integrates with common registries
- Supports custom buildpacks and builders

For enhanced security:
- Enable vulnerability scanning with built-in Tanzu components
- Configure resource limits
- Use private registry authentication

### build a container image using Azure DevOps
Create an `azure-pipelines.yml` in your repository:
```yaml
trigger:
- main

pool:
    vmImage: 'ubuntu-latest'

steps:
- task: Docker@2
    inputs:
        containerRegistry: 'myregistry'
        repository: 'myapp'
        command: 'buildAndPush'
        Dockerfile: '**/Dockerfile'
        tags: |
            $(Build.BuildId)
            latest
```

Key features:
- Supports multi-stage builds
- Integrates with Azure Container Registry
- Built-in vulnerability scanning
- Caching for faster builds
- RBAC controls for registry access

### build a container image using GitLab
Create a `.gitlab-ci.yml` in your repository:
```yaml
image: docker:latest

services:
    - docker:dind

variables:
    DOCKER_TLS_CERTDIR: "/certs"

build:
    stage: build
    script:
        - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
        - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

Key features:
- Built-in container registry
- Auto DevOps pipeline support
- Integrated security scanning
- Cache sharing between jobs
- Registry vulnerability scanning


## Deployment
After the scan and build phase, a deployment plan is created dependant on the target environment requested by the user:  possible choices on prem k8s, AWS k8s or ECS, Azure.

For any Kubernetes deployment:
- A deployment file and service is created
- Where possible a knative (scale to 0 deployment might be used)
- If this is an ephemeral deployment or can use lower priority resources, the deployment is configured with priority appropriate for the purpose
- The deployment file and service written to a source code repository monitored by flux
- the K8s reconcilation loop in flux updates the cluster with the new deployment

on AWS fargate
- AWS Copilot folders are created in the source code repository
- An AWS CodePipeline runs to create the necessary infrastructure resources and deploys the application

