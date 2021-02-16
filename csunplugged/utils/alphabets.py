"""Alphabets for languages."""

from string import ascii_lowercase


SPACER = " "

ALPHABETS = {
    # English
    "en": {
        "letters": list(ascii_lowercase),
    },
    # French
    "fr": {
        "letters": list(ascii_lowercase) + ["Œ", "Æ", "â", "ê", "î", "ô", "û", "ç"],
    },
    # Spanish
    "es": {
        "letters": list(ascii_lowercase) + ["ñ"],
    },
    # German,
    "de": {
        "letters": list(ascii_lowercase) + ["ä", "ö", "ü", "ß"],
    },
    # te reo Māori
    "mi": {
        "letters": [
            "a",
            "ā",
            "e",
            "ē",
            "h",
            "i",
            "ī",
            "k",
            "m",
            "n",
            "ng",
            "o",
            "ō",
            "p",
            "r",
            "t",
            "u",
            "ū",
            "w",
            "wh",
        ],
    },
    # Simplified Chinese
    "zh-hans": {
        "letters": ["─", "╱", "V", "╲"] + list(ascii_lowercase.replace("v", "ü")),
        "description": "汉语拼音",
    },
}


def get_alphabet(language_code):
    """Return the language for the given language code.

    Args:
        language_code (str): Code of language.

    Returns:
        List of strings of alphabet.
    """
    return [SPACER] + ALPHABETS[language_code]["letters"]


def get_alphabet_description(language_code):
    """Return the language description for the given language code.

    Args:
        language_code (str): Code of language.

    Returns:
        String description of alphabet.
    """
    return ALPHABETS[language_code].get("description", "")
