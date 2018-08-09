"""Return the name of a search index."""
from django.conf import settings

DEFAULT_SEARCH_INDEX_NAME = "default"
DEFAULT_SEARCH_INDEX_LANGUAGE = "en"

def get_search_index_name(language_code):
    """Return the name of a search index.

    Args:
        language_code (str): Django code for language.

    Returns:
        String of search index name.
    """
    if language_code == DEFAULT_SEARCH_INDEX_LANGUAGE:
        return DEFAULT_SEARCH_INDEX_NAME
    else:
        return language_code

def get_search_index_language(index_name):
    """Return the name of a search index.

    Args:
        index_name (str): Name of index.

    Returns:
        String of search index language.
    """
    if index_name == DEFAULT_SEARCH_INDEX_NAME:
        return DEFAULT_SEARCH_INDEX_LANGUAGE
    else:
        return index_name
