"""Create test data for resource tests."""

from resources.models import Resource


class ResourcesTestDataGenerator:
    """Class for generating test data for resource tests."""

    def create_test_resource(self, slug, name, webpage_template, generation_view):
        """Create resource object.

        Args:
            slug: Resource slug (str).
            name: Resource name (str).
            webpage_template: Path to HTML form template (str).
            generation_view: Python view module filename (str).

        Returns:
            Resource object.
        """
        resource = Resource(
            slug="resource-{}".format(slug),
            name="Resource {}".format(name),
            webpage_template=webpage_template,
            generation_view=generation_view,
            thumbnail_static_path="static/images/thumbnail-{}".format(slug),
            copies=False,
        )
        resource.save()
        return resource
