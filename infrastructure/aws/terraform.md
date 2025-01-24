## Automating AWS Organization and Subaccounts with Terraform

To automate the creation of an AWS Organization and subaccounts using Terraform, follow these steps:

1. **Install Terraform**: Ensure that Terraform is installed on your machine.
    - Install Terraform: https://learn.hashicorp.com/tutorials/terraform/install-cli

2. **Set Up AWS Provider**: Configure the AWS provider in your Terraform configuration file.
    ```hcl
    provider "aws" {
      region = "us-east-1"
    }
    ```

3. **Create AWS Organization**:
    ```hcl
    resource "aws_organizations_organization" "org" {
      feature_set = "ALL"
    }
    ```

4. **Create Organizational Units (OUs)**:
    ```hcl
    resource "aws_organizations_organizational_unit" "ou" {
      name      = "OU-Name"
      parent_id = aws_organizations_organization.org.roots[0].id
    }
    ```

5. **Create Subaccounts**:
    ```hcl
    resource "aws_organizations_account" "subaccount" {
      name      = "Subaccount-Name"
      email     = "email@example.com"
      parent_id = aws_organizations_organizational_unit.ou.id
    }
    ```

6. **Attach Policies**:
    ```hcl
    resource "aws_organizations_policy_attachment" "policy_attach" {
      policy_id = "p-12345678"
      target_id = aws_organizations_account.subaccount.id
    }
    ```

7. **Apply the Configuration**:
    - Initialize Terraform: `terraform init`
    - Plan the changes: `terraform plan`
    - Apply the changes: `terraform apply`

Note: Ensure that you have the necessary permissions to perform these actions and that you handle any errors or exceptions that may occur during the process.

## Automating AWS Organization and Subaccounts with with the AWS CLI 

/**
 * This script automates the creation of an AWS Organization and subaccounts.
 * 
 * Steps to automate the creation:
 * 1. **Set Up AWS CLI**: Ensure that the AWS CLI is installed and configured with the necessary permissions.
 *    - Install AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
 *    - Configure AWS CLI: `aws configure`
 * 
 * 2. **Create AWS Organization**:
 *    - Use the `create-organization` command to create a new organization.
 *    - Example: `aws organizations create-organization --feature-set ALL`
 * 
 * 3. **Create Organizational Units (OUs)**:
 *    - Use the `create-organizational-unit` command to create OUs within the organization.
 *    - Example: `aws organizations create-organizational-unit --parent-id <root-id> --name <OU-name>`
 * 
 * 4. **Create Subaccounts**:
 *    - Use the `create-account` command to create new accounts within the organization.
 *    - Example: `aws organizations create-account --email <email> --account-name <account-name>`
 * 
 * 5. **Attach Policies**:
 *    - Use the `attach-policy` command to attach policies to the organization, OUs, or accounts.
 *    - Example: `aws organizations attach-policy --target-id <target-id> --policy-id <policy-id>`
 * 
 * 6. **Verify Creation**:
 *    - Use the `list-accounts` and `list-organizational-units-for-parent` commands to verify the creation of accounts and OUs.
 *    - Example: `aws organizations list-accounts`
 * 
 * Note: Ensure that you have the necessary permissions to perform these actions and that you handle any errors or exceptions that may occur during the process.
 */

