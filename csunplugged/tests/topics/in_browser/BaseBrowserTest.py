import unittest
import copy

from django.test import tag
from selenium import webdriver

from . import helpers


@tag("browser")
class BaseBrowserTest(unittest.TestCase):
    """ Base test class for the in_browser test suite.

        This supplies the setup of the selenium driver, its teardown, and the setting of BrowserStack test names."""

    def setUp(self):
        test_capabilities = copy.deepcopy(helpers.CAPABILITIES)
        test_capabilities['name'] = self._testMethodName
        self.driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=test_capabilities)

    def tearDown(self):
        self.driver.quit()
