# Deal with SSH KEYS here
 set -e

 REPO="git@github.com:uccser/cs-unplugged.git"
 CLONED_REPO_DIR="get-unused-crowdin-files-cloned-repo"
 SOURCE_BRANCH="develop"
 CROWDIN_CONFIG_FILE="crowdin_content.yaml"

 if [ -d "${CLONED_REPO_DIR}" ]; then
     rm -rf "${CLONED_REPO_DIR}"
 fi
 git clone "${REPO}" "${CLONED_REPO_DIR}"

 cd "${CLONED_REPO_DIR}"

git checkout "${SOURCE_BRANCH}"

python3 ../get_crowdin_files.py | sort > all_crowdin_files
crowdin -c "${CROWDIN_CONFIG_FILE}" --dryrun upload | sort > current_crowdin_files

diff --new-line-format="" --unchanged-line-format="" all_crowdin_files current_crowdin_files > unused_crowdin_files

cat unused_crowdin_files
