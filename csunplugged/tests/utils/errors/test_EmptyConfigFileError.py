"""Test class for EmptyConfigFileError error."""

from django.test import SimpleTestCase
from utils.errors.EmptyConfigFileError import EmptyConfigFileError


class EmptyConfigFileErrorTest(SimpleTestCase):
    """Test class for EmptyConfigFileError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        exception = EmptyConfigFileError("yaml file path")
        self.assertEqual(exception.yaml_file_path, "yaml file path")

    def test_string(self):
        exception = EmptyConfigFileError("yaml file path")
        expected_string = (
            "\n****************************ERROR****************************\n"
            "File: yaml file path\n\n"
            "A config file cannot be empty.\n"
        )
        self.assertEqual(exception.__str__(), expected_string)
