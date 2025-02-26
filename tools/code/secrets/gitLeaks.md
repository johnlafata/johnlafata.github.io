
[Gitleaks](https://www.jit.io/blog/the-developers-guide-to-using-gitleaks-to-detect-hardcoded-secrets): scans your code for hardcoded secrets, such as passwords and API keys, that could have otherwise been overlooked. This is easy to do in your SCM or IDE to catch hardcoded secrets before production.

### to install
```bash
brew install gitleaks
```

### to execute a scan
```bash
gitleaks dir
```
### to see location of the leaks 
```bash
gitleaks dir -v
```

### to redact password in logs and sysout.
```bash
gitleaks dir -v --redact=95
```

### add a .gitleaksignore file to accommodate false positives or files that are with the .gitignore file and wouldn't be committed.

Refer to these instructions for adding a .gitleaksignore entry: 
https://github.com/gitleaks/gitleaks/tree/master#gitleaksignore 

here's an example specifying the name of the .gitleaksignore file (though this name used below is the default name and it would not be necessary to specify it in this case):

```
gitleaks dir -v -i .gitleaksignore
```