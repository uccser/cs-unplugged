"""Module for generating Pixel Painter resource."""

from PIL import Image, ImageDraw, ImageFont
from utils.retrieve_query_parameter import retrieve_query_parameter
from math import ceil
import string

def resource(request, resource):
    """Create a image for Pixel Painter resource.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).

    Returns:
        A dictionaries for each resource page.
    """
    STATIC_PATH = "static/img/resources/pixel-painter/{}.png"
    FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
    FONT = ImageFont.truetype(FONT_PATH, 80)
    FONT_SMALL = ImageFont.truetype(FONT_PATH, 50)
    TEXT_COLOUR = "#888"

    parameter_options = valid_options()
    method = retrieve_query_parameter(request, "method", parameter_options["method"])
    image_name = retrieve_query_parameter(request, "image", parameter_options["image"])

    image = Image.open(STATIC_PATH.format(image_name + "-pixel"))
    (image_width, image_height) = image.size

    COLUMNS_PER_PAGE = 15
    ROWS_PER_PAGE = 20
    BOX_SIZE = 200
    IMAGE_SIZE_X = BOX_SIZE * COLUMNS_PER_PAGE
    IMAGE_SIZE_Y = BOX_SIZE * ROWS_PER_PAGE
    LINE_COLOUR = "#666"
    LINE_WIDTH = 1

    pages = []
    number_column_pages = ceil(image_width / COLUMNS_PER_PAGE)
    number_row_pages = ceil(image_height / ROWS_PER_PAGE)
    LETTERS = string.ascii_uppercase

    # For each page column
    for number_column_page in range(0, number_column_pages):
        page_start_column = (number_column_page) * COLUMNS_PER_PAGE
        # For each page row
        for number_row_page in range(0, number_row_pages):
            page_start_row = (number_row_page) * ROWS_PER_PAGE
            # Create page
            page = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#fff")
            draw = ImageDraw.Draw(page)

            # Add page grid reference
            draw.text(
                (LINE_WIDTH * 4, -4),
                "{}{}".format(LETTERS[number_row_page], number_column_page + 1),
                font=FONT_SMALL,
                fill=TEXT_COLOUR
            )

            page_columns = min(COLUMNS_PER_PAGE, image_width - page_start_column)
            page_rows = min(ROWS_PER_PAGE, image_height - page_start_row)

            # Draw grid
            grid_width = page_columns * BOX_SIZE
            grid_height = page_rows * BOX_SIZE

            for x_coord in range(0, page_columns * BOX_SIZE, BOX_SIZE):
                draw.line(
                    [(x_coord, 0), (x_coord, grid_height)],
                    fill=LINE_COLOUR,
                    width=LINE_WIDTH
                )
            draw.line(
                [(page_columns * BOX_SIZE - 1, 0), (page_columns * BOX_SIZE - 1, grid_height)],
                fill=LINE_COLOUR,
                width=LINE_WIDTH
            )

            for y_coord in range(0, grid_height, BOX_SIZE):
                draw.line(
                    [(0, y_coord), (grid_width, y_coord)],
                    fill=LINE_COLOUR,
                    width=LINE_WIDTH
                )
            draw.line(
                [(0, grid_height - 1), (grid_width, grid_height - 1)],
                fill=LINE_COLOUR,
                width=LINE_WIDTH
            )

            # Draw text
            for column in range(0, page_columns):
                for row in range(0, page_rows):
                    pixel_value = image.getpixel((page_start_column + column, page_start_row + row))
                    text = str(1 - int(pixel_value / 255))
                    text_width, text_height = draw.textsize(text, font=FONT)
                    text_coord_x = (column * BOX_SIZE) + (BOX_SIZE / 2) - (text_width / 2)
                    text_coord_y = (row * BOX_SIZE) + (BOX_SIZE / 2) - (text_height / 2)
                    draw.text(
                        (text_coord_x, text_coord_y),
                        text,
                        font=FONT,
                        fill=TEXT_COLOUR
                    )

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
    return ""


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "method": ["junior-binary"],
        "image": ["boat", "fish"],
        "paper_size": ["a4", "letter"],
    }
