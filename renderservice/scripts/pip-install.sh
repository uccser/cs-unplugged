#!/bin/bash
PIP_EXEC=$1
REQUIREMENTS=$2
for line in $(cat ${REQUIREMENTS})
do
  ${PIP_EXEC} install ${line}
done
