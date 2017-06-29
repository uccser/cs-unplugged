"""Module for generating Module Clock resource."""

from math import pi, sin, cos
from PIL import Image, ImageDraw, ImageFont


def resource_image(task, resource_manager):
    """Create a image for Modulo Clock resource.

    Args:
        task: Dicitionary of requested document options.
        resource_manager: File loader for external resources.

    Returns:
        A list of Pillow image objects (list).
    """
    image_path = "img/resources/modulo-clock/modulo-clock-{}.png"

    modulo_number = int(task["modulo_number"])
    data = resource_manager.load(image_path.format(modulo_number))
    image = Image.open(data)
    draw = ImageDraw.Draw(image)

    font_size = 150
    font_path = "fonts/PatrickHand-Regular.ttf"
    local_font_path = resource_manager.get_path(font_path)
    font = ImageFont.truetype(local_font_path, font_size)

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


def subtitle(task):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        task: Dicitionary of requested document.

    Returns:
        Text for subtitle (str).
    """
    modulo_number = task["modulo_number"]
    if modulo_number == "1":
        modulo_text = "blank"
    else:
        modulo_text = modulo_number
    return "{} - {}".format(
        modulo_text,
        task["paper_size"]
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
