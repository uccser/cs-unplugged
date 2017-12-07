"""Script to print list of all crowdin language codes for project."""

from crowdin_bot import api

NS_DICT = {
    'ns': "urn:oasis:names:tc:xliff:document:1.2"
}

def get_project_languages():
    """Get list of crowdin language codes.

    Returns:
        (list) list of project crowdin language codes
    """
    active_languages = []
    trans_status = api.api_call_json("status")
    for language in trans_status:
        # Check language has actually had some translation done
        if int(language["words_approved"]) > 0:
            active_languages.append(language["code"])
    return active_languages

if __name__ == "__main__":
    for language in get_project_languages():
        print(language)
