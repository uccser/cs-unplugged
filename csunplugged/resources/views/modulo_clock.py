"""Module for generating Binary Cards resource."""

import os.path
from PIL import Image, ImageDraw, ImageFont
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource_image(request, resource):
    """Create a image for Binary Cards resource.

    Args:
        request: HTTP request object.
        resource: Object of resource data.

    Returns:
        A list of Pillow image objects.
    """
    pass


def subtitle(request, resource):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        request: HTTP request object
        resource: Object of resource data.

    Returns:
        text for subtitle (string)
    """
    pass


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    pass
