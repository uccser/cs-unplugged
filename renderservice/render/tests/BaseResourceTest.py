"""The BaseTest case for tests to inheirit from for render tests."""
from render.tests.BaseTest import BaseTest


class BaseResourceTest(BaseTest):
    """A base test class for individual test classes."""

    def __init__(self, *args, **kwargs):
        """Create a Base Test.

        Create class inheiriting from TestCase, while also storing
        the path to test files and the maxiumum difference to display on
        test failures.
        """
        super(BaseResourceTest, self).__init__(*args, **kwargs)

    def query_string(self, values):
        """Create a GET query to append to a URL from the given values.

        Args:
            values: A dictionary of keys/values of GET parameters.

        Returns:
            String of GET query.
        """
        string = "?"
        for index, (key, value) in enumerate(values.items()):
            string += "{key}={value}".format(key=key, value=value)
            if index < len(values):
                string += "&"
        return string
