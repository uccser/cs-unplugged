import os
import unittest

from django.test import tag
from selenium import webdriver

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
    """ Test cases for the in_browser test suite"""

    def test_local_2(self):
        driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR,
            desired_capabilities=local_server)

        driver.get("http://localhost/en/resources/")
        element = driver.title
        if "Printables" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

    def test_local(self):
        driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR,
            desired_capabilities=local_server)

        driver.get("http://localhost/")
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

    def test_local_dup(self):
        driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR,
            desired_capabilities=local_server)

        driver.get("http://localhost/")
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()
