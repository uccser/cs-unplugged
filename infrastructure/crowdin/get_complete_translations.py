import os
import requests
from lxml import etree
import sys
from django.conf import settings
from django.utils import translation
import language_map

settings.configure()

API_KEY = os.environ["CROWDIN_API_KEY"]
API_URL = "https://api.crowdin.com/api/project/cs-unplugged/{method}"

NS_DICT = {
    'ns': "urn:oasis:names:tc:xliff:document:1.2"
}

if len(sys.argv) != 2:
    raise Exception("Usage: python3 get_completed_translations.py <crowdin language code>")

SOURCE_LANGUAGE = "en"
TARGET_LANGUAGE = sys.argv[1]

def get_language_info(language):
    params = {
        "key" : API_KEY,
        "language": language
    }
    response = requests.get(
        API_URL.format(method="language-status"),
        params=params
    )
    info = etree.fromstring(response.text.encode())
    return info


def process_item(item, parent_path=None):
    if item.find("node_type").text == "file":
        filename = item.find("name").text
        if parent_path:
            path = os.path.join(parent_path, filename)
        else:
            path = filename

        # Skip full translated check for *.po - they can always be included
        if filename.endswith(".po"):
            return [path]

        if item.find("phrases") == item.find("approved"):
            return [path]
        else:
            return []

    else:
        inner_nodes = item.find("files")
        dirname = item.find("name").text
        if dirname == SOURCE_LANGUAGE:
            dirname = language_map.from_crowdin(TARGET_LANGUAGE)
        if parent_path:
            path = os.path.join(parent_path, dirname)
        else:
            path = dirname
        completed = []
        for inner_node in inner_nodes:
            completed += process_item(inner_node, parent_path=path)
        return completed


if __name__ == "__main__":
    lang_info = get_language_info(TARGET_LANGUAGE)
    files = lang_info.find("files")
    completed = []
    for item in files:
        completed += process_item(item)
    print('\n'.join(completed))
