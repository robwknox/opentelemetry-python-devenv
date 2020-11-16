FROM dev/otel/all/install:python3.9.0

RUN pip install -e opentelemetry-api/ \
 && pip install -e opentelemetry-sdk/ \
 && pip install -e exporter/opentelemetry-exporter-zipkin/