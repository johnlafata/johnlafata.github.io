ARG PLATFORM_ARG="windows/x86_64"
# alternately "windows/ARM64" or "windows/ARM"?    
# Indicates that the .net/framework image will be used as the base image.
# FROM --platform=${PLATFORM_ARG} mcr.microsoft.com/dotnet/framework/runtime
FROM --platform=${PLATFORM_ARG} mcr.microsoft.com/dotnet/framework/runtime:4.8-windowsservercore-ltsc2019
     
# other alternate base image - for .net core 
# Indicates that the windowsservercore image will be used as the base image.
# FROM --platform=windows/x86_64  mcr.microsoft.com/windows/servercore:ltsc2019

# # Metadata indicating an image maintainer.
# LABEL maintainer="jshelton@contoso.com"

# # Uses dism.exe to install the IIS role.
# RUN dism.exe /online /enable-feature /all /featurename:iis-webserver /NoRestart

# Creates an HTML file and adds content to this file.
# RUN echo "Hello World - Dockerfile" > c:\inetpub\wwwroot\index.html

# Sets a command or process that will run each time a container is run from the new image.
CMD [ "cmd" ]