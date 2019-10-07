from .BaseBrowserTest import BaseBrowserTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class GlossaryTest(BaseBrowserTest):
    """Test cases for checking the contents of glossary items"""

    def test_binary_numbers_algorithm_glossary(self):
        """Check async loading of glossary terms is functioning for binary numbers."""

        self.load_page("topics/binary-numbers/unit-plan/description/")

        # Click algorithms glossary link
        self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div[3]/p[5]/a[1]').click()

        # Wait for async load of glossary term.
        WebDriverWait(self.driver, 10).until(ec.text_to_be_present_in_element((By.ID, "glossary-modal-term"),
                                                                              "Algorithm"))
        # Check title of popup is present and contains the correct text.
        assert(self.driver.find_element_by_id("glossary-modal-term").text == "Algorithm")
