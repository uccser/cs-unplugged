"""Test class for alphabets module."""

from config.settings.base import DEFAULT_LANGUAGES as LANGUAGES
from tests.BaseTestWithDB import BaseTestWithDB
from utils.alphabets import get_alphabet


class AlphabetsTest(BaseTestWithDB):
    """Test class for alphabets module."""

    def test_all_languages_available(self):
        # Check all available langages return alphabet
        for language_code, language_name in LANGUAGES:
            try:
                get_alphabet(language_code)
            except KeyError:
                error_message = "Alphabet missing for '{}' ({})"
                raise LookupError(error_message.format(language_code, language_name))
