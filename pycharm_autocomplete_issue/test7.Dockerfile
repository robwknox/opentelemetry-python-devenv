FROM python:3.9.0

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev tox python-openssl git

RUN git clone https://github.com/open-telemetry/opentelemetry-python.git

WORKDIR /opentelemetry-python

RUN pip install opentelemetry-api/
RUN pip install opentelemetry-sdk/
RUN pip install -e exporter/opentelemetry-exporter-prometheus/
RUN pip install exporter/opentelemetry-exporter-zipkin/
