"""Create test data for resource tests."""

from resources.models import Resource


class ResourcesTestDataGenerator:
    """Class for generating test data for resource tests."""

    def create_test_resource(self, slug, name, webpage_template, generation_view):
        """Create resource object.

        Args:
            slug: String of resource slug.
            name: String of resource name.
            webpage_template: String describing path to HTML form template.
            generation_view: String of Python view module filename.

        Returns:
            Resource object.
        """
        resource = Resource(
            slug="resource-{}".format(slug),
            name="Resource {}".format(name),
            webpage_template=webpage_template,
            generation_view=generation_view,
            thumbnail_static_path="static/images/thumbnail-{}".format(slug)
        )
        resource.save()
        return resource
