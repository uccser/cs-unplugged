from .BaseBrowserTest import BaseBrowserTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class LanguagePickerTest(BaseBrowserTest):
    """Test cases for using the language selector"""

    LANG_SELECTOR_ERROR_TEXT = "Language selector failed.\nExpected {}, got {}"

    LANGUAGE_DICT = {
        'en': 'English',
        'de': 'Deutsch',
        'es': 'Español',
        'mi': 'Te Reo Māori',
        'zh-hans': '简体中文'
    }

    def change_language(self, lang_code):
        """Change the language to the language code given."""
        self.driver.find_element_by_id("navbarLanguageSelector").click()
        self.driver.find_element_by_link_text(self.LANGUAGE_DICT[lang_code]).click()
        # lang_value = self.driver.find_element_by_tag_name("html").get_attribute("lang")
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, "html[lang='{}']".format(lang_code))))
        # if lang_value != lang_code:
        #     raise Exception(self.LANG_SELECTOR_ERROR_TEXT.format(lang_code, lang_value))

    def test_home_page_language_selector(self):
        """Check all language selector options change the homepage HTML lang attribute."""

        self.load_page()

        # Select German
        self.change_language('de')

        # Select Spanish
        self.change_language('es')

        # Select Te Reo
        self.change_language('mi')

        # Select Chinese
        self.change_language('zh-hans')

        # Select English
        self.change_language('en')
