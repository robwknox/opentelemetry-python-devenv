FROM buildpack-deps:buster

RUN apt-get update && apt-get install -y dos2unix

WORKDIR /root

COPY certificate.conf certificate.conf
COPY create.sh create.sh
RUN dos2unix certificate.conf
RUN dos2unix create.sh

ENV CERT_GEN_DIR="/root/gen"
RUN mkdir ${CERT_GEN_DIR}

ENTRYPOINT ["./create.sh"]