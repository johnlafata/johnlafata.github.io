# ssh private key management

###  to remove the passphrase from an SSH private key:
```
openssl rsa -in ~/.ssh/id_rsa_github -out id_rsa_github
```

### also try
```
ssh-keygen -p -f /path/to/your/private/key
```