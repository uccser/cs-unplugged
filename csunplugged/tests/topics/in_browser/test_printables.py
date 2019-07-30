import unittest

from django.test import tag
from selenium import webdriver
from . import helpers


@tag("browser")
class PrintablesTest(unittest.TestCase):
    """Test cases for using the language selector"""

    def test_arrows(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        helpers.load_page(driver, "resources/")

        # Click Arrows icon
        # Potential issue if there are other links to the arrows page
        driver.find_element_by_link_text("Arrows").click()
        # Alternative is using XPath although this will change with item order
        # driver.find_element_by_link_text('//*[@id="content-container"]/div/div[2]/div/div[1]').click()

        assert(driver.title == "Arrows - CS Unplugged")
        # Close driver
        driver.quit()
