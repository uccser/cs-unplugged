# Deal with SSH KEYS here
 set -e

REPO="git@github.com:jordangriffiths01/crowdin_testing.git"
CLONED_REPO_DIR="incontext-download-cloned-repo"
CROWDIN_CONFIG_FILE="crowdin_content.yaml"

if [ -d "${CLONED_REPO_DIR}" ]; then
    rm -rf "${CLONED_REPO_DIR}"
fi
git clone "${REPO}" "${CLONED_REPO_DIR}"
cd "${CLONED_REPO_DIR}"

SHA=$(git rev-parse --verify HEAD)

git config user.name "Travis CI"
git config user.email "test@test.com"

SOURCE_BRANCH="develop"
TARGET_BRANCH="develop-in-context-l10n"

git config user.name "Travis CI"
git config user.email "test@test.com"

git checkout $TARGET_BRANCH || git checkout -b $TARGET_BRANCH origin/$SOURCE_BRANCH
# Merge if required
git merge origin/$SOURCE_BRANCH --quiet --no-edit

crowdin -c "${CROWDIN_CONFIG_FILE}" download
python3 infrastructure/crowdin/download_xliff.py
python3 infrastructure/crowdin/modify_pseudo_translations.py

git add csunplugged/topics/content/xx-lr

# If there are no changes to the compiled out (e.g. this is a README update) then just bail.
if [[ $(git diff --cached) ]]; then
    git commit -m "Update in-context l10n: ${SHA}"
    git push -q origin $TARGET_BRANCH > /dev/null
fi

# If there are no changes to the compiled out (e.g. this is a README update) then just bail.
if [[ $(git diff $TARGET_BRANCH origin/$SOURCE_BRANCH) ]]; then
    hub pull-request -m "Update in-context localisation files" -b "${SOURCE_BRANCH}" -h "${TARGET_BRANCH}" || \
        echo "Could not create pull request - perhaps one already exists?"
fi
