FROM python:3.9.0

COPY src/opentelemetry-python /opentelemetry-python

RUN pip install -e /opentelemetry-python/opentelemetry-api \
 && pip install -e /opentelemetry-python/opentelemetry-sdk

RUN pip install pytest