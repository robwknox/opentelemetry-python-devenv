FROM buildpack-deps:buster

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev tox python-openssl

RUN git clone https://github.com/pyenv/pyenv.git /root/.pyenv

ENV PYENV_ROOT=/root/.pyenv
ENV PATH="${PYENV_ROOT}/bin:${PYENV_ROOT}/shims:${PATH}"

RUN pyenv install 3.9.0 \
 && pyenv install 3.8.6 \
 && pyenv install 3.7.9 \
 && pyenv install 3.6.12 \
 && pyenv install 3.5.10 \
 && pyenv install pypy3.6-7.3.1 \
 && pyenv global 3.9.0 3.8.6 3.7.9 3.6.12 3.5.10 pypy3.6-7.3.1

RUN pip install pytest

COPY src/opentelemetry-python /opentelemetry-python

WORKDIR /opentelemetry-python

RUN python scripts/eachdist.py develop

#RUN tox --notest
