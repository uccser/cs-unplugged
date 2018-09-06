"""Create test data for resource tests."""

from resources.models import Resource


class ResourcesTestDataGenerator:
    """Class for generating test data for resource tests."""

    def create_resource(self, slug, name, content, generator_module, copies=False):
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
            slug=slug,
            name=name,
            content=content,
            generator_module=generator_module,
            copies=copies,
        )
        resource.save()
        return resource
