#!/bin/bash

MY_PROGRAM="[PROGRAM_NAME]" # For example, "apache2" or "nginx"
MY_USER="[LOCAL_USERNAME]"
CHECKPOINT="/home/$MY_USER/checkpoint.out"
GSUTIL_OPTS="-m -o GSUtil:parallel_composite_upload_threshold=32M"
BUCKET_NAME="[BUCKET_NAME]" # For example, "my-checkpoint-files" (without gs://)

echo "Shutting down!  Seeing if ${MY_PROGRAM} is running."

# Find the newest copy of $MY_PROGRAM
PID="$(pgrep -n "$MY_PROGRAM")"

if [[ "$?" -ne 0 ]]; then
  echo "${MY_PROGRAM} not running, shutting down immediately."
  exit 0
fi

echo "Sending SIGINT to $PID"
kill -2 "$PID"

# Portable waitpid equivalent
while kill -0 "$PID"; do
   sleep 1
done

echo "$PID is done, copying ${CHECKPOINT} to gs://${BUCKET_NAME} as ${MY_USER}"

su "${MY_USER}" -c "gsutil $GSUTIL_OPTS cp $CHECKPOINT gs://${BUCKET_NAME}/"

echo "Done uploading, shutting down."

# TODO:
# - Signal to clear lease on tasks
# - Unmount storage

# To Deploy
# gcloud compute instances create example-instance \
#    --metadata-from-file shutdown-script=examples/scripts/install.sh
