from . import helpers
from .BaseBrowserTest import BaseBrowserTest


class DetailsElementTest(BaseBrowserTest):
    """Test cases for accessing details elements"""

    def test_binary_numbers_unit_plan(self):

        helpers.load_page(self.driver, 'topics/binary-numbers/unit-plan/')

        element = self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details/div')
        assert(not element.is_displayed())

        self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details').click()

        element = self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div[2]/details/div')
        assert(element.is_displayed())
