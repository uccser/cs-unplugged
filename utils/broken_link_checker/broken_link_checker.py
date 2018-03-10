"""Check files for broken links."""

import os
import re
import sys
import requests

# Exclude folders from search
# Must start with './' and not end in '/' to match output of os.path.join
EXCLUDE_FOLDERS = (
    "./.git",
    "./docs/build",
    "./docs/build",
    "./csunplugged/build",
    "./csunplugged/node_modules",
    "./csunplugged/staticfiles",
    "./csunplugged/temp",
    "./csunplugged/utils/custom_converter_templates",
)

# Only check files with these file extensions
CHECK_FILE_EXTENSIONS = (
    ".html",
    ".md",
    ".rst",
)

# This isn't a perfect URL matcher, but should catch the large majority of
# URLs within this project.
URL_REGEX = r'\bhttps?://[^\ \"\'\)\]\>\`\s]+'


if __name__ == "__main__":
    file_count = 0
    url_count = 0
    url_status_counts = {}
    broken_urls = set()

    for directory_root, directories, files in os.walk("."):
        # Remove directories in exclude list
        processed_directories = []
        for directory in directories:
            if os.path.join(directory_root, directory) not in EXCLUDE_FOLDERS:
                processed_directories.append(directory)
        directories[:] = processed_directories

        for filename in files:
            if filename.endswith(CHECK_FILE_EXTENSIONS):
                file_path = os.path.join(directory_root, filename)
                file_count += 1
                print("Checking file {} for URLs... ".format(file_path), end="")
                file_object = open(file_path, "r")
                file_contents = file_object.read()
                file_object.close()
                urls = re.findall(URL_REGEX, file_contents)
                print("{} URL{} found".format(len(urls), "s" if len(urls) != 1 else ""))
                for url in urls:
                    url_count += 1
                    print("  {}) Checking URL {} ".format(url_count, url), end="")
                    response = requests.head(url)
                    # If response doesn't allow HEAD request, try GET request
                    if response.status_code >= 400:
                        response = requests.get(url)
                    print("= {} status".format(response.status_code))
                    url_status_counts[response.status_code] = url_status_counts.get(response.status_code, 0) + 1
                    if response.status_code >= 400:
                        broken_urls.add(url)

    print("\n=============================================")
    print("SUMMARY")
    print("=============================================")
    print("{} file{} checked".format(file_count, "s" if file_count != 1 else ""))
    print("{} URL{} found".format(url_count, "s" if url_count != 1 else ""))

    print("\nStatus code counts")
    print("---------------------------------------------")
    for status in sorted(url_status_counts.keys()):
        print("{}: {}".format(status, url_status_counts[status]))

    print("\nBroken links:")
    print("---------------------------------------------")
    if broken_urls:
        for url in broken_urls:
            print(url)
        sys.exit(1)
    else:
        print("No broken links found!")
        sys.exit(0)
