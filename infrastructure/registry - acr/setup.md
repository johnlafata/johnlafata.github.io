# setup ACR registry
## install azure cli
### reference:
https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-macos?view=azure-cli-latest

### instructions
```
brew install azure-cli
```
### login to azure
```
az login
```

az acr login --name jltestcr
az acr update -n jltestcr --admin-enabled true
