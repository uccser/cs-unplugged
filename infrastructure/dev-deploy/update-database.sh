#!/bin/bash

# Updates the database for the development system

# Overwrite docker-compose.json file with specific file for Cloud SQL Proxy.
mv ./infrastructure/cloud-sql-proxy/docker-compose.yml ./docker-compose.yml

# Decrypt secret files archive that contain credentials.
#
# This includes:
#   - continuous-deployment-dev.json
#     Google Cloud Platform Service Account for using with gcloud.
#   - app-dev.yaml
#     Google App Engine YAML file for deployment, contains sensitive data.
#   - load-dev-deploy-envs.sh
#     Loads environment variables used when running local Django.
openssl aes-256-cbc -K "${encrypted_323d8adec5b7_key}" -iv "${encrypted_323d8adec5b7_iv}" -in ./infrastructure/dev-deploy/dev-deploy-secrets.tar.enc -out dev-deploy-secrets.tar -d

# Unzip the decrypted secret archive into the current folder.
tar -xf dev-deploy-secrets.tar

# Load environment variables.
source ./load-dev-deploy-envs.sh
export GOOGLE_AUTH_JSON=`< ./continuous-deployment-dev.json`

# Start the system which runs the migrate and updatedata system commands.
./csu start
