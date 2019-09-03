from . import helpers
from .BaseBrowserTest import BaseBrowserTest


class PrintablesTest(BaseBrowserTest):
    """Test cases for using the language selector"""

    def test_arrows(self):
        helpers.load_page(self.driver, "resources/")

        # Click Arrows icon
        # Potential issue if there are other links to the arrows page
        self.driver.find_element_by_link_text("Arrows").click()
        # Alternative is using XPath although this will change with item order
        # self.driver.find_element_by_link_text('//*[@id="content-container"]/div/div[2]/div/div[1]').click()

        assert(self.driver.title == "Arrows - CS Unplugged")
