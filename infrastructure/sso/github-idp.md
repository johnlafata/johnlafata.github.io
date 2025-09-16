To integrate GitHub as an SSO provider with Amazon Cognito, there are key limitations and alternative approaches to consider:

## SAML Limitation with GitHub
GitHub **only provides SAML SSO** for Enterprise+ tier organizations[1][4]. For standard GitHub accounts or organizations, SAML integration with Cognito isn't feasible due to this restriction[1][4].

## Recommended Alternative: OpenID Connect via GitHub OAuth
AWS Cognito supports **OpenID Connect (OIDC)** integration, which works with GitHub's standard OAuth implementation[1]:

1. **Create GitHub OAuth App**
   - Go to GitHub Settings → Developer settings → OAuth Apps
   - Set callback URL to:
     ```
     https:///oauth2/idpresponse
     ```
   - Get `Client ID` and `Client Secret`[1]

2. **Configure Cognito Identity Provider**
   ```terraform
   resource "aws_cognito_identity_provider" "github" {
     user_pool_id  = aws_cognito_user_pool.main.id
     provider_name = "GitHub"
     provider_type = "OIDC"
     
     provider_details = {
       client_id        = "YOUR_GITHUB_CLIENT_ID"
       client_secret    = "YOUR_GITHUB_CLIENT_SECRET"
       authorize_scopes = "read:user,user:email"
       attributes_request_method = "GET"
       oidc_issuer      = "https://github.com"
       authorize_url    = "https://github.com/login/oauth/authorize"
       token_url        = "https://github.com/login/oauth/access_token"
       attributes_url   = "https://api.github.com/user"
     }
     
     attribute_mapping = {
       email    = "email"
       username = "sub"
     }
   }
   ```
   This maps GitHub OAuth attributes to Cognito user attributes[1][3]

3. **Configure App Client**
   - Enable GitHub provider in Cognito App Client settings
   - Set callback URLs to handle OAuth flow[1]

## Enterprise SAML Alternative (If Applicable)
For GitHub Enterprise accounts with SAML support:

1. Configure Cognito SAML IdP using these parameters:
   - **Entity ID**: `urn:amazon:cognito:sp:{user-pool-id}`[3]
   - **ACS URL**: `https:///saml2/idpresponse`[2]
   - **NameID Format**: Persistent[5]

2. Use Terraform module for SAML setup:
   ```terraform
   module "saml_cognito" {
     source = "trussworks/saml-cognito/aws"
     name   = "GitHubEnterpriseSAML"
     saml_metadata_file_content = file("github-saml-metadata.xml")
   }
   ```
   Requires SAML metadata from GitHub Enterprise admin[2][5]

The OpenID/OAuth method works for most use cases, while SAML requires GitHub Enterprise. Both methods enable GitHub-authenticated users to obtain Cognito JWTs for accessing AWS resources and applications[3][5].

Citations:
[1] https://blog.ducthinh.net/github-openid-idp-aws-cognito/
[2] https://github.com/trussworks/terraform-aws-saml-cognito
[3] https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp.html
[4] https://docs.github.com/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/about-authentication-with-saml-single-sign-on
[5] https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managing-saml-idp.html
[6] https://github.com/undergroundwires/AWS-in-bullet-points/blob/master/saa/2.2.%20Security%20-%20Identity%20federation%20(STS,%20SAML,%20Cognito,%20SSO,%20Directory%20Service).md
[7] https://stackoverflow.com/questions/76452744/how-can-i-add-github-as-an-identity-provider-for-aws-cognito-with-terraform
[8] https://www.getambassador.io/blog/integrate-single-sign-on-sso-aws-cognito-azure-ad
[9] https://www.miniorange.com/iam/integrations/github-single-sign-on-sso
[10] https://aws.amazon.com/blogs/security/use-saml-with-amazon-cognito-to-support-a-multi-tenant-application-with-a-single-user-pool/
[11] https://docs.aws.amazon.com/cognito/latest/developerguide/saml-identity-provider.html
[12] https://github.com/2ZGroupSolutionsArticles/Article_KZ001
[13] https://github.com/aws-samples/amazon-cognito-example-for-multi-tenant/blob/main/docs/GoogleInstructions.md
[14] https://stackoverflow.com/questions/78965526/how-to-set-up-amazon-cognito-as-the-sole-saml-identity-provider-idp-without-th
[15] https://stackoverflow.com/questions/68049739/how-can-provide-aws-cognito-as-saml-2-0-idp-for-sso
[16] https://aws.amazon.com/blogs/security/how-to-set-up-amazon-cognito-for-federated-authentication-using-azure-ad/

---
Answer from Perplexity: pplx.ai/share