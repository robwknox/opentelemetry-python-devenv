#!/bin/bash
# Get the last arg which is our file path for pylint
UNIX_PATH=$(echo "${1}" | sed 's/\\/\//g' | sed 's/^src//g')
pylint \
  -v \
  --rcfile=/opentelemetry-python/.pylintrc \
  --disable=C0328 \
  --msg-template="C:\Users\robwk\PycharmProjects\openTelemetry\src\opentelemetry-python\{path}:{line}:{column}: {msg_id}:({symbol}) {msg}" \
  $UNIX_PATH
