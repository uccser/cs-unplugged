"""Module for generating Binary Cards resource."""

from math import pi, sin, cos
from PIL import Image, ImageDraw, ImageFont
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource_image(request, resource):
    """Create a image for Binary Cards resource.

    Args:
        request: HTTP request object (QueryDict).
        resource: Object of resource data (Resource).

    Returns:
        A list of Pillow image objects.
    """
    image_path = "static/img/resources/modulo-clock/modulo-clock-{}.png"

    parameter_options = valid_options()
    modulo_number = int(retrieve_query_parameter(request, "modulo_number", parameter_options["modulo_number"]))
    image = Image.open(image_path.format(modulo_number))
    draw = ImageDraw.Draw(image)

    font_size = 150
    font_path = "static/fonts/PatrickHand-Regular.ttf"
    font = ImageFont.truetype(font_path, font_size)

    radius = 750
    x_center = image.width / 2
    y_center = image.height / 2
    # Count from the '12 oclock position'
    start_angle = pi * 1.5
    angle_between_numbers = (2 * pi) / modulo_number

    for number in range(0, modulo_number):
        text = str(number)
        angle = start_angle + (angle_between_numbers * number)
        x_coord = radius * cos(angle) + x_center
        y_coord = radius * sin(angle) + y_center
        text_width, text_height = draw.textsize(text, font=font)
        text_coord_x = x_coord - (text_width / 2)
        text_coord_y = y_coord - (text_height / 2)
        draw.text(
            (text_coord_x, text_coord_y),
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
        request: HTTP request object (QueryDict).
        resource: Object of resource data (Resource).

    Returns:
        Text for subtitle (str).
    """
    modulo_number = retrieve_query_parameter(request, "modulo_number")
    if modulo_number == 1:
        modulo_text = "empty"
    else:
        modulo_text = modulo_number
    return "{} - {}".format(
        modulo_text,
        retrieve_query_parameter(request, "paper_size")
    )


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "modulo_number": ["1", "2", "10"],
        "paper_size": ["a4", "letter"]
    }
