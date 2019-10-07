from .BaseBrowserTest import BaseBrowserTest


class PrintablesTest(BaseBrowserTest):
    """Test cases for using the language selector"""

    URL = "resources/"

    def test_arrows(self):
        """Check arrow resource link navigates to correct page."""

        self.load_page()

        self.driver.find_element_by_link_text("Arrows").click()
        assert(self.driver.title == "Arrows - CS Unplugged")
