#!/bin/bash

source ./infrastructure/dev-deploy/load-dev-deploy-config-envs.sh

# Deploy generated resource files to the development static file server.

./csu start
./csu update

# Generate static PDF resources for deployment.
docker-compose exec django /docker_venv/bin/python3 ./manage.py makeresources "Modulo Clock"
docker-compose exec django /docker_venv/bin/python3 ./manage.py makeresources "Parity Cards"
docker-compose exec django /docker_venv/bin/python3 ./manage.py makeresources "Piano Keys"
docker-compose exec django /docker_venv/bin/python3 ./manage.py makeresources "Pixel Painter"
docker-compose exec django /docker_venv/bin/python3 ./manage.py makeresources "Searching Cards"

# Install Google Cloud SDK
./infrastructure/install_google_cloud_sdk.sh

# Decrypt secret files archive that contain credentials.
./infrastructure/dev-deploy/decrypt-dev-secrets.sh

# Authenticate with gcloud tool using the decrypted service account credentials.
# See: https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account
gcloud auth activate-service-account --key-file continuous-deployment-dev.json

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
gsutil rsync -R ./csunplugged/staticfiles/resources/ gs://cs-unplugged-dev.appspot.com/static/resources/
