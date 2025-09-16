# Cloud Native Buildpacks Setup

Reference:  https://buildpacks.io/docs/

## install the pack CLI
https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/

### macOs
brew install buildpacks/tap/pack

## deploying with buildpacks
pack builder suggest

pack build sample-app --path samples/apps/java-maven --builder cnbs/sample-builder:noble

# in a nodejs app working folder
pack build next-sample --path .  --builder paketobuildpacks/builder-jammy-tiny    
# result - no buidpack detected

pack build next-sample --path . --buildpack gcr.io/paketo-buildpacks/nodejs --builder paketobuildpacks/builder-jammy-full 