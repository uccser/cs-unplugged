"""The BaseTest case for tests to inheirit from for render tests."""
from unittest import TestCase
import pkg_resources


class BaseTest(TestCase):
    """A base test class for individual test classes."""

    def __init__(self, *args, **kwargs):
        """Create a Base Test.

        Create class inheiriting from TestCase, while also storing
        the path to test files and the maxiumum difference to display on
        test failures.
        """
        super(BaseTest, self).__init__(*args, **kwargs)
        self.test_file_path = "tests/assets/{test_type}/{filename}"
        self.maxDiff = None

    def read_test_file(self, test_type, filename, strip=False):
        """Retrieve a string for a given file.

        This function reads a file from a given filename in UTF-8 encoding.

        Args:
            test_type:
            filename:
            strip:
        Returns:
            A UTF-8 encoded python string of the file contents.
        """
        file_path = self.test_file_path.format(test_type=test_type, filename=filename)
        text = pkg_resources.resource_string("render", file_path).decode("utf-8")
        if strip:
            text = text.rstrip("\r\n")
        return text
