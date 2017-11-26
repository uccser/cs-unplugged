#!/usr/bin/env bash

# Script to push source files to crowdin.
# Source files are uploaded from the current state of branch TRANSLATION_SOURCE_BRANCH.

set -e
set -x
set -o pipefail

source crowdin-bot-config.sh
source crowdin-bot-utils.sh

CLONED_REPO_DIR="source-upload-cloned-repo"

# Clone repo, deleting old clone if exists
if [ -d "${CLONED_REPO_DIR}" ]; then
    reset_repo "${CLONED_REPO_DIR}" "${TRANSLATION_SOURCE_BRANCH}"
else
    git clone "${REPO}" "${CLONED_REPO_DIR}" --branch ${TRANSLATION_SOURCE_BRANCH}
fi

cd "${CLONED_REPO_DIR}"

crowdin upload -c "${CROWDIN_CONFIG_FILE}"
