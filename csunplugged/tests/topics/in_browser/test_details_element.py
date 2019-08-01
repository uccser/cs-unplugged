import unittest

from django.test import tag
from selenium import webdriver

from . import helpers


@tag("browser")
class DetailsElementTest(unittest.TestCase):
    """Test cases for using the language selector"""

    def test_binary_numbers_unit_plan(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        helpers.load_page(driver, 'topics/binary-numbers/unit-plan/')

        element = driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details/div')
        assert(not element.is_displayed())

        driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details').click()

        element = driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details/div')
        assert(element.is_displayed())

        # Close driver
        driver.quit()
