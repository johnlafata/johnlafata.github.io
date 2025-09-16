# AWS amplify cli

AWS Amplify CLI is a unified toolchain that allows you to create AWS cloud services for your app. It simplifies the process of connecting your frontend to the cloud for various functionalities like authentication, storage, APIs, and more.

It is used in Identity management by creating IAM users with specific permissions policies, attaching policies directly, and setting up access keys for users. Additionally, it involves configuring AWS profiles locally using IAM Identity Center or IAM roles to manage access to AWS resources securely.

# Installation
https://docs.amplify.aws/gen1/javascript/start/getting-started/installation/#install-the-amplify-cli

```bash
curl -sL https://aws-amplify.github.io/amplify-cli/install | bash && $SHELL
```

# Usage
## Creating a User Pool

To create a user pool using AWS Amplify CLI, follow these steps:

1. **Initialize Amplify in your project**:
    ```sh
    amplify init
    ```

2. **Add authentication**:
    ```sh
    amplify add auth
    ```
    Follow the prompts to configure the authentication flow. Choose the default configuration or customize it as needed.

    response: 
    ```sh
    ⚠️ For new projects, we recommend starting with AWS Amplify Gen 2, our new code-first developer experience. Get started at https://docs.amplify.aws/react/start/quickstart/
    ✔ Do you want to continue with Amplify Gen 1? (y/N) · yes
    ✔ Why would you like to use Amplify Gen 1? · Prefer not to answer
    Note: It is recommended to run this command from the root of your app directory
    ? Enter a name for the project documentprocessor
    The following configuration will be applied:

    Project information
    | Name: documentprocessor
    | Environment: dev
    | Default editor: Visual Studio Code
    | App type: javascript
    | Javascript framework: none
    | Source Directory Path: src
    | Distribution Directory Path: dist
    | Build Command: npm run-script build
    | Start Command: npm run-script start

    ? Initialize the project with the above configuration? Yes
    Using default provider  awscloudformation
    ? Select the authentication method you want to use: AWS profile

    For more information on AWS Profiles, see:
    https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

    ? Please choose the profile you want to use default
    Adding backend environment dev to AWS Amplify app: d3izvwf1kcmhtj

    Deployment completed.
    Deploying root stack documentprocessor [ ==========------------------------------ ] 1/4
            amplify-documentprocessor-dev… AWS::CloudFormation::Stack     CREATE_IN_PROGRESS             Wed Feb 05 2025 11:26:21…     
            AuthRole                       AWS::IAM::Role                 CREATE_IN_PROGRESS             Wed Feb 05 2025 11:26:23…     
            DeploymentBucket               AWS::S3::Bucket                CREATE_COMPLETE                Wed Feb 05 2025 11:26:37…     
            UnauthRole                     AWS::IAM::Role                 CREATE_IN_PROGRESS             Wed Feb 05 2025 11:26:23…     

    ✔ Help improve Amplify CLI by sharing non-sensitive project configurations on failures (y/N) · no

        You can always opt-in by running "amplify configure --share-project-config-on"
    Deployment state saved successfully.
    ✔ Initialized provider successfully.
    ✅ Initialized your environment successfully.
    ✅ Your project has been successfully initialized and connected to the cloud!
    Some next steps:

    "amplify status" will show you what you've added already and if it's locally configured or deployed
    "amplify add <category>" will allow you to add features like user login or a backend API
    "amplify push" will build all your local backend resources and provision it in the cloud
    "amplify console" to open the Amplify Console and view your project status
    "amplify publish" will build all your local backend and frontend resources (if you have hosting category added) and provision it in the cloud


    Pro tip:
    Try "amplify add api" to create a backend API and then "amplify push" to deploy everything
    ```

3. **Push the changes to the cloud**:
    ```sh
    amplify push
    ```

## Creating Policies for AWS Fargate

To secure an AWS Fargate application, you need to create IAM policies and roles. Follow these steps:

1. **Create a policy**:
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "ecs:RunTask",
            "ecs:StopTask",
            "ecs:DescribeTasks",
            "ecs:ListTasks"
          ],
          "Resource": "*"
        }
      ]
    }
    ```

2. **Attach the policy to a role**:
    ```sh
    aws iam create-role --role-name FargateTaskExecutionRole --assume-role-policy-document file://trust-policy.json
    aws iam attach-role-policy --role-name FargateTaskExecutionRole --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
    ```

3. **Update your Fargate task definition to use the new role**:
    ```json
    {
      "executionRoleArn": "arn:aws:iam::123456789012:role/FargateTaskExecutionRole",
      ...
    }
    ```

By following these steps, you can create a user pool and secure your AWS Fargate application using AWS Amplify CLI and IAM policies.