"""Module for generating Binary to Alphabet resource."""

from PIL import Image, ImageDraw, ImageFont
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource_image(request, resource):
    """Create a image for Binary to Alphabet resource.

    Args:
        request: HTTP request object
        resource: Object of resource data.

    Returns:
        A Pillow image object.
    """
    # Retrieve relevant image
    parameter_options = valid_options()
    worksheet_version = retrieve_query_parameter(request, "worksheet_version", parameter_options["worksheet_version"])
    if worksheet_version == "student":
        image_path = "static/img/resources/binary-to-alphabet/table.png"
    else:
        image_path = "static/img/resources/binary-to-alphabet/table-teacher.png"
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font_size = 30
    font_path = "static/fonts/PatrickHand-Regular.ttf"
    font = ImageFont.truetype(font_path, font_size)

    # Draw headings
    column_headings = ["Base 10", "Binary", "Letter"]
    heading_coord_x = 18
    heading_coord_y = 6

    i = 0
    while i < 9:  # 9 = number of columns

        if i % 3 == 0:
            text = str(column_headings[0])
        elif i % 3 == 1:
            text = str(column_headings[1])
        else:
            text = str(column_headings[2])

        draw.text(
            (heading_coord_x, heading_coord_y),
            text,
            font=font,
            fill="#000"
        )

        heading_coord_x += 113

        i += 1

    # Draw numbers
    # Column data: (min number, max number), x coord
    columns_data = [((0, 9), 58), ((9, 18), 397), ((18, 27), 736)]

    for column_set in columns_data:
        start, end = column_set[0]
        base_coord_x = column_set[1]
        base_coord_y = 75

        for number in range(start, end):
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

            base_coord_y += 54

    image = image.rotate(90, expand=True)
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
    text = "{} - {}".format(
        retrieve_query_parameter(request, "worksheet_version"),
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
        "worksheet_version": ["student", "teacher"],
        "paper_size": ["a4", "letter"]
    }
