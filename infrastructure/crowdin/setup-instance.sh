# Script to setup crowdin_bot on a GCE instance

set -e

SECRETS_DIR="crowdin_bot_secrets"
SCRIPTS_DIR="crowdin_bot_scripts"
PYTHON_PACKAGE_DIR="crowdin_bot_python_package"

# Install packages
sudo apt-get install git --yes
sudo apt-get install gettext --yes
sudo apt-get install default-jre --yes  # Java, for crowdin cli
sudo apt-get install python3-pip --yes
sudo apt-get install python3-lxml --yes  # Install here instead of pip3 because compilation uses too much RAM
sudo pip3 install -U pip setuptools
sudo pip3 install verto pyyaml
sudo pip3 install django
sudo pip3 install django-environ

# Install crowdin cli
wget -qO - https://artifacts.crowdin.com/repo/GPG-KEY-crowdin | sudo apt-key add -
echo "deb https://artifacts.crowdin.com/repo/deb/ /" | sudo tee /etc/apt/sources.list.d/crowdin.list > /dev/null
sudo apt-get update
sudo apt-get install crowdin --yes

# Install hub
wget https://github.com/github/hub/releases/download/v2.2.5/hub-linux-amd64-2.2.5.tgz
tar zvxvf hub-linux-amd64-2.2.5.tgz
sudo ./hub-linux-amd64-2.2.5/install
rm -rf hub-linux-amd64-2.2.5

# Unzip crowdin-bot source
tar -xvzf crowdin-bot.tar.gz

# Move into secrets directory
cd "${SECRETS_DIR}"

# Decrypt secrets
gcloud kms decrypt --ciphertext-file=uccser_bot_token.enc --plaintext-file=uccser_bot_token --location=global --keyring=csunplugged-keyring --key=uccser-bot-token
gcloud kms decrypt --ciphertext-file=crowdin_api_key.enc --plaintext-file=crowdin_api_key --location=global --keyring=csunplugged-keyring --key=crowdin-api-key
gcloud kms decrypt --ciphertext-file=gce_key.enc --plaintext-file=gce_key --location=global --keyring=csunplugged-keyring --key=uccser-bot-ssh-key

# Add secret env vars to bashrc
cat > crowdin-bot-env-secrets.sh << EOF
export CROWDIN_API_KEY=$(cat crowdin_api_key)
export GITHUB_TOKEN=$(cat uccser_bot_token)
EOF
sudo cp crowdin-bot-env-secrets.sh "../${SCRIPTS_DIR}"

# Setup github SSH key
cp gce_key ~/.ssh/gce_key
chmod 400 ~/.ssh/gce_key
cat >> ~/.ssh/config << EOF
Host github.com
	IdentityFile ~/.ssh/gce_key
	StrictHostKeyChecking no
EOF

# Move into scripts directory
cd ..
cd "${SCRIPTS_DIR}"

# Copy scripts into /usr/local/bin and make them executable
for script in *; do
    sudo cp "${script}" /usr/local/bin
    sudo chmod +x "/usr/local/bin/${script}"
done

# Return to parent directory
cd ..

# Install crowdin-bot python package
sudo pip3 install "${PYTHON_PACKAGE_DIR}"/

# Setup crontab
crontab << EOF
SHELL=/bin/bash
4 12 * * * PATH=\$PATH:/usr/local/bin; source crowdin-bot-env-secrets.sh; crowdin-bot-update-messages.sh > crowdin-bot-update-messages.log 2> crowdin-bot-update-messages.err
4 13 * * * PATH=\$PATH:/usr/local/bin; source crowdin-bot-env-secrets.sh; crowdin-bot-push-source.sh > crowdin-bot-push-source.log 2> crowdin-bot-push-source.err
4 14 * * * PATH=\$PATH:/usr/local/bin; source crowdin-bot-env-secrets.sh; crowdin-bot-pull-translations.sh > crowdin-bot-pull-translations.log 2> crowdin-bot-pull-translations.err
4 15 * * * PATH=\$PATH:/usr/local/bin; source crowdin-bot-env-secrets.sh; crowdin-bot-pull-incontext.sh > crowdin-bot-pull-incontext.log 2> crowdin-bot-pull-incontext.err
EOF
