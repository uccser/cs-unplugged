import unittest

from django.test import tag
from selenium import webdriver
from . import helpers


@tag("browser")
class LanguagePickerTest(unittest.TestCase):
    """Test cases for using the language selector"""

    def test_home_page_language_selector(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        helpers.load_home_page(driver)

        # Select German
        helpers.change_language(driver, 'de')

        # Select Spanish
        helpers.change_language(driver, 'es')

        # Select Te Reo
        helpers.change_language(driver, 'mi')

        # Select Chinese
        helpers.change_language(driver, 'zh-hans')

        # Select English
        helpers.change_language(driver, 'en')

        # Close driver
        driver.quit()
