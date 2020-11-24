FROM buildpack-deps:buster

RUN git clone https://github.com/pyenv/pyenv.git /root/.pyenv

ENV PYENV_ROOT=/root/.pyenv
ENV PATH="${PYENV_ROOT}/bin:${PYENV_ROOT}/shims:${PATH}"

RUN pyenv install 3.7.9 \
 && pyenv global 3.7.9

RUN pip install pylint

RUN git clone https://github.com/open-telemetry/opentelemetry-python.git

WORKDIR /opentelemetry-python

RUN git clone https://github.com/open-telemetry/opentelemetry-python-contrib.git \
 && git -C opentelemetry-python-contrib checkout 5c9e043d6921550d82668788e3758a733fb11cb8

RUN python scripts/eachdist.py develop

RUN apt-get update && apt-get install -y dos2unix

COPY pylint-path-fix.sh /

RUN dos2unix /pylint-path-fix.sh

