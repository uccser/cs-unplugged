# Deal with SSH KEYS here
 set -e

REPO="git@github.com:uccser/cs-unplugged.git"
CLONED_REPO_DIR="source-upload-cloned-repo"
SOURCE_BRANCH="develop"
CROWDIN_CONFIG_FILE="crowdin_content.yaml"

if [ -d "${CLONED_REPO_DIR}" ]; then
    rm -rf "${CLONED_REPO_DIR}"
fi
git clone "${REPO}" "${CLONED_REPO_DIR}"

cd "${CLONED_REPO_DIR}"

git checkout "${SOURCE_BRANCH}"

crowdin upload -c "${CROWDIN_CONFIG_FILE}"
