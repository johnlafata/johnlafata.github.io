# SAML

## reference material:
https://www.microfocus.com/documentation/single-sign-on/help/single-sign-on-admin/saml-overview.html?view=print 

dev01@azureisynergetics.onmicrosoft.com
Duqo8174

userB@azureisynergetics.onmicrosoft.com
Dapa8192


# SAML metadata:
For SAML metadata, you'll need the Assertion Consumer Service (ACS) URL, which is where the Identity Provider (IdP) redirects the user after authentication, along with the Entity ID (a URI identifying the Service Provider (SP)), and potentially other information like Single Logout Service (SLO) URL and public keys. 

Here's a more detailed breakdown:

**SAML Metadata:**
This is an XML document containing crucial information for SAML-based single sign-on (SSO) interactions between an IdP and an SP. 

**ACS URL (Assertion Consumer Service URL):**
This is the URL where the IdP sends the user's authentication response (assertion) after successful authentication. 

**Entity ID:**
This is a unique identifier (a URI) for the SP, used to identify the issuer of SAML requests, responses, or assertions. 

**Single Logout Service (SLO) URL:**
This URL is used to initiate a logout of the user's session across the SP and IdP. 

**Public Keys:**
These are used to verify the authenticity and integrity of SAML messages. 

**Other Metadata Elements:**
The metadata might also include information about supported bindings (like HTTP Redirect or HTTP POST), and other relevant URLs or configurations. 

In essence, the SAML metadata allows the IdP and SP to communicate and verify each other's identities and endpoints, ensuring a secure and reliable SSO experience. 


# Does an application need special configuration to support SAML?

Yes, applications need specific configuration to accept SAML tokens, which often involves setting up trust with an Identity Provider (IdP) and configuring the application to understand and process SAML assertions. 

Here's a more detailed explanation:
SAML and SSO:
SAML (Security Assertion Markup Language) is a standard for exchanging authentication and authorization data, enabling single sign-on (SSO). 

**Application Configuration:**
To enable SAML SSO, an application needs to be configured to:

* Trust an IdP: The application must be configured to trust a specific IdP (e.g., Microsoft Entra ID, Okta, etc.) that will issue SAML tokens. 

* Process SAML Assertions: The application needs to be able to receive, validate, and extract information from SAML assertions (the tokens). 
Handle Metadata: Some applications can use metadata files (XML) provided by the IdP to simplify the configuration process. 

*Configuration Methods:*
- Manual Configuration: Each application might have specific configuration options and instructions. 
- Metadata Configuration: Uploading a metadata file from the IdP to the application can simplify the configuration process. 

*SAML Configuration in the SP:*
The SP (Service Provider, or the application) needs to be able to receive the IdP's metadata file or have the ability to configure key SAML parameters like the IdP redirect URL, IssuerID, and IdP Logout URL. 
The SP must also allow the IdP's public certificate to be uploaded or saved. 

*Example:*
For example, in Microsoft Entra ID, you can configure an enterprise application to use SAML SSO by adding the application to the Microsoft Entra ID portal and following the configuration steps provided by the application. 
You can then configure the application to use SAML SSO by providing the application with the necessary information, such as the Login URL, Microsoft Entra Identifier, and Logout URL. 

*Custom Claims:*
Applications with more complex requirements, such as custom claims, might require extra configuration in the IdP and/or the application. 

## python service provider using saml
https://github.com/IdentityPython/pysaml2/blob/master/docs/examples/sp.rst 

## spring security service provider using saml
https://github.com/code-tinkering/spring-security-saml2-service-provider-example


## 

To connect an app to SAML Single Sign-On (SSO) with existing infrastructure, you'll need to add the app to your identity provider (IdP) and configure SAML SSO, including setting up the app's metadata and user access, then test the connection. 
Here's a more detailed breakdown of the process:

1. Identify Your Identity Provider (IdP) and Application:
Determine your IdP: Are you using Microsoft Entra ID (formerly Azure AD), Okta, Ping Identity, or another IdP?
Identify the application: What application are you trying to connect to your IdP? 

2. Add the Application to Your IdP:
Log in to your IdP admin console.
Navigate to the "Applications" or "Enterprise Applications" section.
Add a new application: You might need to search for the application in the IdP's gallery or choose "Integrate any other application" if it's not in the gallery.
Enter the application's name and other relevant details. 

3. Configure SAML SSO for the Application:
Navigate to the application's Single Sign-On settings. 
Select "SAML" as the single sign-on method. 

Configure the SAML settings:
Identifier (Entity ID): This is a unique identifier for your application. 
Reply URL (Assertion Consumer Service URL): This is the URL where the IdP will send the user's SAML assertion. 

Sign-on URL: This is the URL where users will be redirected to log in. 
Other settings: Depending on your IdP and application, you might need to configure other settings, such as user attributes, signing certificates, and single logout (SLO) settings. 
Download the IdP's metadata: You'll likely need to download the IdP's SAML metadata (an XML file) to configure the application. 

Upload the application's metadata to the IdP: Some IdPs require you to upload the application's metadata (an XML file) to configure the application. 
Configure the application's metadata: Some applications require you to configure the application's metadata, such as the IdP's URL and signing certificate. 

4. Test the Connection:
Assign users to the application.
Test the SAML SSO flow: Try logging in to the application using the IdP's credentials.
Verify that users can access the application without re-authenticating. 
Specific IdP Examples (Microsoft Entra ID):
Log in to the Microsoft Entra admin center.
Browse to "Identity" > "Applications" > "Enterprise applications" > "All applications".
Select the application from the search results.
In the "Manage" section, select "Single sign-on" and then "SAML".
Configure the SAML settings as described above. 
Key Considerations:
Security: Ensure that your SAML configuration is secure and that you are using strong encryption and signing certificates. 
User Experience: Make sure that the SAML SSO flow is seamless and easy for users. 
Troubleshooting: If you encounter any issues, consult your IdP's documentation or contact their support team. 


## deploy with Amplify and AWS CDK

https://github.com/aws-samples/amazon-cognito-saml-idp

## saml support with amazon cognito
https://aws.amazon.com/blogs/mobile/announcing-saml-support-for-amazon-cognito/