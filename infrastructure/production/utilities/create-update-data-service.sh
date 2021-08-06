#!/bin/bash

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
    --env=DEPLOYMENT_ENVIRONMENT_FILE="/cs-field-guide_deployment_environment" \
    --env=DJANGO_SECRET_KEY_FILE="/run/secrets/cs-unplugged_django_secret_key" \
    --env=POSTGRES_DB_FILE="/run/secrets/cs-unplugged_postgres_db" \
    --env=POSTGRES_USER_FILE="/run/secrets/cs-unplugged_postgres_user" \
    --env=POSTGRES_PASSWORD_FILE="/run/secrets/cs-unplugged_postgres_password" \
    --config cs-field-guide_deployment_environment \
    --secret cs-unplugged_django_secret_key \
    --secret cs-unplugged_postgres_db \
    --secret cs-unplugged_postgres_user \
    --secret cs-unplugged_postgres_password \
    --restart-condition none \
    ghcr.io/uccser/cs-unplugged:develop python ./manage.py updatedata
