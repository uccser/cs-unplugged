import unittest

from django.test import tag
from selenium import webdriver

from . import helpers


@tag("browser")
class NavbarTest(unittest.TestCase):
    """ Test cases for using the navigation bar"""

    def test_navbar_loads_pages(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        # Home page
        helpers.load_home_page(driver)

        # Topics page
        driver.find_element_by_link_text("Topics").click()
        helpers.check_title_and_url(driver, "Topics - CS Unplugged", "{}topics/".format(helpers.BASE_URL))

        # Printables page
        driver.find_element_by_link_text("Printables").click()
        helpers.check_title_and_url(driver, "Printables - CS Unplugged", "{}resources/".format(helpers.BASE_URL))

        # About page
        driver.find_element_by_link_text("About").click()
        helpers.check_title_and_url(driver, "About - CS Unplugged", "{}about/".format(helpers.BASE_URL))

        # Return to home page
        driver.find_element_by_id("navbar-brand-logo").click()
        helpers.check_title_and_url(driver, "CS Unplugged", helpers.BASE_URL)

        # Close driver
        driver.quit()
