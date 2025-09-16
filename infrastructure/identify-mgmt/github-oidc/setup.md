# GitHub Oauth provider

# TODO modify this to reflect that github is an OAUTH provider and not an OIDC provider

## Setting up GitHub as an OpenID Connect (OIDC) Provider

To set up GitHub as an OpenID Connect (OIDC) provider, you'll first need to register an application on GitHub, then configure your target system (e.g., a cloud provider, an application server) to trust GitHub as an identity provider. This involves creating an application in GitHub, obtaining client credentials, and then configuring the trusting system with these credentials and other necessary information like callback URLs and trust policies. 

Here's a step-by-step guide:

1. Register an application on GitHub:
Log in to GitHub: Sign in as the user who has permission to create applications. 
Navigate to Developer Settings: Go to your profile, then click on "Settings", then "Developer settings", then "OAuth Apps". 

Register a new application: Click "Register a new application". 

Fill in the application details:

* App Name: Choose a descriptive name for your application. 
* Homepage URL: Provide a URL for your application's homepage. 
* Authorization callback URL: This is a crucial step. This URL is where GitHub will redirect users after they authenticate. It should be a URL that your target system (the one relying on GitHub as the identity provider) can receive and handle. 

reference for opsmgr setup: https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/tanzu-operations-manager/3-0/tanzu-ops-manager/login.html#oidc 

Create the application: Click "Register application". 
Obtain client credentials: After registration, you'll see a Client ID and Client Secret. These credentials are essential for configuring your target system to trust GitHub. 

client_id: Ov23li8hYkBWi0Ue6Sf8
client_secret: <redacted_fake_secret>

2. Configure your target system:
Select your system:

* from opsmgr install reference above

In Discovery URL, enter your OIDC service provider discovery URL.
https://opsmgr-dev.agi-explorer.com/.well-known/openid-configuration

or from github reference:  [ this generated an error: Oidc settings : Oidc discovery url URL contains invalid JSON ]
https://github.com/login/oauth/authorize

**trying this from stack-overflow**
but for some reason it's undocumented. Here it is:

https://github.com/login/oauth/.well-known/openid-configuration

using this I got an error instead of presenting a login page, "oops, something went awry"

perhaps it would be better to use okta or aws oidc, github is more of an oauth server and not a true oidc provider, maybe.

* from above
In Client ID, enter the client ID created in Step 1.
In Client Secret, enter the client secret created in Step 1.

In Scopes, enter the scopes to request from the OIDC provider, as a comma-separated list. You must include the following scopes.

The openid scope
A scope that allows access to the group claim
Standard email and profile scopes, if you plan to use the claims listed in the next step to populate common fields in UAA
Enter the claims used to populate the UAA user store with data from the OIDC provider.

Enter the External Groups Claim to populate associated groups for the user in UAA. Enter the OIDC provider’s token claim that contains the groups to which the user belongs. Only the provided OIDC Admin Group Name and the default group names of opsman.full_control, opsman.restricted_control, opsman.full_view and opsman.restricted_view are mapped to UAA groups.
(Optional) Enter the Username Claim to populate the username field in UAA. Tanzu Operations Manager uses this to show the current logged-in user.
In OIDC Admin Group Name, enter the OIDC provider group name that corresponds to users who receive admin access. Users in this OIDC group are granted the opsman.admin scope in UAA.






This could be an AWS IAM role, an Azure AD application, a Google Cloud Service Account, or any other system that supports OIDC and wants to use GitHub as a trust provider. 
Add a GitHub identity provider:

In AWS IAM: Go to the Identity Providers section and add a new provider, specifying the OIDC endpoint (usually https://token.actions.githubusercontent.com) and providing the thumbprint. 
In Azure: Register an application in Azure AD and configure it to trust GitHub. 
In Google Cloud: Configure the Identity Platform to trust GitHub as a provider. 
Define trust policy:
AWS IAM: You need to configure a trust policy for the IAM role, allowing the GitHub OIDC provider to assume the role. This policy specifies which GitHub repositories, branches, or environments can assume the role. 
Azure AD: You'll configure the application to trust GitHub, specifying which GitHub repositories or users can authenticate and access resources. 
Google Cloud: You'll configure the Service Account to trust GitHub, specifying which repositories or users can access resources. 
Use the client credentials:
Provide the Client ID and Client Secret obtained from GitHub to the target system. 
Optional: Add additional security measures:
Conditions: Use conditions in the trust policy to restrict access to specific GitHub repositories, branches, or environments, as mentioned in the trust policy step. 
Thumbprints: Add the thumbprint of the GitHub OIDC provider to the trust policy in AWS IAM. 
Test:
Verify that the target system can authenticate using GitHub credentials by attempting to access resources that the trust policy allows. 
3. Update your workflows (if applicable):
If you are using GitHub Actions, you'll need to update your workflows to use the OIDC token to authenticate with the target system. 
This usually involves adding the id-token: write permission to the workflow, and using an action (e.g., the aws-actions/configure-aws-credentials action for AWS) to exchange the OIDC token for a short-lived AWS access token. 
In essence, you're creating a bridge between GitHub and your target system, allowing users to authenticate with their GitHub credentials and access resources in that system securely. 