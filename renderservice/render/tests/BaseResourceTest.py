"""The BaseTest case for tests to inheirit from for render tests."""
import importlib
from render.tests.BaseTest import BaseTest
from render.daemon.ResourceGenerator import ResourceGenerator


class BaseResourceTest(BaseTest):
    """A base test class for individual test classes."""

    def __init__(self, *args, **kwargs):
        """Create a Base Test.

        Create class inheiriting from TestCase, while also storing
        the path to test files and the maxiumum difference to display on
        test failures.
        """
        super(BaseResourceTest, self).__init__(*args, **kwargs)
        self.module = None

    @classmethod
    def setUpClass(cls):
        """Set up before class initialization."""
        cls.generator = ResourceGenerator()

    def load_module(self):
        """Load resource module.

        Returns:
            Module object to make calls from.
        """
        module_path = "render.resources.{}".format(self.module)
        return importlib.import_module(module_path)

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
