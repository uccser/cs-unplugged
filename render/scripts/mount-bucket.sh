#!/bin/bash
BUCKET_NAME=$1
DIRECTORY=$2

if [ ! -d "${DIRECTORY}" ]; then
  mkdir ${DIRECTORY}
fi

gcsfuse ${BUCKET_NAME} ${DIRECTORY}
