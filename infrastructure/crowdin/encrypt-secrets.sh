# Encrypt file "gce_key", a github ssh private key attached to the uccser bot account
gcloud kms encrypt --plaintext-file=gce_key --ciphertext-file=gce_key.enc --keyring=csunplugged-keyring --key=uccser-bot-ssh-key --location=global

# Encrypt file "uccser_bot_token", the github personal access token for the uccser bot account
gcloud kms encrypt --plaintext-file=uccser_bot_token --ciphertext-file=uccser_bot_token.enc --keyring=csunplugged-keyring --key=uccser-bot-token --location=global

# Encrypt file "crowdin_api_key", the crowdin API key
gcloud kms encrypt --plaintext-file=crowdin_api_key --ciphertext-file=crowdin_api_key.enc --keyring=csunplugged-keyring --key=crowdin-api-key --location=global
