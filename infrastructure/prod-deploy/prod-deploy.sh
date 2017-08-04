#!/bin/bash
# Deploy the system to the production website.

# Generate production static files
./csu dev static_prod

# Generate static PDF resources for deployment.
./csu dev makeresources

# Install Python requirements for running Django locally when using Google
# Cloud SQL proxy. Ideally this would be run inside the Docker image, to
# prevent having to reinstall the requirements again.
#
# Travis is running on Python 3.6, as set in '.travis.yml'.
#
# Travis already uses isolated virtualenvs to no need to create a virtualenv.
# See: https://docs.travis-ci.com/user/languages/python/#Travis-CI-Uses-Isolated-virtualenvs
pip install -r ./requirements/production.txt

# Set the environment variable for Google Cloud SDK to disable prompts
# and choose default settings.
export CLOUDSDK_CORE_DISABLE_PROMPTS=1;

# Create an environment variable for the correct distribution.
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

# Add the Cloud SDK distribution URI as a package source.
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key.
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

# Update the package list and install the Cloud SDK.
sudo apt-get update && sudo apt-get install google-cloud-sdk

# Decrypt secret files archive that contain credentials.
#
# This includes:
#   - continuous-deployment-prod.json
#     Google Cloud Platform Service Account for using with gcloud.
#   - app-prod.yaml
#     Google App Engine YAML file for deployment, contains sensitive data.
#   - load-prod-deploy-envs.sh
#     Loads environment variables used when running local Django.
openssl aes-256-cbc -K "${encrypted_9cabeeff4658_key}" -iv "${encrypted_9cabeeff4658_iv}" -in ./infrastructure/prod-deploy/prod-deploy-secrets.tar.enc -out prod-deploy-secrets.tar -d

# Unzip the decrypted secret archive into the current folder.
tar -xf prod-deploy-secrets.tar

# Authenticate with gcloud tool using the decrypted service account credentials.
# See: https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account
gcloud auth activate-service-account --key-file continuous-deployment-prod.json

# Display the gcloud version, useful for debugging purposes.
# See: https://cloud.google.com/sdk/gcloud/reference/version
gcloud version

# Create empty SSH keys with an empty passphrase, for Google Cloud SDK to
# copy files to a VM for building the Docker image.
# Only required for deploying to Google App Engine flexible environment.
# See: https://cloud.google.com/solutions/continuous-delivery-with-travis-ci#continuous_deployment_on_app_engine_flexible_environment_instances
ssh-keygen -q -N "" -f ~/.ssh/google_compute_engine

# Delete all previous stopped versions of application on Google App Engine.
# This command deletes all stopped applications of the 'default' service,
# and when the new application is deployed, the previous application version
# will remain until the next deployment.
# We delete old versions due avoid hitting the App Engine version limit.
declare -a versions_to_delete
versions_to_delete=($(gcloud app versions list --filter="SERVING_STATUS=STOPPED" --service=default --format="[no-heading]" | awk '{print $2}' | tr '\n' ' '))
for version in "${versions_to_delete[@]}"; do
  gcloud app versions delete --service=default ${version}
done

# Load environment variables.
# Used when running local Django for updating production database.
. ./load-prod-deploy-envs.sh

# Download the Google Cloud SQL proxy for updating production database.
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
./cloud_sql_proxy -instances="${GOOGLE_CLOUD_SQL_CONNECTION_NAME}"=tcp:5433 -credential_file="./continuous-deployment-prod.json" >/dev/null 2>/dev/null &

# Publish static files.
#
# This copies the generated static files from tests to the Google Storage
# Bucket.
# See: https://cloud.google.com/python/django/flexible-environment#deploy_the_app_to_the_app_engine_flexible_environment
gsutil rsync -R ./csunplugged/staticfiles/ gs://cs-unplugged.appspot.com/static/

# Publish Django system to Google App Engine.
#
# This deploys using the 'app-prod.yaml' decrypted earlier that contains
# secret environment variables to use within the application.
# Project is specified to ensure correct project deployment.
# Runs with '--quiet' to skip prompt of confirmation.
# If multiple services are deployed at a later stage, these should be checked
# that the apps deploy to the correct services.
# See: https://cloud.google.com/sdk/gcloud/reference/app/deploy
gcloud app deploy ./app-prod.yaml --quiet --project=cs-unplugged

# Update production database.
#
# The approach used for updating the database is to run the Django system
# locally and connect to the production database using the Google Cloud SQL
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
