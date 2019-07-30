import unittest

from django.test import tag
from selenium import webdriver
from . import helpers


@tag("browser")
class GlossaryTest(unittest.TestCase):
    """Test cases for using the language selector"""

    def test_binary_numbers_algorithm(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        helpers.load_page(driver, "topics/binary-numbers/unit-plan/description/")

        # Click algorithms glossary link
        # Shakey solution no.1: Finds link 'n' within paragraph 'm'
        driver.find_element_by_xpath('//*[@id="content-container"]/div/div[3]/p[5]/a[1]').click()

        # Shakey solution no.2: Finds first clickable link with text 'algorithms'
        # driver.find_element_by_link_text('algorithms')

        # Check title of popup is present and contains the correct text.
        assert(driver.find_element_by_id('glossary-modal-term').text == 'Algorithm')

        # Close driver
        driver.quit()
