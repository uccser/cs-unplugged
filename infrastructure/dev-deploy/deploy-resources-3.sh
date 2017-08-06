#!/bin/bash

# Deploy generated resource files to the development static file server.

./csu start_without_static

# Generate static PDF resources for deployment.
./csu dev makeresources "Treasure Hunt"

# Install Google Cloud SDK
./infrastructure/install_google_cloud_sdk.sh

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

# Authenticate with gcloud tool using the decrypted service account credentials.
# See: https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account
gcloud auth activate-service-account --key-file continuous-deployment-dev.json

# Display the gcloud version, useful for debugging purposes.
# See: https://cloud.google.com/sdk/gcloud/reference/version
gcloud version

# Create empty SSH keys with an empty passphrase, for Google Cloud SDK to
# copy files to a VM for building the Docker image.
# Only required for deploying to Google App Engine flexible environment.
# See: https://cloud.google.com/solutions/continuous-delivery-with-travis-ci#continuous_deployment_on_app_engine_flexible_environment_instances
ssh-keygen -q -N "" -f ~/.ssh/google_compute_engine

# Publish static files.
#
# This copies the generated static files from tests to the Google Storage
# Bucket.
# See: https://cloud.google.com/python/django/flexible-environment#deploy_the_app_to_the_app_engine_flexible_environment
gsutil rsync -R ./csunplugged/staticfiles/ gs://cs-unplugged-dev.appspot.com/static/
