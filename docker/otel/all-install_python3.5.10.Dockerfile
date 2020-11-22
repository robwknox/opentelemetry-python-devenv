FROM python:3.5.10

RUN pip install pytest

RUN git clone https://github.com/open-telemetry/opentelemetry-python.git

WORKDIR /opentelemetry-python

RUN git clone https://github.com/open-telemetry/opentelemetry-python-contrib.git \
 && git -C opentelemetry-python-contrib checkout 5c9e043d6921550d82668788e3758a733fb11cb8

# We can't use the 'develop' mode b/c --with-dev-deps fails on trying to install black (reqs py3.6+)
RUN python scripts/eachdist.py install --editable --eager-upgrades --with-test-deps
