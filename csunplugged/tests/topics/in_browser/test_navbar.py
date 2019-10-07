from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from .BaseBrowserTest import BaseBrowserTest
from .setup_config import BASE_URL


class NavbarTest(BaseBrowserTest):
    """ Test cases for using the navigation bar"""

    TITLE_ERROR_TEXT = "Failed to load page\nExpected title = {}, got {}"

    def check_title_and_url(self, expected_title, expected_url):
        """Check that the title and url are correct."""

        WebDriverWait(self.driver, 10).until(ec.title_is(expected_title),
                                             message=self.TITLE_ERROR_TEXT.format(expected_title, self.driver.title))

        if self.driver.current_url != expected_url:
            raise Exception(self.URL_ERROR_TEXT.format(expected_url, self.driver.current_url))

    def test_navbar_loads_pages(self):
        """Check the navigation bar switches to the correct page."""

        # Home page
        self.load_page()

        # Topics page
        self.driver.find_element_by_link_text("Topics").click()
        self.check_title_and_url("Topics - CS Unplugged", "{}topics/".format(BASE_URL))

        # Printables page
        self.driver.find_element_by_link_text("Printables").click()
        self.check_title_and_url("Printables - CS Unplugged", "{}resources/".format(BASE_URL))

        # About page
        self.driver.find_element_by_link_text("About").click()
        self.check_title_and_url("About - CS Unplugged", "{}about/".format(BASE_URL))

        # Return to home page
        self.driver.find_element_by_id("navbar-brand-logo").click()
        self.check_title_and_url("CS Unplugged", BASE_URL)
