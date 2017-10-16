"""Module for generating Barcode Checksum Poster resource."""

from PIL import Image
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource(request, resource):
    """Create a image for Barcode Checksum Poster resource.

    Args:
        request: HTTP request object (QueryDict).
        resource: Object of resource data (Resource).

    Returns:
        A dictionary for the resource page.
    """
    # Retrieve parameters
    parameter_options = valid_options()
    barcode_length = retrieve_query_parameter(request, "barcode_length", parameter_options["barcode_length"])

    image_path = "static/img/resources/barcode-checksum-poster/{}-digits.png"
    image = Image.open(image_path.format(barcode_length))
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
    barcode_length = retrieve_query_parameter(request, "barcode_length")
    paper_size = retrieve_query_parameter(request, "paper_size")
    return "{} digits - {}".format(barcode_length, paper_size)


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "barcode_length": ["12", "13"],
        "paper_size": ["a4", "letter"],
    }
