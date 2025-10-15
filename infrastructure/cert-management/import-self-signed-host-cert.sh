#!/bin/bash

# Script to download a self-signed certificate and import it to macOS Keychain

set -e

# Check if hostname is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <hostname:port>"
    echo "Example: $0 localhost:8443"
    exit 1
fi

HOST_PORT=$1
HOST=$(echo $HOST_PORT | cut -d':' -f1)
PORT=$(echo $HOST_PORT | cut -d':' -f2)

# Default to 443 if no port specified
if [ "$HOST" == "$PORT" ]; then
    PORT=443
fi

CERT_FILE="/tmp/${HOST}.crt"

echo "Downloading certificate from ${HOST}:${PORT}..."

# Get the certificate using openssl
openssl s_client -connect ${HOST}:${PORT} -showcerts </dev/null 2>/dev/null | \
    openssl x509 -outform PEM > ${CERT_FILE}

if [ ! -s ${CERT_FILE} ]; then
    echo "Error: Failed to download certificate"
    exit 1
fi

echo "Certificate downloaded to ${CERT_FILE}"
echo "Importing certificate to System Keychain (requires sudo)..."

# Import to System keychain as trusted root CA
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ${CERT_FILE}

echo "Certificate successfully imported!"
echo "You may need to restart your applications for changes to take effect."

# Cleanup
rm -f ${CERT_FILE}