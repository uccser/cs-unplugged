import os
import requests
from lxml import etree
import sys
import language_map

API_KEY = os.environ["CROWDIN_API_KEY"]
API_URL = "https://api.crowdin.com/api/project/cs-unplugged/{method}"

def get_project_info():
    params = {
        "key" : API_KEY,
    }
    response = requests.get(
        API_URL.format(method="info"),
        params=params
    )
    info = etree.fromstring(response.text.encode())
    return info


def process_item(item, parent_path="/"):
    if item.find("node_type").text == "file":
        filename = item.find("name").text
        path = os.path.join(parent_path, filename)
        return [path]
    else:
        inner_nodes = item.find("files")
        dirname = item.find("name").text
        path = os.path.join(parent_path, dirname)
        files = []
        for inner_node in inner_nodes:
            files += process_item(inner_node, parent_path=path)
        return files


if __name__ == "__main__":
    proj_info = get_project_info()
    files_elem = proj_info.find("files")
    file_paths = []
    for item in files_elem:
        file_paths += process_item(item)
    print('\n'.join(file_paths))
