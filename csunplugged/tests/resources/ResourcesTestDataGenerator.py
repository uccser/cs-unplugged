"""Create test data for resource tests."""

from resources.models import Resource


class ResourcesTestDataGenerator:
    """Class for generating test data for resource tests."""

    def create_resource(self, slug, name, content, generator_module, thumbnail=True, copies=False):
        """Create resource object.

        Args:
            slug: Resource slug (str).
            name: Resource name (str).
            webpage_template: Path to HTML form template (str).
            generator_module: Resource generator class filename (str).

        Returns:
            Resource object.
        """
        resource = Resource(
            slug="resource-{}".format(slug),
            name="Resource {}".format(name),
            content=content,
            generator_module=generator_module,
            copies=copies,
        )
        if thumbnail:
            resource.thumbnail_static_path = "static/images/thumbnail-{}".format(slug)
        resource.save()
        return resource
