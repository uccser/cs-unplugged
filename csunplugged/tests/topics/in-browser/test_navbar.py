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

TITLE_ERROR_TEXT = "Failed to load page\nExpected title = {}, got {}"
URL_ERROR_TEXT = "Failed to load page\nExpected url = {}, not {}"


def check_title_and_url(driver, expected_title, expected_url):
    if driver.title != expected_title:
        raise Exception(TITLE_ERROR_TEXT.format(expected_title, driver.title))
    if driver.current_url != expected_url:
        raise Exception(URL_ERROR_TEXT.format(expected_url, driver.current_url))


def load_home_page(driver):
    driver.get("http://localhost/en")
    if driver.title != "CS Unplugged":
        raise Exception(TITLE_ERROR_TEXT.format(driver.title, "CS Unplugged"))


@tag("browser")
class NavbarTest(unittest.TestCase):
    """ Test cases for the in-browser test suite"""

    def test_navbar_loads_pages(self):
        driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR,
            desired_capabilities=local_server)

        # Home page
        load_home_page(driver)

        # Topics page
        driver.find_element_by_link_text("Topics").click()
        check_title_and_url(driver, "Topics - CS Unplugged", "http://localhost/en/topics/")

        # Printables page
        driver.find_element_by_link_text("Printables").click()
        check_title_and_url(driver, "Printables - CS Unplugged", "https://csunplugged.org/en/resources/")

        # About page
        driver.find_element_by_link_text("About").click()
        check_title_and_url(driver, "About - CS Unplugged", "https://csunplugged.org/en/about/")

        # Return to home page
        driver.find_element_by_id("navbar-brand-logo")
        check_title_and_url(driver, "CS Unplugged", "http://localhost/en")

        # Close driver
        driver.quit()
