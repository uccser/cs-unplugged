# TODO: PAth manipulations?

tar -xvzf crowdin.tar.gz

gcloud kms decrypt --ciphertext-file=uccser_bot_token.enc --plaintext-file=uccser_bot_token --location=global --keyring=csunplugged-keyring --key=uccser-bot-token
gcloud kms decrypt --ciphertext-file=crowdin_api_key.enc --plaintext-file=crowdin_api_key --location=global --keyring=csunplugged-keyring --key=crowdin-api-key
cat >> ~/.bashrc << EOF
export CROWDIN_API_KEY=$(cat crowdin_api_key)
export GITHUB_TOKEN=$(cat uccser_bot_token)
EOF

# TODO: Activate service account to get access to KMS
gcloud kms decrypt --ciphertext-file=gce_key.enc --plaintext-file=gce_key --location=global --keyring=csunplugged-keyring --key=uccser-bot-ssh-key
eval "$(ssh-agent -s)"
cp gce_key ~/.ssh
chmod 400 ~/.ssh/gce_key
ssh-add ~/.ssh/gce_key

cat >> ~/.ssh/config << EOF
Host github.com
	IdentityFile ~/.ssh/gce_key
EOF

apt-get install git --yes
apt-get install python3-pip
pip3 install verto

apt-get install python3-lxml # Can't use pip - not enough RAM for compilation!

# Install Crowdin CLI
wget -qO - https://artifacts.crowdin.com/repo/GPG-KEY-crowdin | sudo apt-key add -
echo "deb https://artifacts.crowdin.com/repo/deb/ /" > /etc/apt/sources.list.d/crowdin.list
apt-get update
apt-get install crowdin --yes
# ... and Java dependency
apt-get install default-jre --yes

# Install hub
wget https://github.com/github/hub/releases/download/v2.2.5/hub-linux-amd64-2.2.5.tgz
tar zvxvf hub-linux-amd64-2.2.5.tgz
sudo ./hub-linux-amd64-2.2.5/install
