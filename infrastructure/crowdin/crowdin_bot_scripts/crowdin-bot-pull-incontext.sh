#!/usr/bin/env bash

# Script to pull in-context pseudo-language translation files from crowdin,
# And update them to restore verto tags and non-translatable strings.
# If the resulting files differ from the current state of IN_CONTEXT_L10N_TARGET_BRANCH,
# the changes are pushed to a branch "IN_CONTEXT_L10N_TARGET_BRANCH-in-context-l10n",
# and a pull request opened to merge into IN_CONTEXT_L10N_TARGET_BRANCH

set -e
set -x
set -o pipefail

source crowdin-bot-config.sh
source crowdin-bot-utils.sh

CLONED_REPO_DIR="incontext-download-cloned-repo"
IN_CONTEXT_L10N_PR_BRANCH="${IN_CONTEXT_L10N_TARGET_BRANCH}-in-context-l10n"

# Clone repo, deleting old clone if exists
if [ -d "${CLONED_REPO_DIR}" ]; then
    reset_repo "${CLONED_REPO_DIR}" "${IN_CONTEXT_L10N_TARGET_BRANCH}"
else
    git clone "${REPO}" "${CLONED_REPO_DIR}" --branch ${IN_CONTEXT_L10N_TARGET_BRANCH}
fi

cd "${CLONED_REPO_DIR}"

# Set up git bot parameters
git config user.name "${GITHUB_BOT_NAME}"
git config user.email "${GITHUB_BOT_EMAIL}"

SHA=$(git rev-parse --verify HEAD)

git checkout $IN_CONTEXT_L10N_PR_BRANCH || git checkout -b $IN_CONTEXT_L10N_PR_BRANCH $IN_CONTEXT_L10N_TARGET_BRANCH

# Merge if required
git merge origin/$IN_CONTEXT_L10N_TARGET_BRANCH --quiet --no-edit

crowdin -c "${CROWDIN_CONFIG_FILE}" -l "${CROWDIN_PSEUDO_LANGUAGE}" download
python3 -m crowdin_bot.download_xliff
python3 -m crowdin_bot.modify_pseudo_translations


for content_path in "${CONTENT_PATHS[@]}"; do
  git add "${content_path}/${CSU_PSEUDO_LANGUAGE}"
done

reset_po_files_timestamp_only

# If there are no changes to the compiled out (e.g. this is a README update) then just bail.
if [[ $(git diff --cached) ]]; then
    git commit -m "Update in-context l10n: ${SHA}"
    git push -q origin $IN_CONTEXT_L10N_PR_BRANCH > /dev/null
fi

# If there are no changes to the compiled out (e.g. this is a README update) then just bail.
if [[ $(git diff $IN_CONTEXT_L10N_PR_BRANCH origin/$IN_CONTEXT_L10N_TARGET_BRANCH) ]]; then
    hub pull-request -m "Update in-context localisation files" -b "${IN_CONTEXT_L10N_TARGET_BRANCH}" -h "${IN_CONTEXT_L10N_PR_BRANCH}" || \
        echo "Could not create pull request - perhaps one already exists?"
fi
