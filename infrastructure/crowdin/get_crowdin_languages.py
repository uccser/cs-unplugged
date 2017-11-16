import os
import requests
from lxml import etree

API_KEY = os.environ["CROWDIN_API_KEY"]
API_URL = "https://api.crowdin.com/api/project/cs-unplugged/{method}"

NS_DICT = {
    'ns': "urn:oasis:names:tc:xliff:document:1.2"
}

def get_project_languages():
    params = {
        "key" : API_KEY,
    }
    response = requests.get(
        API_URL.format(method="info"),
        params=params
    )
    info = etree.fromstring(response.text.encode())
    languages = info.find('languages')
    translatable_languages = []
    for language in languages:
        # Check it's not the incontext pseudo language
        if language.find("can_translate").text == "1":
            translatable_languages.append(language.find('code').text)
    return translatable_languages

if __name__ == "__main__":
    print('\n'.join(get_project_languages()))
