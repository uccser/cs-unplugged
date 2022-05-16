#!/bin/bash

set -e

# Check for environment variables
checkEnvVariableExists() {
    if [ -z ${!1} ]
    then
        echo "ERROR: Define $1 environment variable."
        exit 1
    else
        echo "INFO: $1 environment variable found."
    fi
}
checkEnvVariableExists CS_UNPLUGGED_IMAGE_TAG
checkEnvVariableExists CS_UNPLUGGED_ROUTER_RULE

docker stack deploy cs-unplugged -c docker-compose.prod.yml
docker service scale cs-unplugged_task-update-data=1
