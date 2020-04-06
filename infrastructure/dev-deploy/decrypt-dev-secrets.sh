#!/bin/bash

# Decrypt secret files archive that contain credentials.
#
# This includes:
#   - continuous-deployment-dev.json
#     Google Cloud Platform Service Account for using with gcloud.
#   - load-dev-deploy-envs.sh
#     Loads environment variables used when running Django.
openssl aes-256-cbc -K "${encrypted_d482352db195_key}" -iv "${encrypted_d482352db195_iv}" -in ./infrastructure/dev-deploy/dev-deploy-secrets.tar.enc -out dev-deploy-secrets.tar -d

# Unzip the decrypted secret archive into the current folder.
tar -xf dev-deploy-secrets.tar
