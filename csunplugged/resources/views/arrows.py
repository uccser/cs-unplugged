"""Module for generating Arrows resource."""

from PIL import Image, ImageDraw
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource_image(request, resource):
    """Create a image for Arrows resource.

    Args:
        request: HTTP request object (QueryDict).
        resource: Object of resource data (Resource).

    Returns:
        A list of Pillow image objects.
    """
    image_path = "static/img/resources/arrows/arrows.png"
    image = Image.open(image_path)
    ImageDraw.Draw(image)

    return image


def subtitle(request, resource):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        request: HTTP request object (QueryDict).
        resource: Object of resource data (Resource).

    Returns:
        Text for subtitle (str).
    """
    return retrieve_query_parameter(request, "paper_size")


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "paper_size": ["a4", "letter"]
    }
