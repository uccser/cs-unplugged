"""Module for generating Treasure Hunt resource."""

from PIL import Image, ImageDraw, ImageFont
from random import sample
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource(request, resource):
    """Create a image for Treasure Hunt resource.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).

    Returns:
        A dictionary for the resource page.
    """
    pages = []
    IMAGE_PATH = "static/img/resources/treasure-hunt/{}.png"
    font_path = "static/fonts/PatrickHand-Regular.ttf"

    parameter_options = valid_options()
    prefilled_values = retrieve_query_parameter(request, "prefilled_values", parameter_options["prefilled_values"])
    number_order = retrieve_query_parameter(request, "number_order", parameter_options["number_order"])
    instructions = retrieve_query_parameter(request, "instructions", parameter_options["instructions"])
    art_style = retrieve_query_parameter(request, "art", parameter_options["art"])

    if instructions:
        image = Image.open(IMAGE_PATH.format("instructions"))
        ImageDraw.Draw(image)
        pages.append({"type": "image", "data": image})

    image = Image.open(IMAGE_PATH.format(art_style))
    draw = ImageDraw.Draw(image)

    # Add numbers to image if required
    if prefilled_values != "blank":
        (range_min, range_max, font_size) = number_range(request)
        font = ImageFont.truetype(font_path, font_size)

        total_numbers = 26
        numbers = sample(range(range_min, range_max), total_numbers)
        if number_order == "sorted":
            numbers.sort()

        base_coord_y = 1530
        coord_y_increment = 597
        base_coords_x = [1200, 2080]
        for i in range(0, total_numbers):
            text = str(numbers[i])
            text_width, text_height = draw.textsize(text, font=font)

            coord_x = base_coords_x[i % 2] - (text_width / 2)
            coord_y = base_coord_y - (text_height / 2)
            if i % 2 == 1:
                coord_y -= 10
                base_coord_y += coord_y_increment
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill="#000"
            )

        # Add number order and range text
        text = subtitle(request, resource)
        font = ImageFont.truetype(font_path, 110)
        text_width, text_height = draw.textsize(text, font=font)
        coord_x = 1472 - (text_width / 2)
        coord_y = 35 - (text_height / 2)
        draw.text(
            (coord_x, coord_y),
            text,
            font=font,
            fill="#000"
        )
    pages.append({"type": "image", "data": image})

    return pages


def subtitle(request, resource):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).

    Returns:
        text for subtitle (str)
    """
    prefilled_values = retrieve_query_parameter(request, "prefilled_values")
    if prefilled_values == "blank":
        text = "blank"
    else:
        SUBTITLE_TEMPLATE = "{} - {} to {}"
        number_order_text = retrieve_query_parameter(request, "number_order").title()
        range_min, range_max, font_size = number_range(request)
        text = SUBTITLE_TEMPLATE.format(number_order_text, range_min, range_max - 1)
    return "{} - {}".format(text, retrieve_query_parameter(request, "paper_size"))


def number_range(request):
    """Return number range tuple for resource.

    Args:
        request: HTTP request object (HttpRequest).

    Returns:
        Tuple of (range_min, range_max, font_size)
    """
    parameter_options = valid_options()
    prefilled_values = retrieve_query_parameter(request, "prefilled_values", parameter_options["prefilled_values"])
    range_min = 0
    if prefilled_values == "easy":
        range_max = 100
        font_size = 170
    elif prefilled_values == "medium":
        range_max = 1000
        font_size = 140
    elif prefilled_values == "hard":
        range_max = 10000
        font_size = 125
    return (range_min, range_max, font_size)


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "prefilled_values": ["blank", "easy", "medium", "hard"],
        "number_order": ["sorted", "unsorted"],
        "instructions": [True, False],
        "art": ["colour", "bw"],
        "paper_size": ["a4", "letter"],
    }
