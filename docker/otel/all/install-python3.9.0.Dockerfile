FROM python:3.9.0

RUN pip install pytest

RUN git clone https://github.com/open-telemetry/opentelemetry-python.git

WORKDIR /opentelemetry-python

RUN git clone https://github.com/open-telemetry/opentelemetry-python-contrib.git \
 && git -C opentelemetry-python-contrib checkout 5c9e043d6921550d82668788e3758a733fb11cb8

RUN python scripts/eachdist.py install
