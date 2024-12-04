# managing python environments with pyenv, like java's sdkman
# pyenv is a simple python version management tool
# reference: https://github.com/pyenv/pyenv

# setup:
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