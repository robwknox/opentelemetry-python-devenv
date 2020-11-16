FROM python:3.9.0

RUN pip install pytest

RUN git clone https://github.com/open-telemetry/opentelemetry-python.git

WORKDIR /opentelemetry-python

RUN python scripts/eachdist.py install
