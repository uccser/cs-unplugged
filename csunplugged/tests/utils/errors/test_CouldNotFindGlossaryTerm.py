"""Test class for CouldNotFindGlossaryTerm error."""

from django.test import SimpleTestCase
from utils.errors.CouldNotFindGlossaryTerm import CouldNotFindGlossaryTerm


class CouldNotFindGlossaryTermTest(SimpleTestCase):
    """Test class for CouldNotFindGlossaryTerm error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        exception = CouldNotFindGlossaryTerm("term", "file path")
        self.assertEqual(exception.term, "term")
        self.assertEqual(exception.reference_file_path, "file path")

    def test_string(self):
        exception = CouldNotFindGlossaryTerm("term", "file path")
        expected_string = (
            "\n****************************ERROR****************************\n"
            "File: file path\n\n"
            "Could not find glossary term: term\n\n"
            "Options:\n"
            "  - Is the glossary term key defined in the\n"
            "    application structure file?\n"
            "  - Is the term spelt correctly?\n"
        )
        self.assertEqual(exception.__str__(), expected_string)
