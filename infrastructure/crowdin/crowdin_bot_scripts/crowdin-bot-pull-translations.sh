set -e
set -x
set -o pipefail

source crowdin-bot-config.sh
source crowdin-bot-utils.sh

REPO="git@github.com:jordangriffiths01/crowdin_testing.git"
CLONED_REPO_DIR="update-completed-translations-cloned-repo"
TRANSLATION_PR_BRANCH_BASE="${TRANSLATION_TARGET_BRANCH}-translations"

# Clone repo, deleting old clone if exists
if [ -d "${CLONED_REPO_DIR}" ]; then
    reset_repo "${CLONED_REPO_DIR}" "${TRANSLATION_TARGET_BRANCH}"
else
    git clone "${REPO}" "${CLONED_REPO_DIR}" --branch ${TRANSLATION_TARGET_BRANCH}
fi

python3 -m crowdin_bot.get_language_map --crowdin-config "${CLONED_REPO_DIR}/${CROWDIN_CONFIG_FILE}" > language_map.json

# Change into the working repo
cd "${CLONED_REPO_DIR}"

# Set up git bot parameters
git config user.name "${GITHUB_BOT_NAME}"
git config user.email "${GITHUB_BOT_EMAIL}"

# Populate array of all project languages
languages=($(python3 -m crowdin_bot.get_crowdin_languages))

for language in ${languages[@]}; do

    # The branch for new translationss
    TRANSLATION_PR_BRANCH="${TRANSLATION_PR_BRANCH_BASE}-${language}"

    # Checkout the translation branch, creating if off $TRANSLATION_TARGET_BRANCH if it didn't already exist
    git checkout $TRANSLATION_PR_BRANCH || git checkout -b $TRANSLATION_PR_BRANCH $TRANSLATION_TARGET_BRANCH

    # Merge if required
    git merge $TRANSLATION_TARGET_BRANCH --quiet --no-edit

    # Delete existing translation directories
    mapped_code=$(cat ../language_map.json | python -c "import json,sys;obj=json.load(sys.stdin);print(obj[\"${language}\"]);")
    for content_path in "${CONTENT_PATHS[@]}"; do
        translation_path="${content_path}/${mapped_code}"
        if [ -d "${translation_path}" ]; then
            rm -r "${translation_path}"
        fi
    done

    # Download translations from crowdin
    crowdin -c "${CROWDIN_CONFIG_FILE}" -l "${language}" download

    # Boolean flag indicating whether changes are made that should be pushed
    changes=0

    # If there are any files that were not re-downloaded from crowdin, they
    # no longer exist on the translation server - delete them
    if [[ $(git ls-files --deleted) ]]; then
        git rm $(git ls-files --deleted)
        git commit -m "Deleting old translation files no longer present on Crowdin"
        changes=1
    fi

    # Get list of files that are completely translated/ready for committing
    # Note that .po files are included even if not completely translated
    python3 -m crowdin_bot.get_complete_translations --crowdin-code "${language}" --csu-code "${mapped_code}" > "${language}_completed"

    # Loop through each completed translation file:
    while read path; do
        # If file is different to what's already on the branch, commit it
        git add "${path}" >/dev/null 2>&1 || true
        if [[ $(git diff --cached -- "${path}") ]]; then
          git commit -m "New translations for ${path}"
          changes=1
        fi
    done < "${language}_completed"

    # If any changes were made, push to github
    if [[ $changes -eq 1 ]]; then
        git push -q origin $TRANSLATION_PR_BRANCH > /dev/null
    fi

    # If the target branch differs from the source branch, create a PR
    if [[ $(git diff $TRANSLATION_PR_BRANCH $TRANSLATION_TARGET_BRANCH) ]]; then
        hub pull-request -f -m "Updated translations for ${language}" -b "${TRANSLATION_TARGET_BRANCH}" -h "${TRANSLATION_PR_BRANCH}" || \
            echo "Could not create pull request - this probably means one already exists"
    fi

    # Return repo to clean state for next language
    git reset --hard
    git clean -fdx

done
