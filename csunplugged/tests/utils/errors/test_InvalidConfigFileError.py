"""Test class for InvalidConfigFileError error."""

from django.test import SimpleTestCase
from utils.errors.InvalidConfigFileError import InvalidConfigFileError


class InvalidConfigFileErrorTest(SimpleTestCase):
    """Test class for InvalidConfigFileError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        exception = InvalidConfigFileError("yaml file path")
        self.assertEqual(exception.yaml_file_path, "yaml file path")

    def test_string(self):
        exception = InvalidConfigFileError("yaml file path")
        expected_string = (
            "\n****************************ERROR****************************\n"
            "File: yaml file path\n\n"
            "Invalid configuration file.\n\n"
            "Options:\n"
            "  - Does the file match the expected layout?\n"
            "  - Does the file contain at least one key:value pair?\n"
            "  - Is the syntax correct? (are you missing a colon somewhere?)\n"
        )
        self.assertEqual(exception.__str__(), expected_string)
