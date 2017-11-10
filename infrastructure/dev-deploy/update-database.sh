#!/bin/bash

# Updates the database for the development system

# Decrypt secret files archive that contain credentials.
./infrastructure/dev-deploy/decrypt-dev-secrets.sh

# Load environment variables.
source ./load-dev-deploy-envs.sh
export GOOGLE_AUTH_JSON="$(cat ./continuous-deployment-dev.json)"

# Start the system and run the migrate and updatedata system commands.
docker-compose up -f ./infrastructure/cloud-sWeql-proxy/docker-compose.yml -d
./csu static
./csu migrate
./csu updatedata
