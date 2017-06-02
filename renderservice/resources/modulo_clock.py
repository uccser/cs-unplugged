"""Module for generating Module Clock resource."""

from math import pi, sin, cos
from PIL import Image, ImageDraw, ImageFont


def resource_image(task, resource_manager):
    """Create a image for Modulo Clock resource.

    Args:
        task: Dicitionary of requested document options.
        resource_manager: File loader for external resources.

    Returns:
        A list of Pillow image objects.
    """
    modulo_number = int(task["modulo_number"])
    if modulo_number == 2:
        image_path = "img/resources/modulo-clock/modulo-clock-2.png"
    elif modulo_number == 10:
        image_path = "img/resources/modulo-clock/modulo-clock-10.png"
    data = resource_manager.load(image_path)
    image = Image.open(data)
    draw = ImageDraw.Draw(image)

    font_size = 150
    font_path = "fonts/PatrickHand-Regular.ttf"
    local_font_path = resource_manager.get_path(font_path)
    font = ImageFont.truetype(local_font_path, font_size)

    x_offset = 75
    y_offset = 225
    radius = 750
    x_center = (image.width - x_offset) / 2
    y_center = (image.height - y_offset) / 2
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


def subtitle(task):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        task: Dicitionary of requested document.

    Returns:
        Text for subtitle (str).
    """
    return "{} - {}".format(
        task["modulo_number"],
        task["paper_size"]
    )


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
