
#!/bin/bash

# Remove self-signed certificate associated with a host from trust store
# Usage: {./rm-self-signed-host-cert.sh} <hostname> [port]

set -e

HOSTNAME="${1}"
PORT="${2:-443}"

if [ -z "$HOSTNAME" ]; then
    echo "Usage: $0 <hostname> [port]"
    echo "Example: $0 example.com 443"
    exit 1
fi

echo "Removing certificate for ${HOSTNAME}:${PORT} from trust store..."

# Get the certificate alias by searching for the hostname
ALIAS=$(security find-certificate -a -c "${HOSTNAME}" -Z | grep "SHA-1" | head -1 | awk '{print $3}')

if [ -z "$ALIAS" ]; then
    echo "No certificate found for ${HOSTNAME}"
    exit 1
fi

# Remove from system keychain (requires sudo)
echo "Removing certificate with SHA-1: ${ALIAS}"
sudo security delete-certificate -Z "${ALIAS}" /Library/Keychains/System.keychain

echo "Certificate removed successfully"