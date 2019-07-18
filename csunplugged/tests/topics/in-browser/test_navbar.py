import os
import unittest

from django.test import tag
from selenium import webdriver

ACCESS_KEY = os.environ['KEY']
COMMAND_EXECUTOR = 'http://cseducationresea1:' + ACCESS_KEY + '@hub.browserstack.com:80/wd/hub'

local_server = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '63.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true'
}


@tag("browser")
class NavbarTests(unittest.TestCase):
    """ Test cases for the in-browser test suite"""

    def test_navbar_loads_pages(self):
        driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR,
            desired_capabilities=local_server)

        # Loading home page
        driver.get("http://localhost/en")
        if driver.title != "CS Unplugged":
            raise Exception("Failed to load homepage\nCurrent title = {}, not {}".format(driver.title, "CS Unplugged"))
        if driver.current_url != "localhost/en/":
            raise Exception("Failed to load homepage\nCurrent url = {}, not {}".format(driver.current_url,
                                                                                       "localhost/en/"))
        # Load topics page
        driver.find_element_by_link_text("Topics").click()
        if driver.title != "CS Unplugged":
            raise Exception(
                "Failed to load Topics page\nCurrent title = {}, not {}".format(driver.title, "CS Unplugged"))
        if driver.current_url != "localhost/en/":
            raise Exception("Failed to load Topics page\nCurrent url = {}, not {}".format(driver.current_url,
                                                                                          "localhost/en/"))
        driver.quit()
