"""Script to print list of file paths of all completely translated files for a given language."""

import os
import argparse

from crowdin_bot import api

SOURCE_LANGUAGE = "en"

def get_language_info(language):
    """Get xml tree from language info api call.

    Args:
        language: (str) crowdin language code

    Returns:
        lxml.etree object
    """
    return api.api_call_xml(
        "language-status",
        language=language
    )

def process_item(item, parent_path=None, csu_language_code=None):
    """Return list of completely translated file paths in a given directory tree node.

    Args:
        item: (etree.Element): itemm node in language-status xml tree
            (see https://support.crowdin.com/api/language-status/)
        parent_path: (str) path to the translated file node (None if the current item is
            the root of the directory tree).
        csu_language_code: (str) Language code (in locale format) on CSU end
            (may differ from crowdin language code according to language mapping
            in yaml file)

    Returns:
        (list) list of file paths that are completely translated
    """
    if item.find("node_type").text == "file":
        filename = item.find("name").text
        if parent_path:
            path = os.path.join(parent_path, filename)
        else:
            path = filename

        # Skip *.po - they are handled separately
        if filename.endswith(".po"):
            return []

        if item.find("phrases").text == item.find("approved").text:
            return [path]
        else:
            return []

    else:
        inner_nodes = item.find("files")
        dirname = item.find("name").text
        if dirname == SOURCE_LANGUAGE:
            dirname = csu_language_code
        if parent_path:
            path = os.path.join(parent_path, dirname)
        else:
            path = dirname
        completed = []
        for inner_node in inner_nodes:
            completed += process_item(inner_node, parent_path=path, csu_language_code=csu_language_code)
        return completed


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--crowdin-code', required=True,
                        help='Crowdin language code for target language')
    parser.add_argument('--csu-code', required=True,
                        help='CSU language code for target language')
    args = parser.parse_args()
    lang_info = get_language_info(args.crowdin_code)
    files = lang_info.find("files")
    completed = []
    for item in files:
        completed += process_item(item, csu_language_code=args.csu_code)
    for path in completed:
        print(path)
