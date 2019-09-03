from . import helpers
from .BaseBrowserTest import BaseBrowserTest


class LanguagePickerTest(BaseBrowserTest):
    """Test cases for using the language selector"""

    def test_home_page_language_selector(self):
        helpers.load_home_page(self.driver)

        # Select German
        helpers.change_language(self.driver, 'de')

        # Select Spanish
        helpers.change_language(self.driver, 'es')

        # Select Te Reo
        helpers.change_language(self.driver, 'mi')

        # Select Chinese
        helpers.change_language(self.driver, 'zh-hans')

        # Select English
        helpers.change_language(self.driver, 'en')
