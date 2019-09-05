import copy
import unittest

from django.test import tag
from selenium import webdriver

from . import helpers


@tag("browser")
class BaseBrowserTest(unittest.TestCase):
    """Base test class for the in_browser test suite."""

    def setUp(self):
        """Automatically called before each test.

        Creates the Selenium driver and sets the BrowserStack capabilities.
        """

        test_capabilities = copy.deepcopy(helpers.CAPABILITIES)
        test_capabilities['name'] = self._testMethodName
        self.driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=test_capabilities)

    def tearDown(self):
        """Automatically called after each test.

        Quits the Selenium webdriver.
        """
        self.driver.quit()
