"""Test class for CouldNotFindConfigFileError error."""

from django.test import SimpleTestCase
from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError


class CouldNotFindConfigFileErrorTest(SimpleTestCase):
    """Test class for CouldNotFindConfigFileError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        exception = CouldNotFindConfigFileError("yaml file path")
        self.assertEqual(exception.config_file_path, "yaml file path")

    def test_string(self):
        exception = CouldNotFindConfigFileError("yaml file path")
        expected_string = (
            "\n****************************ERROR****************************\n"
            "File: yaml file path\n\n"
            "Could not find config file.\n\n"
            "  - Did you spell the name of the file correctly?\n"
            "  - Does the file exist?\n"
            "  - Is the file saved in the correct directory?\n"
        )
        self.assertEqual(exception.__str__(), expected_string)
