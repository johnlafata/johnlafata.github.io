## install om on jumphost

### reference
references:
https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/tanzu-operations-manager/3-0/tanzu-ops-manager/install-cli.html#homebrew

https://github.com/pivotal-cf/om

## install om
brew tap pivotal-cf/om https://github.com/pivotal-cf/om
brew install om

## configure om
```
touch om-cli-env.yml
vi om-cli-env.yml
```
```
---
target: https://OPS-MANAGER-FQDN
username: OPS-MANAGER-USERNAME
password: OPS-MANAGER-PASSWORD
```

## test with self-signed cert
```
export OM_ENV=PATH-TO-WORKING-DIRECTORY/om-cli-env.yml
```
for exampple:
```
export OM_ENV=~/om-cli-env.yml
```
test
```
om --skip-ssl-validation --env=$OM_ENV products
```