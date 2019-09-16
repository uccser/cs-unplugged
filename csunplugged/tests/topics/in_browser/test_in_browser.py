from . import helpers
from .BaseBrowserTest import BaseBrowserTest


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
