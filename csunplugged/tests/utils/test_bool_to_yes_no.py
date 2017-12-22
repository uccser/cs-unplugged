"""Test class for bool_to_yes_no module."""

from django.test import SimpleTestCase
from utils.bool_to_yes_no import bool_to_yes_no


class BoolToYesNoTest(SimpleTestCase):
    """Test class for bool_to_yes_no module."""

    def test_true(self):
        self.assertEqual(
            bool_to_yes_no(True),
            "yes"
        )

    def test_false(self):
        self.assertEqual(
            bool_to_yes_no(False),
            "no"
        )

    def test_non_boolean_value(self):
        self.assertEqual(
            bool_to_yes_no("example"),
            "example"
        )

    def test_non_boolean_value_invalid_flag(self):
        self.assertRaises(
            ValueError,
            bool_to_yes_no,
            "example",
            True
        )
