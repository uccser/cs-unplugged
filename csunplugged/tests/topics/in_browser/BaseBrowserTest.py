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
        cls.browsers = run_browser_tests.get_browsers(os.getenv('JSONFILE', 'in_browser/capabilities.json'))

    def setUp(self):
        """Automatically called before each test.

        Creates the Selenium driver and sets the BrowserStack capabilities.
        """
        test_capabilities = copy.deepcopy(self.browsers[int(os.getenv('INDEX', None))])
        # test_capabilities = helpers.CAP_MAP.get("environments").get(cap_key)

        test_capabilities['name'] = self._testMethodName
        self.driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=test_capabilities)

    def tearDown(self):
        """Automatically called after each test.

        Quits the Selenium webdriver.
        """
        self.driver.quit()
