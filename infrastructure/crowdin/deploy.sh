set -e

PROJECT="cs-unplugged-dev"
ZONE="us-central1-c"

INSTANCE_NAME="crowdin-bot"
MACHINE_TYPE="f1-micro"
SERVICE_ACCOUNT="uccser-bot@cs-unplugged-dev.iam.gserviceaccount.com"

# Create instance
gcloud compute --project "${PROJECT}" instances create "${INSTANCE_NAME}" \
    --zone "${ZONE}" --machine-type "${MACHINE_TYPE}" \
    --image-family "ubuntu-1404-lts" \
    --image-project "ubuntu-os-cloud" \
    --service-account "${SERVICE_ACCOUNT}" \
    --scopes "https://www.googleapis.com/auth/cloudkms" \
    --boot-disk-size "10" --boot-disk-type "pd-standard"

# Transfer files to instance
tar cvzf crowdin-bot.tar.gz crowdin_bot_python_package crowdin_bot_scripts crowdin_bot_secrets
gcloud beta compute scp setup-instance.sh crowdin-bot.tar.gz "${INSTANCE_NAME}:/tmp" --zone="${ZONE}"

# Unzip files and run setup script
gcloud compute ssh "${INSTANCE_NAME}" --zone="${ZONE}" -- "cp /tmp/crowdin-bot.tar.gz /tmp/setup-instance.sh ~ && chmod +x setup-instance.sh && sudo ./setup-instance.sh"



# Only once, check in encrypted key
# gcloud kms encrypt --plaintext-file=gce_key --ciphertext-file=gce_key.enc --keyring=csunplugged-keyring --key=uccser-bot-ssh-key --location=global
# gcloud kms encrypt --plaintext-file=crowdin_api_key --ciphertext-file=crowdin_api_key.enc --keyring=csunplugged-keyring --key=crowdin-api-key --location=global
# gcloud kms encrypt --plaintext-file=uccser_bot_token --ciphertext-file=uccser_bot_token.enc --keyring=csunplugged-keyring --key=uccser-bot-token --location=global
