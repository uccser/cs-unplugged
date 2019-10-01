from .BaseBrowserTest import BaseBrowserTest


class DetailsElementTest(BaseBrowserTest):
    """Test cases for accessing details elements"""

    URL = "topics/binary-numbers/unit-plan/"

    def test_binary_numbers_unit_plan(self):
        """Check the details element can be opened in the binary numbers unit plan."""
        self.load_page()

        element = self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details/div')
        assert(not element.is_displayed())

        self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details').click()

        element = self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details/div')
        assert(element.is_displayed())
