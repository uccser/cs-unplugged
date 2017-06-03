"""Module for generating Sorting Network resource."""

from PIL import Image, ImageDraw, ImageFont
from random import sample
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource_image(request, resource):
    """Create a image for Sorting Network resource.

    Args:
        request: HTTP request object
        resource: Object of resource data.

    Returns:
        A Pillow image object.
    """
    image_path = "static/img/resources/resource-sorting-network-colour.png"
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    (range_min, range_max, font_size) = number_range(request)

    font_path = "static/fonts/PatrickHand-Regular.ttf"

    # Add numbers to text if needed
    parameter_options = valid_options()
    prefilled_values = retrieve_query_parameter(request, "prefilled_values", parameter_options["prefilled_values"])
    if prefilled_values != "blank":
        font = ImageFont.truetype(font_path, font_size)
        numbers = sample(range(range_min, range_max), 6)
        base_coord_x = 70
        base_coord_y = 2560
        coord_x_increment = 204
        for number in numbers:
            text = str(number)
            text_width, text_height = draw.textsize(text, font=font)
            coord_x = base_coord_x - (text_width / 2)
            coord_y = base_coord_y - (text_height / 2)
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill="#000"
            )
            base_coord_x += coord_x_increment

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
    prefilled_values = retrieve_query_parameter(request, "prefilled_values")
    if prefilled_values == "blank":
        range_text = "blank"
    else:
        SUBTITLE_TEMPLATE = "{} to {}"
        range_min, range_max, font_size = number_range(request)
        range_text = SUBTITLE_TEMPLATE.format(range_min, range_max - 1)
    return "{} - {}".format(range_text, retrieve_query_parameter(request, "paper_size"))


def number_range(request):
    """Return number range tuple for resource.

    Args:
        request: HTTP request object

    Returns:
        Tuple of (range_min, range_max, font_size)
    """
    parameter_options = valid_options()
    prefilled_values = retrieve_query_parameter(request, "prefilled_values", parameter_options["prefilled_values"])
    range_min = 0
    range_max = 0
    font_size = 150
    if prefilled_values == "easy":
        range_min = 1
        range_max = 10
    elif prefilled_values == "medium":
        range_min = 10
        range_max = 100
        font_size = 120
    elif prefilled_values == "hard":
        range_min = 100
        range_max = 1000
        font_size = 90
    return (range_min, range_max, font_size)


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "prefilled_values": ["blank", "easy", "medium", "hard"],
        "paper_size": ["a4", "letter"],
    }
