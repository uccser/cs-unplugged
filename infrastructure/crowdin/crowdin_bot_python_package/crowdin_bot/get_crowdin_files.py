"""Script to print list of all source file paths on crowdin."""

import os
from crowdin_bot import api


def get_project_info():
    """Get xml containing all crowdin files (from api).

    Returns:
        lxml.etree object
    """
    return api.api_call_xml("info")


def process_item(item, parent_path="/"):
    """Return list of paths to all files under a given node

    Args:
        item: (etree.Element): itemm node in info xml tree
            (see https://support.crowdin.com/api/info/)
        parent_path: (str) path to the file/folder node "item".

    Returns:
        (list) list of paths of source files inside given node
    """
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
