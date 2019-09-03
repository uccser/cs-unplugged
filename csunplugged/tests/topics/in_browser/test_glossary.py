from . import helpers
from .BaseBrowserTest import BaseBrowserTest


class GlossaryTest(BaseBrowserTest):
    """Test cases for checking the contents of glossary items"""

    def test_binary_numbers_algorithm(self):
        helpers.load_page(self.driver, "topics/binary-numbers/unit-plan/description/")

        # Click algorithms glossary link
        # Shakey solution no.1: Finds link 'n' within paragraph 'm'
        self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div[3]/p[5]/a[1]').click()

        # Shakey solution no.2: Finds first clickable link with text 'algorithms'
        # self.driver.find_element_by_link_text('algorithms')

        # Check title of popup is present and contains the correct text.
        assert(self.driver.find_element_by_id('glossary-modal-term').text == 'Algorithm')
