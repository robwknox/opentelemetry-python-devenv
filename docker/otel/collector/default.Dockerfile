FROM buildpack-deps:buster

RUN apt-get update && apt-get install -y dos2unix

RUN wget https://golang.org/dl/go1.15.5.linux-amd64.tar.gz \
 && tar -C /usr/local -xzf go1.15.5.linux-amd64.tar.gz \
 && rm -f go1.15.5.linux-amd64.tar.gz

RUN git clone https://github.com/open-telemetry/opentelemetry-collector.git

WORKDIR /opentelemetry-collector

RUN mkdir /root/go

ENV GOROOT="/usr/local/go"
ENV GOPATH="/root/go"
ENV PATH="${PATH}:${GOROOT}/bin:${GOPATH}/bin"

RUN make install-tools
RUN make otelcol

COPY .bashrc /root/.bashrc
COPY otel-config.yaml /etc/otel/config.yaml
# Symlink of docker/util/certs/gen/ => certs/
#
#  mklink /D docker\otel\collector\certs docker\util\certs\gen
#
COPY certs/service.key /root/service.key
COPY certs/service.pem /root/service.pem
RUN dos2unix /root/.bashrc /etc/otel/config.yaml /root/service.key /root/service.pem

ENTRYPOINT ["/opentelemetry-collector/bin/otelcol_linux_amd64"]
CMD ["--config", "/etc/otel/config.yaml"]
EXPOSE 55678 55679 55680 55681