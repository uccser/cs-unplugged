import pytest

from . import helpers
from .BaseBrowserTest import BaseBrowserTest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    item.cls._item = item
    yield


@pytest.mark.parametrize("caps", [helpers.CAPABILITIES, helpers.DEV_TESTING_PARAMETERIZATION_TEST_CAPABILITIES])
class BrowserTest(BaseBrowserTest):
    """ Test cases for the in_browser test suite"""

    def test_local(self):
        self.driver.get(helpers.BASE_URL)
        element = self.driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")

    def test_local_2(self):
        self.driver.get(helpers.BASE_URL)
        element = self.driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")

    def test_local_3(self):
        self.driver.get("{}resources/".format(helpers.BASE_URL))
        element = self.driver.title
        if "Printables" not in element:
            raise Exception("Unable to load local page!")
