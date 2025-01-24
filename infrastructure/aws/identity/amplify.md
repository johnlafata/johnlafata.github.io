# AWS amplify cli

AWS Amplify CLI is a unified toolchain that allows you to create AWS cloud services for your app. It simplifies the process of connecting your frontend to the cloud for various functionalities like authentication, storage, APIs, and more.

It is used in Identity management by creating IAM users with specific permissions policies, attaching policies directly, and setting up access keys for users. Additionally, it involves configuring AWS profiles locally using IAM Identity Center or IAM roles to manage access to AWS resources securely.

# Installation
https://docs.amplify.aws/gen1/javascript/start/getting-started/installation/#install-the-amplify-cli

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