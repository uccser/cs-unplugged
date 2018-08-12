"""Alphabets for languages."""

from string import ascii_lowercase


SPACER = " "

ALPHABETS = {
    # English
    "en": list(ascii_lowercase),
    # German,
    "de": list(ascii_lowercase) + ["ä", "ö", "ü", "ß"],
    # te reo Māori
    "mi": [
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
    ]
}


def get_alphabet(language_code):
    """Return the language for the given language code.

    Args:
        language_code (str): Code of language.

    Returns:
        List of strings of alphabet.
    """
    return [SPACER] + ALPHABETS.get(language_code)
