from django.conf import settings

def get_available_languages():
    return [code for code, name in settings.LANGUAGES]

def get_default_language():
    return settings.LANGUAGE_CODE
