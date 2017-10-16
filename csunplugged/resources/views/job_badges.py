"""Module for generating Job Badges resource."""

from PIL import Image, ImageDraw
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource(request, resource):
    """Create a image for Job Badges resource.

    Args:
        request: HTTP request object (QueryDict).
        resource: Object of resource data (Resource).

    Returns:
        A dictionary for the resource page.
    """
    image_path = "static/img/resources/job-badges/job-badges.png"
    image = Image.open(image_path)
    ImageDraw.Draw(image)
    return {"type": "image", "data": image}


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
