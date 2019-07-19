import unittest

from django.test import tag
from selenium import webdriver

from .helpers import *


@tag("browser")
class LanguagePickerTest(unittest.TestCase):
    """Test cases for using the language selector"""

    def test_home_page_language_selector(self):
        driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR,
            desired_capabilities=local_server)

        load_home_page(driver)
        driver.find_element_by_id("navbarLangaugeSelector").click()
        driver.find_element_by_link_text("Deutsch").click()
        lang_value = driver.find_element_by_tag_name("html").get_attribute("lang")
        if lang_value != "de":
            raise Exception("Language selector failed.\nExpected {}, got {}".format("de", lang_value))

        # Close driver
        driver.quit()
