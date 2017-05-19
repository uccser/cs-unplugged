"""Module for generating Binary to Alphabet resource."""

from PIL import Image, ImageDraw, ImageFont
from random import sample


def resource_image(get_request, resource):
    """Create a image for Sorting Network resource.

    Args:
        get_request: HTTP request object
        resource: Object of resource data.

    Returns:
        A Pillow image object.
    """
    image_path = "static/img/resources/binary-to-alphabet/table-teacher.png"
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    column_headings = ["Base 10", "Binary", "Letter",
        "Base 10", "Binary", "Letter",
        "Base 10", "Binary", "Letter"
    ]
    column_number_range = [(0, 8), (9, 17), (18, 26)]

    font_size = 50
    font_path = "static/fonts/PatrickHand-Regular.ttf"
    font = ImageFont.truetype(font_path, font_size)

    base_coord_x = 90

    heading_coord_x = 25
    heading_coord_y = 6

    for i,heading in enumerate(column_headings):

        base_coord_y = 110
        text = str(column_headings[i])
        draw.text(
            (heading_coord_x, heading_coord_y),
            text,
            font=font,
            fill="#000"
        )

        coord_y_increment = 75
        coord_x_increment = 515

        heading_coord_x += 172

        if i%3 == 0:
            numbers = range(
                column_number_range[0][0],
                column_number_range[0][1] + 1
            )
        elif i%3 == 1:
            numbers = range(
                column_number_range[1][0],
                column_number_range[1][1] + 1
            )
        else:
            numbers = range(
                column_number_range[2][0],
                column_number_range[2][1] + 1
            )
    
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
    
            base_coord_y += coord_y_increment
    
        base_coord_x += coord_x_increment

    return image


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
    return "blank"
