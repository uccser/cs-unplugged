#!/bin/bash

# Updates the database for the development system

# Overwrite docker-compose.json file with specific file for Cloud SQL Proxy.
mv ./infrastructure/cloud-sql-proxy/docker-compose.yml ./docker-compose.yml

# Decrypt secret files archive that contain credentials.
./infrastructure/dev-deploy/decrypt-dev-secrets.sh

# Load environment variables.
source ./load-dev-deploy-envs.sh
export GOOGLE_AUTH_JSON=`< ./continuous-deployment-dev.json`

# Start the system which runs the migrate and updatedata system commands.
./csu start
