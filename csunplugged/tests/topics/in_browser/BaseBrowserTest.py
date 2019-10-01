"""Base test class for the in_browser test suite."""

import copy
import os
import unittest

from django.test import tag
from selenium import webdriver

from . import run_browser_tests
from . import setup_config


@tag("browser")
class BaseBrowserTest(unittest.TestCase):
    """Base test class for the in_browser test suite."""

    URL = None  # Provides the address for the load_page method.

    @classmethod
    def setUpClass(cls):
        """Call only once for entire class.

        This retrieves the browser configurations and sets as variable.
        It also removes the browserstack local key if the tests are to be run on the live site and
        the tests weren't launched by Travis.
        """
        cls.browsers = run_browser_tests.get_browsers(os.getenv('JSONFILE', 'in_browser/capabilities.json'))
        if setup_config.TEST_ON_LIVE_SITE and not setup_config.TRAVIS_LAUNCH:
            for browser_config in cls.browsers:
                del browser_config["browserstack.local"]

    def setUp(self):
        """Automatically called before each test.

        Creates the Selenium driver and sets the BrowserStack capabilities.
        """
        # Defaults to first index if local
        test_capabilities = copy.deepcopy(self.browsers[int(os.getenv('INDEX', 0))])

        test_capabilities['name'] = self._testMethodName
        self.driver = webdriver.Remote(
            command_executor=setup_config.COMMAND_EXECUTOR,
            desired_capabilities=test_capabilities)

    def tearDown(self):
        """Automatically called after each test.

        Quits the Selenium webdriver.
        """
        self.driver.quit()

    def load_page(self, arg_string="", close_dev_toolbar=True):
        """Load the page using the set url.

        Defaults to closing the toolbar, but this should be set to false for further calls.
        """
        self.driver.get(setup_config.BASE_URL + self.URL + arg_string)
        if close_dev_toolbar:
            self.hide_dev_toolbar()

    def hide_dev_toolbar(self):
        """Hide the tool bar if the test has been run in developer mode, ie it has been run locally."""
        if setup_config.BASE_URL == setup_config.LOCAL_URL:
            self.driver.find_element_by_id("djHideToolBarButton").click()
