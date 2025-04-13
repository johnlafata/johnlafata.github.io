Principle of least privilege
You should grant only the permissions needed to accomplish the task

Root user
Create AWS account - only user who can destroy account
Secure it with MFA

Define granular permissions

IAM policies
IAM user groups
IAM users
IAM user access
	Access Key and secrets - rotate often automatically
	IAM roles automatically rotate keys by design

Some tools
IAM access analyzer 
- identifies resources with external access
- Validate IAM policies and 
- Generate IAM policies based on usage

IAM policy simulator
- Test new IAM policies before granting them to users, user groups and roles

IAM identify Center - support federated identity management like: 
- MS AD
- Okta?
- Oauth?
- LDAP?
- Jump cloud?

* Followup research following
Amazon Cognito - signup page ( login with Apple, Google, Amazon, Facebook ).  GitHub?

S3 managed keys
Amazon Macie


Network Access Control List (NACL) 
- provide stateless access control in VPC and subnets
    - Stateless means these apply to traffic both in subnets in the VPC and from outside
Security Groups 
- Best practices
- provide stateful access control
    - Stateful means these apply to traffic ONLY  from outside the VPC. If traffic is initiated from inside the subnet or security group it is allowed

managing Multiple accounts 
Best practices is to create multiple accounts
AWS organizations
- Can apply config rules
- Role up costs to individual account
- Service control policies can prevent actions
    - IAM policy evil twins - prevent policies
AWS control tower
- Automate account creation