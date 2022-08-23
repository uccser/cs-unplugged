"""Functions for getting a thumbnail for a resource."""

from os.path import join
from django.conf import settings
from django.utils.translation import get_language
from resources.utils.get_resource_generator import get_resource_generator
from utils.bool_to_yes_no import bool_to_yes_no


def get_thumbnail_filename(resource_slug, selected_options):
    """Create thumbnail filename for a given resource and options.

    Args:
        resource_slug (str): Slug of resource to create thumbnail for.
        selected_options (dict): Dictionary of option IDs to selected values.
    """
    filename = resource_slug + "-"
    for (key, value) in sorted(selected_options.items()):
        filename += "{}-{}-".format(key, bool_to_yes_no(value))
    filename = "{}.png".format(filename[:-1])
    return filename


def get_thumbnail_base(resource_slug):
    """Return base thumbnail path for a given resource.

    Preview shows English version if in local development or
    viewing in-context language.

    Args:
        resource_slug (str): Slug of resource to create base path for.

    Returns:
        String of thumbnail base.
    """
    if settings.DEPLOYED:
        resource_language = get_language()
    else:
        resource_language = "en"
    resource_thumbnail_base = join(
        settings.STATIC_URL,
        "img/resources/",
        resource_slug,
        "thumbnails",
        resource_language,
        ""
    )
    return resource_thumbnail_base


def get_thumbnail_static_path_for_resource(resource):
    """Return static path to thumbnail for resource.

    Args:
        resource (Resource): Resource to get thumbnail for.

    Returns:
        String of static path to thumbnail.
    """
    generator = get_resource_generator(resource.generator_module)
    thumbnail = join(
        get_thumbnail_base(resource.slug),
        get_thumbnail_filename(resource.slug, generator.get_option_defaults())
    )
    return thumbnail
