set -e
set -x

REPO="git@github.com:jordangriffiths01/crowdin_testing.git"
CLONED_REPO_DIR="translations-download-cloned-repo"
CROWDIN_CONFIG_FILE="crowdin_content.yaml"
CROWDIN_BUILD_DIR="crowdin_build"

SOURCE_BRANCH="develop"
TARGET_BRANCH_BASE="develop-translations"

# Clone repo, deleting old clone if exists
if [ -d "${CLONED_REPO_DIR}" ]; then
    rm -rf "${CLONED_REPO_DIR}"
fi
git clone "${REPO}" "${CLONED_REPO_DIR}" --branch ${SOURCE_BRANCH}

# Copy repo to separate build directory
# This keeps it out of the way when changing between branches etc.
if [ -d "${CROWDIN_BUILD_DIR}" ]; then
    rm -rf "${CROWDIN_BUILD_DIR}"
fi
cp -r ${CLONED_REPO_DIR} ${CROWDIN_BUILD_DIR}

# Download all translation files from crowdin
cd "${CROWDIN_BUILD_DIR}"
crowdin -c "${CROWDIN_CONFIG_FILE}" download

# Change into the working repo
cd "../${CLONED_REPO_DIR}"

# Set up git bot parameters
# TODO: Change these
git config user.name "Travis CI"
git config user.email "test@test.com"

# Populate array of all project languages
languages=($(python3 infrastructure/crowdin/get_crowdin_languages.py))


for language in ${languages[@]}; do

    # The branch for new translationss
    TARGET_BRANCH="${TARGET_BRANCH_BASE}-${language}"

    # Checkout the translation branch, creating if off $SOURCE_BRANCH if it didn't already exist
    git checkout $TARGET_BRANCH || git checkout -b $TARGET_BRANCH $SOURCE_BRANCH

    # Merge if required
    git merge $SOURCE_BRANCH --quiet --no-edit

    # Overwrite directory tree with saved built version
    cp -r "../${CROWDIN_BUILD_DIR}/csunplugged" .

    # Get list of files that are completely translated/ready for committing
    # Note that .po files are included even if not completely translated
    python3 infrastructure/crowdin/get_complete_translations.py "${language}" > "${language}_completed"


    changes=0
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
        git push -q origin $TARGET_BRANCH > /dev/null
    fi

    # If the target branch differs from the source branch, create a PR
    if [[ $(git diff $TARGET_BRANCH $SOURCE_BRANCH) ]]; then
        hub pull-request -m "Updated translations for ${language}" -b "${SOURCE_BRANCH}" -h "${TARGET_BRANCH}" || \
            echo "Could not create pull request - perhaps one already exists?"
    fi

    # Return repo to clean state for next language
    git reset --hard
    git clean -fd

done
