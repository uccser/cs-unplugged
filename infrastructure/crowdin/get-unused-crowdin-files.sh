set -e
set -x

source config.sh
source utils.sh

CLONED_REPO_DIR="get-unused-crowdin-files-cloned-repo"

# Clone repo, deleting old clone if exists
if [ -d "${CLONED_REPO_DIR}" ]; then
    reset_repo "${CLONED_REPO_DIR}" "${TRANSLATION_SOURCE_BRANCH}"
else
    git clone "${REPO}" "${CLONED_REPO_DIR}" --branch ${TRANSLATION_SOURCE_BRANCH}
fi

cd "${CLONED_REPO_DIR}"

python3 ../get_crowdin_files.py | sort > all_crowdin_files
crowdin -c "${CROWDIN_CONFIG_FILE}" --dryrun upload | sort > current_crowdin_files

# Diff returns exit code 1 if diff found - don't abort script if that is the case
diff --new-line-format="" --unchanged-line-format="" all_crowdin_files current_crowdin_files > unused_crowdin_files || [ $? -eq 1 ]

echo "Files present on Crowdin that are unused (i.e. do not match any current english source file):"
cat unused_crowdin_files
