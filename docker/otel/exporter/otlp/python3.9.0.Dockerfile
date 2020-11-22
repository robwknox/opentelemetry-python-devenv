FROM dev/otel/all/install:python3.9.0

RUN pip install -e opentelemetry-api/ \
 && pip install -e opentelemetry-sdk/ \
 && pip install -e opentelemetry-proto/ \
 && pip install -e exporter/opentelemetry-exporter-otlp/

# Symlink of docker/util/certs/gen/ => certs/
#
#  mklink /D docker\otel\exporter\otlp\certs docker\util\certs\gen
#
COPY certs/service.pem /root/service.pem
COPY certs/ca.crt /root/ca.crt