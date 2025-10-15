
#!/bin/bash

# Script to extract and import certificate chain from a host URL to system trust store
# Usage: ./import-cert-chain.sh <hostname:port>

set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <hostname:port>"
    echo "Example: $0 example.com:443"
    exit 1
fi

HOST_PORT="$1"
TEMP_DIR=$(mktemp -d)
CHAIN_FILE="${TEMP_DIR}/chain.pem"
ROOT_FILE="${TEMP_DIR}/root.crt"
INTERMEDIATE_FILE="${TEMP_DIR}/intermediate.crt"

# Extract certificate chain from host
echo "Extracting certificate chain from ${HOST_PORT}..."
openssl s_client -connect "${HOST_PORT}" -showcerts < /dev/null 2>/dev/null | \
    sed -n '/BEGIN CERTIFICATE/,/END CERTIFICATE/p' > "${CHAIN_FILE}"

if [ ! -s "${CHAIN_FILE}" ]; then
    echo "Error: Failed to retrieve certificates from ${HOST_PORT}"
    rm -rf "${TEMP_DIR}"
    exit 1
fi

# Split chain into individual certificates
csplit -s -z -f "${TEMP_DIR}/cert-" -b "%02d.crt" "${CHAIN_FILE}" '/-----BEGIN CERTIFICATE-----/' '{*}'

CERT_COUNT=$(ls -1 ${TEMP_DIR}/cert-*.crt 2>/dev/null | wc -l)
echo "Found ${CERT_COUNT} certificates in chain"

# Identify root and intermediate certificates
for cert in ${TEMP_DIR}/cert-*.crt; do
    SUBJECT=$(openssl x509 -in "$cert" -noout -subject | sed 's/subject=//')
    ISSUER=$(openssl x509 -in "$cert" -noout -issuer | sed 's/issuer=//')
    
    echo "Processing: ${SUBJECT}"
    
    # Root cert (self-signed)
    if [ "$SUBJECT" = "$ISSUER" ]; then
        echo "  -> Root certificate"
        cp "$cert" "${ROOT_FILE}"
    else
        echo "  -> Intermediate certificate"
        cat "$cert" >> "${INTERMEDIATE_FILE}"
    fi
done

# Import to system trust store (macOS)
if [ -f "${ROOT_FILE}" ]; then
    echo "Importing root certificate to system keychain..."
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain "${ROOT_FILE}"
fi

if [ -f "${INTERMEDIATE_FILE}" ]; then
    echo "Importing intermediate certificates to system keychain..."
    sudo security add-trusted-cert -d -r trustAsRoot -k /Library/Keychains/System.keychain "${INTERMEDIATE_FILE}"
fi

# Cleanup
rm -rf "${TEMP_DIR}"

echo "Certificate chain imported successfully!"