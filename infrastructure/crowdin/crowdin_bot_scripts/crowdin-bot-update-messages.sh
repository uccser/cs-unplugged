set -e
set -x
set -o pipefail

source crowdin-bot-config.sh
source crowdin-bot-utils.sh

CLONED_REPO_DIR="update-messages-cloned-repo"
UPDATE_MESSAGES_PR_BRANCH="${UPDATE_MESSAGES_TARGET_BRANCH}-update-messages"

# Clone repo, deleting old clone if exists
if [ -d "${CLONED_REPO_DIR}" ]; then
    reset_repo "${CLONED_REPO_DIR}" "${UPDATE_MESSAGES_TARGET_BRANCH}"
else
    git clone "${REPO}" "${CLONED_REPO_DIR}" --branch ${UPDATE_MESSAGES_TARGET_BRANCH}
fi

# Change into the working repo
cd "${CLONED_REPO_DIR}"

# Set up git bot parameters
git config user.name "${GITHUB_BOT_NAME}"
git config user.email "${GITHUB_BOT_EMAIL}"

git checkout $UPDATE_MESSAGES_PR_BRANCH || git checkout -b $UPDATE_MESSAGES_PR_BRANCH $UPDATE_MESSAGES_TARGET_BRANCH

# Merge if required
git merge origin/$UPDATE_MESSAGES_TARGET_BRANCH --quiet --no-edit

cd csunplugged
python3 manage.py makemessages -l en --no-location

git add locale/en/LC_MESSAGES/django.po

reset_po_files_timestamp_only

# If there are no changes to the compiled out (e.g. this is a README update) then just bail.
if [[ $(git diff --cached) ]]; then
    git commit -m "Update en message file (django.po)"
    git push -q origin $UPDATE_MESSAGES_PR_BRANCH > /dev/null
fi

# If there are no changes to the compiled out (e.g. this is a README update) then just bail.
if [[ $(git diff $UPDATE_MESSAGES_PR_BRANCH origin/$UPDATE_MESSAGES_TARGET_BRANCH) ]]; then
    hub pull-request -m "Update source message file (django.po)" -b "${UPDATE_MESSAGES_TARGET_BRANCH}" -h "${UPDATE_MESSAGES_PR_BRANCH}" || \
        echo "Could not create pull request - perhaps one already exists?"
fi
