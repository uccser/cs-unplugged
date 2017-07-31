"""Module for generating Sorting Network Cards resource."""

from random import sample
from PIL import Image, ImageDraw, ImageFont
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource(request, resource):
    """Create a image for Sorting Network Cards resource.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).

    Returns:
        A list of dictionaries for each resource page.
    """
    IMAGE_SIZE_X = 2000
    IMAGE_SIZE_Y = 3000
    LINE_COLOUR = "#000000"
    LINE_WIDTH = 3
    font_path = "static/fonts/PatrickHand-Regular.ttf"

    # Retrieve parameters
    parameter_options = valid_options()
    card_type = retrieve_query_parameter(request, "type", parameter_options["type"])

    # Create card outlines
    card_outlines = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#fff")
    draw = ImageDraw.Draw(card_outlines)
    for x_coord in range(0, IMAGE_SIZE_X, IMAGE_SIZE_X - LINE_WIDTH):
        draw.line([(x_coord, 0), (x_coord, IMAGE_SIZE_Y)], fill=LINE_COLOUR, width=LINE_WIDTH)
    for y_coord in range(0, IMAGE_SIZE_Y, int(IMAGE_SIZE_Y / 2 - LINE_WIDTH)):
        draw.line([(0, y_coord), (IMAGE_SIZE_X, y_coord)], fill=LINE_COLOUR, width=LINE_WIDTH)

    # Prepare text data
    if card_type == "small_numbers":
        font_size = 800
        text = ["1", "2", "3", "4", "5", "6"]
    elif card_type == "large_numbers":
        font_size = 500
        text = []
        numbers = sample(range(1700000, 2100000), 6)
        for number in numbers:
            text.append("{:,}".format(number))
    elif card_type == "fractions":
        font_size = 900
        font_path = "static/fonts/NotoSans-Regular.ttf"
        text = [u"\u00bd", u"\u2153", u"\u2154", u"\u215c", u"\u00be", u"\u215d"]
    elif card_type == "maori_numbers":
        font_size = 300
        text = [
            "tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru",
            "iwa", "tekau", "tekau mā tahi", "tekau mā waru", "tekau mā toru",
            "tekau mā whā", "rua tekau", "rua tekau mā ono"
        ]
    elif card_type == "words":
        font_size = 500
        text = ["crocodile", "crochet", "kiwi", "weka", "kiwi", "kiwano"]
    elif card_type == "letters":
        font_size = 800
        text = ["L", "O", "N", "K", "E", "D", "S", "P", "G", "B", "I", "Y"]
    else:
        font_size = 500
        text = [
            "whero", "kākāriki", "kiwikiwi", "karaka",
            "kōwhai", "pango", "māwhero", "mā"
        ]

    font = ImageFont.truetype(font_path, font_size)
    card_centers = [
        (IMAGE_SIZE_X / 2, IMAGE_SIZE_Y / 4),
        (IMAGE_SIZE_X / 2, (IMAGE_SIZE_Y / 4) * 3),
    ]

    # Add text to cards
    pages = []
    for (text_number, text_string) in enumerate(text):
        if text_number % 2 == 0:
            page = card_outlines.copy()
            draw = ImageDraw.Draw(page)
            (x, y) = card_centers[0]
        else:
            (x, y) = card_centers[1]

        text_width, text_height = draw.textsize(text_string, font=font)
        coord_x = x - (text_width / 2)
        coord_y = y - (text_height / 1.5)
        draw.text(
            (coord_x, coord_y),
            text_string,
            font=font,
            fill="#000"
        )
        # If text on second card but not last page
        if text_number % 2 == 1 and text_number != len(text) - 1:
            pages.append({"type": "image", "data": page})
    pages.append({"type": "image", "data": page})
    return pages


def subtitle(request, resource):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).

    Returns:
        text for subtitle (str).
    """
    return "{} - {}".format(
        retrieve_query_parameter(request, "type").replace("_", " "),
        retrieve_query_parameter(request, "paper_size")
    )


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "type": [
            "small_numbers", "large_numbers", "fractions", "maori_numbers",
            "words", "letters", "maori_colours"
        ],
        "paper_size": ["a4", "letter"],
    }
