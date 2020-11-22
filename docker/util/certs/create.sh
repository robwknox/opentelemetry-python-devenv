#!/bin/bash
#
# Based on: https://itnext.io/practical-guide-to-securing-grpc-connections-with-go-and-tls-part-1-f63058e9d6d1

# Create CA private key
openssl genrsa -out $CERT_GEN_DIR/ca.key 4096

# Create CA public cert
openssl req -new -x509 -key $CERT_GEN_DIR/ca.key -sha256 -subj "/C=US/ST=NJ/O=CA, Inc." -days 365 -out $CERT_GEN_DIR/ca.crt

# Create service private key
openssl genrsa -out $CERT_GEN_DIR/service.key 4096

# Create service CSR (signing request for CA)
openssl req -new -key $CERT_GEN_DIR/service.key -out $CERT_GEN_DIR/service.csr -config /root/certificate.conf

# Create service public cert
openssl x509 -req -in $CERT_GEN_DIR/service.csr -CA $CERT_GEN_DIR/ca.crt -CAkey $CERT_GEN_DIR/ca.key -CAcreateserial -out $CERT_GEN_DIR/service.pem -days 365 -sha256 -extfile /root/certificate.conf -extensions req_ext
