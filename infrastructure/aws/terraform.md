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

