### Tool to make sure no credentials are deployed to a git repo.

https://github.com/awslabs/git-secrets

#### installation on mac
brew install git-secrets

#### to ensure a git repository is scanned for secrets on each commit:

cd /path/to/my/repo
git secrets --install
git secrets --register-aws


#### to scan this repo
git secrets --scan