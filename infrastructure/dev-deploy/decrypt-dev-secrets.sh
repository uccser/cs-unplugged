#!/bin/bash

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
