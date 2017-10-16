#!/bin/bash

# Updates the database for the development system

# Overwrite docker-compose.json file with specific file for Cloud SQL Proxy.
mv ./infrastructure/cloud-sql-proxy/docker-compose.yml ./docker-compose.yml

# Decrypt secret files archive that contain credentials.
./infrastructure/prod-deploy/decrypt-prod-secrets.sh

# Load environment variables.
source ./load-prod-deploy-envs.sh
export GOOGLE_AUTH_JSON=`< ./continuous-deployment-prod.json`

# Download the Google Cloud SQL proxy for updating development database.
#
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

# Start the system which runs the migrate and updatedata system commands.
./csu start
