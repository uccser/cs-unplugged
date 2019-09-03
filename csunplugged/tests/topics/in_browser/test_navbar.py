from . import helpers
from .BaseBrowserTest import BaseBrowserTest


class NavbarTest(BaseBrowserTest):
    """ Test cases for using the navigation bar"""

    def test_navbar_loads_pages(self):

        # Home page
        helpers.load_home_page(self.driver)

        # Topics page
        self.driver.find_element_by_link_text("Topics").click()
        helpers.check_title_and_url(self.driver, "Topics - CS Unplugged", "{}topics/".format(helpers.BASE_URL))

        # Printables page
        self.driver.find_element_by_link_text("Printables").click()
        helpers.check_title_and_url(self.driver, "Printables - CS Unplugged", "{}resources/".format(helpers.BASE_URL))

        # About page
        self.driver.find_element_by_link_text("About").click()
        helpers.check_title_and_url(self.driver, "About - CS Unplugged", "{}about/".format(helpers.BASE_URL))

        # Return to home page
        self.driver.find_element_by_id("navbar-brand-logo").click()
        helpers.check_title_and_url(self.driver, "CS Unplugged", helpers.BASE_URL)
