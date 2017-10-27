"""Test all possible valid resource combinations."""

from http import HTTPStatus
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.resource_valid_configurations import resource_valid_configurations
from utils.create_query_string import query_string

CONTENT_DISPOSITION = 'attachment; filename="{name} ({subtitle}).pdf"'


def resource_test_valid_configurations(test_class, resource, base_url, subtitle_function):
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
        response = test_class.client.get(url)
        test_class.assertEqual(HTTPStatus.OK, response.status_code)
        subtitle = subtitle_function(combination)
        test_class.assertEqual(
            response.get("Content-Disposition"),
            CONTENT_DISPOSITION.format(name=resource.name, subtitle=subtitle)
        )
        print("ok")
