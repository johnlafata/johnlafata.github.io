### setup
`brew install awscli`

### verify
```
aws --version
```
### complete setup
### after installing awscli, configure it with identity information found in the AWS console, IAM Users, Security credentials
I have a shell script to set these environment variables.  it's in a private repository.  By centalizing all the references to environment variables to this repo, I can decide whether to keep them hardcoded in the scripts or to move them to a secrets manager.  I can also decide to use a different secrets manager or to use a different method to manage the secrets.
```bash
# to set the environment variables
source ~/personal-workspace/credential_repo/aws-credentials.sh
# to confirm
aws configure list
```
result
```bash
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key     ****************4LKA              env    
secret_key     ****************gjF0              env    
    region                us-east-1              env    ['AWS_REGION', 'AWS_DEFAULT_REGION']
```

without this script you can set the environment variables manually
```bash
aws configure
```
result
```bash 
AWS Access Key ID:  <your key>
AWS Secret Access Key: <your secret>
Default region:  <your default region>
Default output format: 
```

