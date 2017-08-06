#!/bin/bash

# Updates the database for the development system

# Deploy the system to the development website.
./csu start

# Install Python requirements for running Django locally when using Google
# Cloud SQL proxy. Ideally this would be run inside the Docker image, to
# prevent having to reinstall the requirements again.
#
# Travis is running on Python 3.6, as set in '.travis.yml'.
#
# Travis already uses isolated virtualenvs to no need to create a virtualenv.
# See: https://docs.travis-ci.com/user/languages/python/#Travis-CI-Uses-Isolated-virtualenvs
pip install -r ./requirements/production.txt

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

# Load environment variables.
# Used when running local Django for updating development database.
. ./load-dev-deploy-envs.sh

# Download the Google Cloud SQL proxy for updating development database.
#
# This is done before any deployment to minimise downtime between the app
# deployment and the database update.
# See: https://cloud.google.com/python/django/flexible-environment#install_the_sql_proxy
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64
# Rename the proxy to standard filename.
mv cloud_sql_proxy.linux.amd64 cloud_sql_proxy
# Allow the proxy to be executable.
chmod +x cloud_sql_proxy

# Start the Google Cloud SQL Proxy.
#
# This connects to the database instance using the connection name set in an
# environment variable. It is authenticated using the service account credentials.
# The proxy command is appended with '&>/dev/null &' to run in the background
# and to not send output to console.
# See: https://cloud.google.com/python/django/flexible-environment#initialize_your_cloud_sql_instance
./cloud_sql_proxy -instances="${GOOGLE_CLOUD_SQL_CONNECTION_NAME}"=tcp:5433 -credential_file="./continuous-deployment-dev.json" >/dev/null 2>/dev/null &

# Update development database.
#
# The approach used for updating the database is to run the Django system
# locally and connect to the development database using the Google Cloud SQL
# proxy.
#
# Change working directory to 'csunplugged' to run 'manage.py' from the
# expected location for running loaders.
cd csunplugged
# Run the 'migrate' command to update the database schema, if required.
# Runs with the database_proxy settings which connect the database to the
# Google Cloud SQL proxy.
python ./manage.py migrate --settings=config.settings.database_proxy
# Run the 'updatedata' command to update the database content.
# Runs with the database_proxy settings which connect the database to the
# Google Cloud SQL proxy.
python ./manage.py updatedata --settings=config.settings.database_proxy
