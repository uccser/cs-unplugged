#!/bin/bash

source ./infrastructure/prod-deploy/load-prod-deploy-config-envs.sh

# Updates the database for the development system
mv ./infrastructure/cloud-sql-proxy/docker-compose.yml ./docker-compose.yml

# Decrypt secret files archive that contain credentials.
./infrastructure/prod-deploy/decrypt-prod-secrets.sh

# Load environment variables.
source ./load-prod-deploy-envs.sh

# Start the system and run the migrate and updatedata system commands.
docker-compose up -d
./csu dev static
./csu dev migrate
./csu dev updatedata
