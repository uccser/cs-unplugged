"""Test class for check_glossary_links module."""

from tests.BaseTestWithDB import BaseTestWithDB
from utils.check_glossary_links import check_converter_glossary_links
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from utils.errors.CouldNotFindGlossaryTermError import CouldNotFindGlossaryTermError


class CheckGlossaryLinksTest(BaseTestWithDB):
    """Test class for check_glossary_links module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_single_term(self):
        self.test_data.create_glossary_term(1)
        terms_to_find = {
            "term-1": [],
        }
        check_converter_glossary_links(terms_to_find, "md file path")

    def test_multiple_terms(self):
        self.test_data.create_glossary_term(1)
        self.test_data.create_glossary_term(2)
        self.test_data.create_glossary_term(3)
        self.test_data.create_glossary_term(4)
        terms_to_find = {
            "term-1": [],
            "term-2": [],
            "term-3": [],
            "term-4": [],
        }
        check_converter_glossary_links(terms_to_find, "md file path")

    def test_missing_term(self):
        self.test_data.create_glossary_term(1)
        terms_to_find = {
            "term-2": [],
        }
        self.assertRaises(
            CouldNotFindGlossaryTermError,
            check_converter_glossary_links,
            terms_to_find,
            "md file path"
        )
