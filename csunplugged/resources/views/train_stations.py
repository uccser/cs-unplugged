"""Module for generating Train Stations resource."""

from PIL import Image
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource(request, resource):
    """Create a image for Train Stations resource.

    Args:
        request: HTTP request object (QueryDict).
        resource: Object of resource data (Resource).

    Returns:
        A dictionary for the resource page.
    """
    image_path = "static/img/resources/train-stations/train-stations-tracks-{}.png"

    parameter_options = valid_options()
    track_type = retrieve_query_parameter(request, "tracks", parameter_options["tracks"])
    image = Image.open(image_path.format(track_type))
    image = image.rotate(90, expand=True)
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
    return "{} tracks - {}".format(
        retrieve_query_parameter(request, "tracks"),
        retrieve_query_parameter(request, "paper_size")
    )


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "tracks": ["circular", "twisted"],
        "paper_size": ["a4", "letter"]
    }
