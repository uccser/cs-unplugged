import unittest

from django.test import tag
from selenium import webdriver

from . import helpers


@tag("browser")
class BrowserTest(unittest.TestCase):
    """ Test cases for the in_browser test suite"""

    def test_local_2(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        driver.get("{}resources/".format(helpers.BASE_URL))
        element = driver.title
        if "Printables" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

    def test_local(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        driver.get(helpers.BASE_URL)
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

    def test_local_dup(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        driver.get(helpers.BASE_URL)
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()
