# Script to deploy crowdin bot to GCE

set -e

PROJECT="cs-unplugged-dev"
ZONE="us-central1-c"

INSTANCE_NAME="crowdin-bot"
MACHINE_TYPE="f1-micro"
SERVICE_ACCOUNT="uccser-bot@cs-unplugged-dev.iam.gserviceaccount.com"

# Create instance
echo "Creating instance ${INSTANCE_NAME}"
gcloud compute --project "${PROJECT}" instances create "${INSTANCE_NAME}" \
    --zone "${ZONE}" --machine-type "${MACHINE_TYPE}" \
    --image-family "ubuntu-1404-lts" \
    --image-project "ubuntu-os-cloud" \
    --service-account "${SERVICE_ACCOUNT}" \
    --scopes "https://www.googleapis.com/auth/cloudkms" \
    --boot-disk-size "10" --boot-disk-type "pd-standard"

# Transfer files to instance
source_tarball=crowdin-bot.tar.gz
echo "Creating tarball ${source_tarball}"
tar cvzf "${source_tarball}" crowdin_bot_python_package crowdin_bot_scripts crowdin_bot_secrets
for i in $(seq 1 10); do
    echo "Copying ${source_tarball} to /tmp on ${INSTANCE_NAME}"
    gcloud beta compute scp setup-instance.sh "${source_tarball}" "${INSTANCE_NAME}:/tmp" --zone="${ZONE}" && break
    echo "Could not SCP, instance is probably still booting. Retrying in 10 seconds"
    sleep 10
done

# Unzip files and run setup script
echo "Setting up instance and installing crowdin_bot"
gcloud compute ssh "${INSTANCE_NAME}" --zone="${ZONE}" -- "cp /tmp/crowdin-bot.tar.gz /tmp/setup-instance.sh ~ && chmod +x setup-instance.sh && ./setup-instance.sh"

echo "Cleaning up"
rm crowdin-bot.tar.gz

echo "Deployed Successfully"
