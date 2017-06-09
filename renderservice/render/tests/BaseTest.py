"""The BaseTest case for tests to inheirit from for render tests."""
from unittest import TestCase


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
