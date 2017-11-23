"""Test class for str_to_bool module."""

from django.test import SimpleTestCase
from utils.str_to_bool import str_to_bool


class StrToBoolTest(SimpleTestCase):
    """Test class for str_to_bool module."""

    def test_true(self):
        self.assertTrue(str_to_bool("True"))

    def test_false(self):
        self.assertFalse(str_to_bool("False"))

    def test_yes(self):
        self.assertTrue(str_to_bool("yes"))

    def test_no(self):
        self.assertFalse(str_to_bool("no"))

    def test_other_value(self):
        self.assertEqual(
            str_to_bool("example"),
            "example"
        )

    def test_other_value_invalid_flag(self):
        self.assertRaises(
            ValueError,
            str_to_bool,
            "example",
            True
        )
