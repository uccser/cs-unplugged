import os
import requests
import csunplugged
from csunplugged.config.settings.base import INCONTEXT_L10N_PSEUDOLANGUAGE

INCONTEXT_L10N_PSEUDOLANGUAGE_CROWDIN = "en-UD"
API_KEY = os.environ["CROWDIN_API_KEY"]
API_URL = "https://api.crowdin.com/api/project/cs-unplugged/{method}"

CONTENT_ROOT = "csunplugged/topics/content"
EN_DIR = os.path.join(CONTENT_ROOT, 'en')
XLIFF_DIR = os.path.join(CONTENT_ROOT, 'xliff')


def download_xliff(source_filename, dest_filename, language=INCONTEXT_L10N_PSEUDOLANGUAGE_CROWDIN):
    params = {
        "key" : API_KEY,
        "file": source_filename,
        "language": language,
        "format": "xliff"
    }
    response = requests.get(
        API_URL.format(method="export-file"),
        params=params
    )
    print("Downloading {}".format(response.url))
    xliff_text = response.text.replace('\x0C', '')
    with open(dest_filename, 'w') as f:
        f.write(xliff_text)

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
                # path = os.path.join(root, name)
                # xliff_path = os.path.splitext(path)[0] + ".xliff"
                download_xliff(source_path, xliff_path)
