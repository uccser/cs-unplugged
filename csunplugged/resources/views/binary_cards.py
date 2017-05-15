"""Module for generating Binary Cards resource."""

import os.path
from PIL import Image, ImageDraw, ImageFont


def resource_image(get_request, resource):
    """Create a image for Binary Cards resource.

    Args:
        get_request: HTTP request object
        resource: Object of resource data.

    Returns:
        A list of Pillow image objects.
    """
    BASE_IMAGE_PATH = "static/img/resources/binary-cards/"
    IMAGE_SIZE_X = 2480
    IMAGE_SIZE_Y = 3508
    IMAGE_DATA = [
        ("binary-cards-1-dot.png", 1),
        ("binary-cards-2-dots.png", 2),
        ("binary-cards-4-dots.png", 4),
        ("binary-cards-8-dots.png", 8),
        ("binary-cards-16-dots.png", 16),
        ("binary-cards-32-dots.png", 32),
        ("binary-cards-64-dots.png", 64),
        ("binary-cards-128-dots.png", 128),
    ]

    if get_request["display_numbers"] == "yes":
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font = ImageFont.truetype(font_path, 600)
        BASE_COORD_X = IMAGE_SIZE_X / 2
        BASE_COORD_Y = IMAGE_SIZE_Y - 100
        IMAGE_SIZE_Y = IMAGE_SIZE_Y + 300

    images = []

    for (image_path, number) in IMAGE_DATA:
        image = Image.open(os.path.join(BASE_IMAGE_PATH, image_path))
        if get_request["display_numbers"] == "yes":
            background = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#FFF")
            background.paste(image, mask=image)
            draw = ImageDraw.Draw(background)
            text = str(number)
            text_width, text_height = draw.textsize(text, font=font)
            coord_x = BASE_COORD_X - (text_width / 2)
            coord_y = BASE_COORD_Y - (text_height / 2)
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill="#000"
            )
            image = background
        images.append(image)

    return images


def subtitle(get_request, resource):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        get_request: HTTP request object
        resource: Object of resource data.

    Returns:
        text for subtitle (string)
    """
    if get_request["display_numbers"] == "yes":
        text = "with numbers"
    else:
        text = "without numbers"
    return text
