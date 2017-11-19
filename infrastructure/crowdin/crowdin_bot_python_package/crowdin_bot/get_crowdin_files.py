import os
from crowdin_bot import api


def get_project_info():
    return api.api_call_xml("info")


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
