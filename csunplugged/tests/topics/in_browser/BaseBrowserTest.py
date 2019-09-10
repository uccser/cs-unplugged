import copy
import unittest
import os
from . import run_browser_tests

from django.test import tag
from selenium import webdriver

from . import helpers


@tag("browser")
class BaseBrowserTest(unittest.TestCase):
    """Base test class for the in_browser test suite."""

    @classmethod
    def setUpClass(cls):
        """ Called once for entire test suite. This retrieves the browser configurations and sets as variable."""
        cls.browsers = run_browser_tests.get_browsers(os.getenv('JSONFILE', 'in_browser/capabilities.json'))

    def setUp(self):
        """Automatically called before each test.

        Creates the Selenium driver and sets the BrowserStack capabilities.
        """
        # Defaults to first index if local
        test_capabilities = copy.deepcopy(self.browsers[int(os.getenv('INDEX', 0))])

        test_capabilities['name'] = self._testMethodName
        self.driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=test_capabilities)

    def tearDown(self):
        """Automatically called after each test.

        Quits the Selenium webdriver.
        """
        self.driver.quit()
