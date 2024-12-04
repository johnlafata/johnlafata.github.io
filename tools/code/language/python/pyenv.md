# Installing and managing python environments with pyenv

### managing python environments with pyenv
As a java developer I've used SDKMan to manage java versions for application development.  I've found that pyenv is a similar tool for managing python versions.  I'm going to use pyenv to manage python versions for my python applications.

pyenv is a simple python version management tool

reference: https://github.com/pyenv/pyenv

### setup:
```
brew update
brew install pyenv
pyenv install 3.10
pyenv global 3.10.15
pyenv which python
pyenv exec python --version

alias python="pyenv exec python"
alias pip="pyenv exec pip"
```