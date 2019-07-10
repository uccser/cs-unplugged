import unittest

from selenium import webdriver
import os
from django.test import tag

ACCESS_KEY = os.environ['KEY']
COMMAND_EXECUTOR = 'http://cseducationresea1:' + ACCESS_KEY + '@hub.browserstack.com:80/wd/hub'


v1 = {
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '60.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true',
    # 'browserstack.selenium_version': '3.5.2',
    # 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
}

v2 = {
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '61.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true',
    # 'browserstack.selenium_version': '3.5.2',
    # 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
}

v3 = {
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '62.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true',
    # 'browserstack.selenium_version': '3.5.2',
    # 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
}

local_server = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '63.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true',
    # 'browserstack.selenium_version': '3.5.2',
    # 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
}


@tag("browser")
class BrowserTest(unittest.TestCase):
    """ Test cases for the in-browser test suite"""

    # def test_local_2_test(self):
    #     driver = webdriver.Remote(
    #         command_executor=COMMAND_EXECUTOR,
    #         desired_capabilities=local_server)
    #
    #     driver.get("http://localhost/en/resources/")
    #     element = driver.title
    #     assert "Printables" in element
    #     if "Printables" not in element:
    #         raise Exception("Unable to load local page!")
    #     driver.quit()
    #
    # def test_local_3(self):
    #     driver = webdriver.Remote(
    #         command_executor=COMMAND_EXECUTOR,
    #         desired_capabilities=local_server)
    #
    #     driver.get("http://localhost/")
    #     driver.find_element_by_xpath(
    #         "(.//*[normalize-space(text()) and normalize-space(.)="
    #         "'How do I teach CS Unplugged?'])[1]/following::h2[1]").click()
    #     element = driver.title
    #     if "Topics - CS Unplugged" not in element:
    #         raise Exception("Unable to load local page!")
    #     driver.quit()

    def test_local(self):
        driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR,
            desired_capabilities=local_server)

        driver.get("http://localhost/")
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()
