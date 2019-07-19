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
            desired_capabilities=helpers.local_server)

        helpers.load_home_page(driver)
        driver.find_element_by_id("navbarLangaugeSelector").click()
        driver.find_element_by_link_text("Deutsch").click()
        lang_value = driver.find_element_by_tag_name("html").get_attribute("lang")
        if lang_value != "de":
            raise Exception("Language selector failed.\nExpected {}, got {}".format("de", lang_value))

        # Close driver
        driver.quit()
