"""Script for downloading XLIFF translation files for in-context pseudo-language."""

import os

from crowdin_bot import api

INCONTEXT_L10N_PSEUDOLANGUAGE_CROWDIN = "en-UD"
CONTENT_ROOT = "csunplugged/topics/content"
EN_DIR = os.path.join(CONTENT_ROOT, 'en')
XLIFF_DIR = os.path.join(CONTENT_ROOT, 'xliff')


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
    if not os.path.exists(XLIFF_DIR):
        os.mkdir(XLIFF_DIR)
    for root, dirs, files in os.walk(EN_DIR):
        for name in files:
            if name.endswith(".md"):
                source_path = os.path.join(root, name)
                path_from_language_root = os.path.relpath(source_path, start=EN_DIR)
                xliff_path = os.path.join(XLIFF_DIR, path_from_language_root)
                xliff_path = os.path.splitext(xliff_path)[0] + ".xliff"
                os.makedirs(os.path.split(xliff_path)[0], exist_ok=True)
                download_xliff(source_path, xliff_path)
