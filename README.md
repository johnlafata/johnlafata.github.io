# Planting Roots

As a cloud architect, I'm passionate about building scalable and efficient systems that can adapt to changing business needs.

This repo is where I'll share my thoughts and experience as a cloud architect.   I'm gradually going to release projects, experiments, and learnings here.  

Some sample topics may include containerizing a web application, deploying a new application, migrating code to a cloud ready architecture, or automating infrastructure provisioning, this repo is where I'll document my experiences, successes, and failures along the way. 

---

One of the first things I want do to is make sure I don't accidently commit any secrets to this repo, so I'm going to explore how to use git-secrets to prevent that

https://github.com/awslabs/git-secrets

So this is great, it scans and finds AWS related secrets by default, but I really want a more comprehensive scan, which would require me to add more patterns to scan for.  I'll be looking for common credential patterns to add to sthis

I'm also looking at this to see if this is an even better solution.

https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection

Turns out that secret scanning and push protection are enabled by default.  

![pushProtection](images/pushProtectionAndSecretScanning.png)