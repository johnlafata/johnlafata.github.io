### install helm
```bash
brew install kubernetes-helm
```

#### response
```bash
brew install kubernetes-helm
==> Auto-updating Homebrew...
Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Auto-updated Homebrew!
Updated 4 taps (hashicorp/tap, moderneinc/moderne, homebrew/core and homebrew/cask).
==> New Formulae
ampl-asl

You have 23 outdated formulae installed.

Warning: Formula kubernetes-helm was renamed to helm.
==> Downloading https://ghcr.io/v2/homebrew/core/helm/manifests/3.16.3
######################################################################################################################## 100.0%
==> Fetching helm
==> Downloading https://ghcr.io/v2/homebrew/core/helm/blobs/sha256:b91608810e5b6a549a48f4cb1752600fc0ed5ccd7baf135a0bcae9c0cbce
######################################################################################################################## 100.0%
==> Pouring helm--3.16.3.arm64_sonoma.bottle.tar.gz
==> Caveats
zsh completions have been installed to:
  /opt/homebrew/share/zsh/site-functions
==> Summary
🍺  /opt/homebrew/Cellar/helm/3.16.3: 66 files, 55.4MB
==> Running `brew cleanup helm`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```
### verify
helm version

