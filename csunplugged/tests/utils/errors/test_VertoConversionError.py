"""Test class for VertoConversionError error."""

from django.test import SimpleTestCase
from utils.errors.VertoConversionError import VertoConversionError
from unittest.mock import Mock


class VertoConversionErrorTest(SimpleTestCase):
    """Test class for VertoConversionError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        verto_error = Mock()
        verto_error.message = "Message."
        verto_error.line_nums = (2, 3, 4)
        verto_error.lines = ("", "{panel}", "Panel contents")
        exception = VertoConversionError("md file path", verto_error)
        self.assertEqual(exception.markdown_path, "md file path")
        self.assertEqual(exception.verto_error, verto_error)

    def test_string_without_line_nums(self):
        verto_error = Mock()
        verto_error.message = "Message."
        del verto_error.line_nums
        del verto_error.lines
        exception = VertoConversionError("md file path", verto_error)
        expected_string = (
            "\n****************************ERROR****************************\n"
            "File: md file path\n\n"
            "Conversion failed with error: \"Message.\"\n"
        )
        self.assertEqual(exception.__str__(), expected_string)

    def test_string_with_line_nums(self):
        verto_error = Mock()
        verto_error.message = "Message."
        verto_error.line_nums = (2, 3, 4)
        verto_error.lines = ("", "{panel}", "Panel contents")
        exception = VertoConversionError("md file path", verto_error)
        expected_string = (
            "\n****************************ERROR****************************\n"
            "File: md file path\n\n"
            "Conversion failed with error: \"Message.\"\n"
            "2     \n"
            "3     {panel}\n"
            "4     Panel contents\n"
        )
        self.assertEqual(exception.__str__(), expected_string)
