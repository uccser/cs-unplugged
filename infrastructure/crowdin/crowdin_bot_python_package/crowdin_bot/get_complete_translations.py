import os
import argparse

from crowdin_bot import api

SOURCE_LANGUAGE = "en"

def get_language_info(language):
    return api.api_call_xml(
        "language-status",
        language=language
    )

def process_item(item, parent_path=None, csu_language_code=None):
    if item.find("node_type").text == "file":
        filename = item.find("name").text
        if parent_path:
            path = os.path.join(parent_path, filename)
        else:
            path = filename

        # Skip full translated check for *.po - they can always be included
        if filename.endswith(".po"):
            return [path]

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
    # parser.add_argument('--crowdin-code', required=True,
    #                     help='Crowdin language code')
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
    print('\n'.join(completed))
