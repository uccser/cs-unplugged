"""Script for downloading XLIFF translation files for in-context pseudo-language."""

import os
from crowdin_bot import api
from constants import CONTENT_FOLDERS

INCONTEXT_L10N_PSEUDOLANGUAGE_CROWDIN = "en-UD"


def download_xliff(source_filename, dest_filename, language=INCONTEXT_L10N_PSEUDOLANGUAGE_CROWDIN):
    """Download xliff translation file for given source file and language.

    Args:
        source_filename: (str) Path to english source file from csunplugged root
        dest_filename: (str) Path to save xliff file
        language: (str) Crowdin language code of the translation file to download
    """
    params = {
        "file": source_filename,
        "language": language,
        "format": "xliff"
    }
    xliff_content = api.api_call_text("export-file", **params)
    xliff_content = xliff_content.replace('\x0C', '')
    with open(dest_filename, 'w') as f:
        f.write(xliff_content)


if __name__ == "__main__":
    for content_root in CONTENT_FOLDERS:
        en_dir = os.path.join(content_root, 'en')
        xliff_dir = os.path.join(content_root, 'xliff')
        if not os.path.exists(xliff_dir):
            os.mkdir(xliff_dir)
        for root, dirs, files in os.walk(en_dir):
            for name in files:
                if name.endswith(".md"):
                    source_path = os.path.join(root, name)
                    path_from_language_root = os.path.relpath(source_path, start=en_dir)
                    xliff_path = os.path.join(xliff_dir, path_from_language_root)
                    xliff_path = os.path.splitext(xliff_path)[0] + ".xliff"
                    os.makedirs(os.path.split(xliff_path)[0], exist_ok=True)
                    download_xliff(source_path, xliff_path)
