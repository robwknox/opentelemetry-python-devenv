FROM dev/otel/all/install:python3.5.10

RUN pip install -e opentelemetry-api/ \
 && pip install -e opentelemetry-sdk/ \
 && pip install -e opentelemetry-proto/ \
 && pip install -e exporter/opentelemetry-exporter-otlp/
