"""Script to print list of all crowdin language codes for project."""

from crowdin_bot import api

NS_DICT = {
    'ns': "urn:oasis:names:tc:xliff:document:1.2"
}

def get_project_languages():
    """Get list of crowdin language codes."""
    info_xml = api.api_call_xml("info")
    languages = info_xml.find('languages')
    translatable_languages = []
    for language in languages:
        # Check it's not the incontext pseudo language
        if language.find("can_translate").text == "1":
            translatable_languages.append(language.find('code').text)
    return translatable_languages

if __name__ == "__main__":
    print('\n'.join(get_project_languages()))
