### Tool to make sure no credentials are deployed to a git repo.

https://github.com/awslabs/git-secrets

#### installation on mac
```bash
brew install git-secrets
```

#### to ensure a git repository is scanned for secrets on each commit:

```bash
cd /path/to/my/repo
git secrets --install
git secrets --register-aws
```

#### to scan this repo
```bash
git secrets --scan
```

#### to setup the scan globally for all future repositories

[Advanced configuration](https://github.com/awslabs/git-secrets?tab=readme-ov-file#id10)


Add a configuration template if you want to add hooks to all repositories you initialize or clone in the future.
```bash
git secrets --register-aws --global
```

Add hooks to all your local repositories.
```bash
git secrets --install ~/.git-templates/git-secrets
git config --global init.templateDir ~/.git-templates/git-secrets
```

Add custom providers to scan for security credentials.
```bash
git secrets --add-provider -- cat /path/to/secret/file/patterns
```