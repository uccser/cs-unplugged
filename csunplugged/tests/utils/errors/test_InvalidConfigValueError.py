"""Test class for InvalidConfigValueError error."""

from django.test import SimpleTestCase
from utils.errors.InvalidConfigValueError import InvalidConfigValueError


class InvalidConfigValueErrorTest(SimpleTestCase):
    """Test class for InvalidConfigValueError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used (for
          example: topic loaders).
    """

    def test_invalid_config_value_error_attributes(self):
        exception = InvalidConfigValueError(
            "yaml file path",
            "key",
            "expected"
        )
        self.assertEqual(exception.yaml_file_path, "yaml file path")
        self.assertEqual(exception.key, "key")
        self.assertEqual(exception.expected, "expected")

    def test_invalid_config_value_error_string(self):
        exception = InvalidConfigValueError(
            "yaml file path",
            "key",
            "expected"
        )
        expected_string = (
            "\n****************************ERROR****************************\n"
            "File: yaml file path\n\n"
            "Invalid configuration file value for: key\n\n"
            "Expected: expected\n"
        )
        self.assertEqual(exception.__str__(), expected_string)
