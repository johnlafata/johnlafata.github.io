One of the first things I want do to is make sure I don't accidently commit any secrets to this repo, so I'm going to explore how to use git-secrets to prevent that.

https://github.com/awslabs/git-secrets

[See more of my exercize with git-secrets here.](tools/code/gitgSecrets.md)

So git- secrets his is great, it scans and finds AWS related secrets by default, but I really want a more comprehensive scan, which would require me to add more patterns to scan for.  I'll be looking for common credential patterns to add to sthis

I'm also looking at this to see if this is an even better solution.

https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection

Turns out that secret scanning and push protection are enabled by default.  

![pushProtection](images/pushProtectionAndSecretScanning.png)