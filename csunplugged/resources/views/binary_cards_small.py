"""Module for generating Binary Cards (Small) resource."""

import os.path
from PIL import Image, ImageDraw, ImageFont
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource_image(request, resource):
    """Create a image for Binary Cards (Small) resource.

    Args:
        request: HTTP request object.
        resource: Object of resource data.

    Returns:
        A list of Pillow image objects.
    """
    BASE_IMAGE_PATH = "static/img/resources/binary-cards-small/"
    IMAGE_SIZE_X = 2480
    IMAGE_SIZE_Y = 3044
    IMAGE_DATA = [
        ("binary-cards-small-1.png", 4),
        ("binary-cards-small-2.png", 8),
        ("binary-cards-small-3.png", 12),
    ]

    # Retrieve parameters
    parameter_options = valid_options()
    requested_bits = retrieve_query_parameter(request, "number_bits", parameter_options["number_bits"])
    dot_counts = retrieve_query_parameter(request, "dot_counts", parameter_options["dot_counts"])
    black_back = retrieve_query_parameter(request, "black_back", parameter_options["black_back"])

    if dot_counts:
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font = ImageFont.truetype(font_path, 200)
        TEXT_COORDS = [
            (525, 1341),
            (1589, 1341),
            (525, 2889),
            (1589, 2889),
        ]

    images = []

    for (image_path, image_bits) in IMAGE_DATA:
        requested_bits = int(requested_bits)
        if image_bits <= requested_bits:
            image = Image.open(os.path.join(BASE_IMAGE_PATH, image_path))
            if dot_counts:
                draw = ImageDraw.Draw(image)
                for number in range(image_bits - 4, image_bits):
                    text = str(pow(2, number))
                    text_width, text_height = draw.textsize(text, font=font)
                    coord_x = TEXT_COORDS[number % 4][0] - (text_width / 2)
                    coord_y = TEXT_COORDS[number % 4][1] - (text_height / 2)
                    draw.text(
                        (coord_x, coord_y),
                        text,
                        font=font,
                        fill="#000"
                    )
            images.append(image)

            if black_back:
                black_card = Image.new("1", (IMAGE_SIZE_X, IMAGE_SIZE_Y))
                images.append(black_card)

    return images


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
    if retrieve_query_parameter(request, "dot_counts"):
        display_numbers_text = "with dot counts"
    else:
        display_numbers_text = "without dot counts"
    if retrieve_query_parameter(request, "black_back"):
        black_back_text = "with black back"
    else:
        black_back_text = "without black back"
    text = "{} bits - {} - {} - {}".format(
        retrieve_query_parameter(request, "number_bits"),
        display_numbers_text,
        black_back_text,
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
        "number_bits": ["4", "8", "12"],
        "dot_counts": [True, False],
        "black_back": [True, False],
        "paper_size": ["a4", "letter"],
    }
