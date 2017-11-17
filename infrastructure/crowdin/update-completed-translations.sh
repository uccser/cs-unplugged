set -e
set -x

REPO="git@github.com:jordangriffiths01/crowdin_testing.git"
CLONED_REPO_DIR="translations-download-cloned-repo"
CROWDIN_CONFIG_FILE="crowdin_content.yaml"

SOURCE_BRANCH="develop"
TARGET_BRANCH_BASE="develop-translations"

CONTENT_PATHS=(
    "csunplugged/topics/content"
    "csunplugged/locale"
)

# Clone repo, deleting old clone if exists
if [ -d "${CLONED_REPO_DIR}" ]; then
    rm -rf "${CLONED_REPO_DIR}"
fi
git clone "${REPO}" "${CLONED_REPO_DIR}" --branch ${SOURCE_BRANCH}

# Change into the working repo
cd "${CLONED_REPO_DIR}"

# Set up git bot parameters
# TODO: Change these
git config user.name "Travis CI"
git config user.email "test@test.com"

# Populate array of all project languages
languages=($(python3 ../get_crowdin_languages.py))

for language in ${languages[@]}; do

    # The branch for new translationss
    TARGET_BRANCH="${TARGET_BRANCH_BASE}-${language}"

    # Checkout the translation branch, creating if off $SOURCE_BRANCH if it didn't already exist
    git checkout $TARGET_BRANCH || git checkout -b $TARGET_BRANCH $SOURCE_BRANCH

    # Merge if required
    git merge $SOURCE_BRANCH --quiet --no-edit

    # Delete existing translation directories
    mapped_code=$(python3 ../language_map.py ${language})
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
    python3 ../get_complete_translations.py "${language}" > "${language}_completed"

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
