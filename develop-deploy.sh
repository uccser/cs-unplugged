# Install Google Cloud SDK
pip install -r ./requirements/production.txt
export CLOUDSDK_CORE_DISABLE_PROMPTS=1;
if [ ! -d ${HOME}/google-cloud-sdk ]; then
     curl https://sdk.cloud.google.com | bash;
fi

# Decrypt and unpack credential files
openssl aes-256-cbc -K $encrypted_323d8adec5b7_key -iv $encrypted_323d8adec5b7_iv -in credentials.tar.gz.enc -out credentials.tar.gz -d
tar -xzf credentials.tar.gz

# Here we use the decrypted service account credentials to authenticate the command line tool
gcloud auth activate-service-account --key-file continuous-deployment-develop-credentials.json
sudo gcloud components update
gcloud version
ssh-keygen -q -N "" -f ~/.ssh/google_compute_engine

# Install requirements for updating database (minimises downtime later)
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64
mv cloud_sql_proxy.linux.amd64 cloud_sql_proxy
chmod +x cloud_sql_proxy
./cloud_sql_proxy -instances="$GOOGLE_CLOUD_SQL_CONNECTION_NAME"=tcp:5433 -credential_file="./continuous-deployment-develop-credentials.json" &>/dev/null &

# Publish static files
gsutil rsync -R ./csunplugged/staticfiles/ gs://cs-unplugged-develop/static/

# Publish app engine
gcloud app deploy ./app-develop.yaml --quiet --project=cs-unplugged-develop

# Update database
cd csunplugged
python ./manage.py migrate --settings=config.settings.database_proxy
python ./manage.py updatedata --settings=config.settings.database_proxy
