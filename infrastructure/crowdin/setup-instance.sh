set -e

SECRETS_DIR="crowdin_bot_secrets"
SCRIPTS_DIR="crowdin_bot_scripts"
PYTHON_PACKAGE_DIR="crowdin_bot_python_package"

# Install packages
apt-get install git --yes
apt-get install default-jre --yes  # Java, for crowdin cli
apt-get install python3-pip --yes
apt-get install python3-lxml --yes  # Install here instead of pip3 because compilation uses too much RAM
pip3 install -U pip setuptools
pip3 install verto

# Install crowdin cli
wget -qO - https://artifacts.crowdin.com/repo/GPG-KEY-crowdin | sudo apt-key add -
echo "deb https://artifacts.crowdin.com/repo/deb/ /" > /etc/apt/sources.list.d/crowdin.list
apt-get update
apt-get install crowdin --yes

# Install hub
wget https://github.com/github/hub/releases/download/v2.2.5/hub-linux-amd64-2.2.5.tgz
tar zvxvf hub-linux-amd64-2.2.5.tgz
./hub-linux-amd64-2.2.5/install
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
cat >> ~/.bashrc << EOF
export CROWDIN_API_KEY=$(cat crowdin_api_key)
export GITHUB_TOKEN=$(cat uccser_bot_token)
EOF

# Add github ssh key to ssh agent
eval "$(ssh-agent -s)"
cp gce_key ~/.ssh/id_rsa
chmod 400 ~/.ssh/id_rsa
# ...and add it to config file in case of restart
# TODO: Fix this, it's not registering properly, so can't git clone
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
    cp "${script}" /usr/local/bin
    chmod +x "/usr/local/bin/${script}"
done

# Return to parent directory
cd ..

# Install crowdin-bot python package
pip3 install "${PYTHON_PACKAGE_DIR}"/
