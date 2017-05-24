"""Module for generating Binary Cards resource."""

from math import pi, sin, cos
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
    parameter_options = valid_options()
    modulo_number = int(retrieve_query_parameter(request, "modulo_number", parameter_options["modulo_number"]))
    if modulo_number == 2:
        image_path = "static/img/resources/modulo-clock/modulo-clock-2.png"
    elif modulo_number == 10:
        image_path = "static/img/resources/modulo-clock/modulo-clock-10.png"
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font_size = 150
    font_path = "static/fonts/PatrickHand-Regular.ttf"
    font = ImageFont.truetype(font_path, font_size)

    x_offset = 75
    y_offset = 225
    radius = 750
    x_center = (image.width - x_offset)/2
    y_center = (image.height - y_offset)/2
    start_angle = (2 * pi) / modulo_number

    for num in range(0, modulo_number):

        text = str(num)

        angle = start_angle * (num - 2.5)
        x_coord = radius * cos(angle) + x_center
        y_coord = radius * sin(angle) + y_center

        draw.text(
            (x_coord, y_coord),
            text,
            font=font,
            fill="#000"
        )

    return image


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
    text = "{} - {}".format(
        retrieve_query_parameter(request, "modulo_number"),
        retrieve_query_parameter(request, "paper_size")
    )
    return text


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "modulo_number": ["2", "10"],
        "paper_size": ["a4", "letter"]
    }
