import unittest

from django.test import tag
from selenium import webdriver

from .helpers import *


@tag("browser")
class NavbarTest(unittest.TestCase):
    """ Test cases for using the navigation bar"""

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
        check_title_and_url(driver, "Printables - CS Unplugged", "http://localhost/en/resources/")

        # About page
        driver.find_element_by_link_text("About").click()
        check_title_and_url(driver, "About - CS Unplugged", "http://localhost/en/about/")

        # Return to home page
        driver.find_element_by_id("navbar-brand-logo")
        check_title_and_url(driver, "CS Unplugged", "http://localhost/en")

        # Close driver
        driver.quit()
