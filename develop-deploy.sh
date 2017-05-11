# Install Google Cloud SDK
export CLOUDSDK_CORE_DISABLE_PROMPTS=1;
if [ ! -d ${HOME}/google-cloud-sdk ]; then
     curl https://sdk.cloud.google.com | bash;
fi

# Decrypt and unpack credential files
openssl aes-256-cbc -K $encrypted_323d8adec5b7_key -iv $encrypted_323d8adec5b7_iv -in credentials.tar.gz.enc -out credentials.tar.gz -d
tar -xzf credentials.tar.gz

# Here we use the decrypted service account credentials to authenticate the command line tool
gcloud auth activate-service-account --key-file continuous-deployment-develop-credentials.json

# Install requirements for updating database (minimises downtime later)
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64
cloud_sql_proxy.linux.amd64 cloud_sql_proxy
chmod +x cloud_sql_proxy
./cloud_sql_proxy -instances="$GOOGLE_CLOUD_SQL_CONNECTION_NAME"=tcp:5432 -credential_file="./../continuous-deployment-develop-credentials.json" &
exit
sudo apt-get install -y python3 python3-dev python3-pip
python -m virtualenv --python=python3.4 /venv
/venv/bin/pip3 install -r /requirements/production.txt

# Publish static files
gsutil rsync -R ./csunplugged/staticfiles/ gs://cs-unplugged-develop/static/

# Publish app engine
gcloud app deploy ./app-develop.yaml --quiet

# Update database
cd csunplugged
/venv/bin/python3 ./manage.py migrate --settings=config.settings.database_proxy
/venv/bin/python3 ./manage.py updatedata --settings=config.settings.database_proxy
