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
checkEnvVariableExists CS_UNPLUGGED_DOMAIN

# Update Django service
docker stack deploy --compose-file docker-compose.prod.yml cs-unplugged_django

# Run updata_data command
if [ docker service ps cs-unplugged_update-data | grep cs-unplugged_update-data ]
then
    docker service update --force cs-unplugged_update-data
else
    docker service create \
    --name cs-unplugged_update-data \
    --detach \
    --mode replicated-job \
    --label traefik.enable=false \
    --network cs-unplugged_backend \
    --constraint node.role==worker \
    --constraint node.labels.role==apps \
    --env POSTGRES_HOST="postgres" \
    --env=POSTGRES_PORT="5432" \
    --env=DEPLOYMENT_ENVIRONMENT_FILE="/cs-unplugged_deployment_environment" \
    --env=DJANGO_SECRET_KEY_FILE="/run/secrets/cs-unplugged_django_secret_key" \
    --env=POSTGRES_DB_FILE="/run/secrets/cs-unplugged_postgres_db" \
    --env=POSTGRES_USER_FILE="/run/secrets/cs-unplugged_postgres_user" \
    --env=POSTGRES_PASSWORD_FILE="/run/secrets/cs-unplugged_postgres_password" \
    --config cs-unplugged_deployment_environment \
    --secret cs-unplugged_django_secret_key \
    --secret cs-unplugged_postgres_db \
    --secret cs-unplugged_postgres_user \
    --secret cs-unplugged_postgres_password \
    --restart-condition none \
    ghcr.io/uccser/cs-unplugged:${CS_UNPLUGGED_IMAGE_TAG} python ./manage.py updatedata
fi
