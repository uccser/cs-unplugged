"""Test class for testing resource views."""

from http import HTTPStatus
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.resource_valid_configurations import resource_valid_configurations
from utils.create_query_string import query_string
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


class ResourceViewBaseTest(BaseTestWithDB):
    """Test class for testing resource views."""

    CONTENT_DISPOSITION = 'attachment; filename="{name} ({subtitle}).pdf"'

    def __init__(self, *args, **kwargs):
        """Create the BaseTest object by calling the parent's constructor."""
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()

    def run_valid_configuration_tests(self, resource, base_url):
        """Test all possible valid resource combinations.

        Args:
            resource: Resource object to be tested (Resource).
            base_url: URL to send query to (str).
        """
        empty_generator = get_resource_generator(resource.generator_module)
        combinations = resource_valid_configurations(
            empty_generator.valid_options
        )
        print()
        for combination in combinations:
            print("   - Testing combination: {} ... ".format(combination), end="")
            url = base_url + query_string(combination)
            response = self.client.get(url)
            self.assertEqual(HTTPStatus.OK, response.status_code)
            subtitle = self.subtitle(combination)
            self.assertEqual(
                response.get("Content-Disposition"),
                self.CONTENT_DISPOSITION.format(name=resource.name, subtitle=subtitle)
            )
            print("ok")

    def subtitle(self, combination):
        """Return text of subtitle for given combination.

        Args:
            combination (dict): Dictionary of a valid combination

        Returns:
            String of subtitle.
        """
        raise NotImplementedError
