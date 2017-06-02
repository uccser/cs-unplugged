"""Module for generating Treasure Hunt resource."""

from PIL import Image, ImageDraw, ImageFont
from random import sample


def resource_image(task, resource_manager):
    """Create a image for Treasure Hunt resource.

    Args:
        task: Dicitionary of requested document options.
        resource_manager: File loader for external resources.

    Returns:
        A Pillow image object.
    """
    image_path = "img/resources/resource-treasure-hunt.png"
    data = resource_manager.load(image_path)
    image = Image.open(data)
    draw = ImageDraw.Draw(image)

    font_path = "fonts/PatrickHand-Regular.ttf"
    local_font_path = resource_manager.get_path(font_path)

    # Add numbers to image if required
    prefilled_values = task["prefilled_values"]
    number_order = task["number_order"]

    if prefilled_values != "blank":
        (range_min, range_max, font_size) = number_range(task)
        font = ImageFont.truetype(local_font_path, font_size)

        total_numbers = 26
        numbers = sample(range(range_min, range_max), total_numbers)
        if number_order == "sorted":
            numbers.sort()

        starting_coord_y = 494
        base_coord_y = starting_coord_y
        coord_y_increment = 286
        base_coords_x = [257, 692]
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
        text = subtitle(task)
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

    return image


def subtitle(task):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        task: Dicitionary of requested document.

    Returns:
        text for subtitle (string)
    """
    prefilled_values = task["prefilled_values"]
    if prefilled_values == "blank":
        text = "blank"
    else:
        SUBTITLE_TEMPLATE = "{} - {} to {}"
        number_order_text = task["number_order"].title()
        range_min, range_max, font_size = number_range(task)
        text = SUBTITLE_TEMPLATE.format(number_order_text, range_min, range_max - 1)
    return "{} - {}".format(text, task["paper_size"])


def number_range(task):
    """Return number range tuple for resource.

    Args:
        task: Dicitionary of requested document.

    Returns:
        Tuple of (range_min, range_max, font_size)
    """
    prefilled_values = task["prefilled_values"]
    range_min = 0
    if prefilled_values == "easy":
        range_max = 100
        font_size = 97
    elif prefilled_values == "medium":
        range_max = 1000
        font_size = 80
    elif prefilled_values == "hard":
        range_max = 10000
        font_size = 70
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
        "paper_size": ["a4", "letter"],
    }
