"""Module for generating Binary Windows resource."""

import os.path
from PIL import Image, ImageDraw, ImageFont
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource_image(request, resource):
    """Create a image for Binary Windows resource.

    Args:
        request: HTTP request object (Request).
        resource: Object of resource data (Resource).

    Returns:
        A list of Pillow image objects (list of Image objects).
    """
    BASE_IMAGE_PATH = "static/img/resources/binary-windows/"
    FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
    FONT = ImageFont.truetype(FONT_PATH, 300)
    SMALL_FONT = ImageFont.truetype(FONT_PATH, 180)

    # Retrieve parameters
    number_of_bits = retrieve_query_parameter(request, "number_bits", ["4", "8"])
    value_type = retrieve_query_parameter(request, "value_type", ["binary", "lightbulb"])
    dot_counts = retrieve_query_parameter(request, "dot_counts", ["yes", "no"])

    images = []
    page_sets = [("binary-windows-1-to-8.png", 8)]
    if number_of_bits == "8":
        page_sets.append(("binary-windows-16-to-128.png", 128))

    for (filename, dot_count_start) in page_sets:
        image = Image.open(os.path.join(BASE_IMAGE_PATH, filename))
        image = add_digit_values(image, value_type, True, 660, 724, 1700, FONT)
        if dot_counts == "yes":
            image = add_dot_counts(image, dot_count_start, SMALL_FONT)
        image = image.rotate(90, expand=True)
        images.append(image)
        images.append(back_page(BASE_IMAGE_PATH, FONT, value_type))

    return images


def back_page(BASE_IMAGE_PATH, FONT, value_type):
    """Return a Pillow object of back page of Binary Windows.

    Args:
        BASE_IMAGE_PATH: Base image path for finding images (str).
        FONT: Pillow ImageFont for writing text (ImageFont).
        value_type: Type of value representation used (str).

    Returns:
        Pillow Image of back page (Image).
    """
    image = Image.open(os.path.join(BASE_IMAGE_PATH, "binary-windows-blank.png"))
    image = add_digit_values(image, value_type, False, 660, 724, 650, FONT)
    image = image.rotate(90, expand=True)
    return image


def add_dot_counts(image, starting_value, font):
    """Add dot count text onto image.

    Args:
        image: The image to add text to (Pillow Image).
        starting_value: Number on left window (int).
        font: Font used for adding text (Pillow Font).

    Returns:
        Pillow Image with text added.
    """
    value = starting_value
    draw = ImageDraw.Draw(image)
    coord_x = 660
    coord_x_increment = 724
    coord_y = 1000
    for i in range(4):
        text = str(value)
        text_width, text_height = draw.textsize(text, font=font)
        text_coord_x = coord_x - (text_width / 2)
        text_coord_y = coord_y - (text_height / 2)
        draw.text(
            (text_coord_x, text_coord_y),
            text,
            font=font,
            fill="#000"
        )
        coord_x += coord_x_increment
        value = int(value / 2)
    return image


def add_digit_values(image, value_type, on, x_coord_start, x_coord_increment, base_y_coord, font):
    """Add binary values onto image.

    Args:
        image: The image to add binary values to (Pillow Image).
        value_type: Either "binary" for 0's and 1's, or "lightbulb" for
                    lit and unlit lightbulbs (str).
        on: True if binary value is on/lit, otherwise False (bool).
        x_coord_start: X co-ordinate starting value (int).
        x_coord_increment: X co-ordinate increment value (int).
        base_y_coord: Y co-ordinate value (int).
        font: Font used for adding text (Pillow Font).

    Returns:
        Pillow Image with binary values.
    """
    text_coord_x = x_coord_start

    if value_type == "binary":
        if on:
            text = "1"
        else:
            text = "0"
    elif value_type == "lightbulb":
        if on:
            image_file = "col_binary_lightbulb.png"
        else:
            image_file = "col_binary_lightbulb_off.png"
        lightbulb = Image.open(os.path.join("static/img/topics/", image_file))
        (width, height) = lightbulb.size
        SCALE_FACTOR = 0.6
        lightbulb = lightbulb.resize((int(width * SCALE_FACTOR), int(height * SCALE_FACTOR)))
        (width, height) = lightbulb.size
        lightbulb_width = int(width / 2)
        lightbulb_height = int(height / 2)
        if not on:
            lightbulb = lightbulb.rotate(180)

    for i in range(4):
        draw = ImageDraw.Draw(image)
        if value_type == "binary":

            text_width, text_height = draw.textsize(text, font=font)
            coord_x = text_coord_x - (text_width / 2)
            coord_y = base_y_coord - (text_height / 2)
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill="#000"
            )
        elif value_type == "lightbulb":
            coords = (text_coord_x - lightbulb_width, base_y_coord - lightbulb_height + 75)
            image.paste(lightbulb, box=coords, mask=lightbulb)
        text_coord_x += x_coord_increment
    return image


def subtitle(request, resource):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        request: HTTP request object (Request).
        resource: Object of resource data (Resource).

    Returns:
        text for subtitle (str)
    """
    number_of_bits = retrieve_query_parameter(request, "number_bits")
    value_type = retrieve_query_parameter(request, "value_type")
    dot_counts = retrieve_query_parameter(request, "dot_counts")
    if dot_counts == "yes":
        count_text = "with dot counts"
    else:
        count_text = "without dot counts"
    TEMPLATE = "{num_bits} bits - {value} - {counts}"
    text = TEMPLATE.format(
        num_bits=number_of_bits,
        value=value_type,
        counts=count_text
    )
    return text


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    valid_options = {
        "number_bits": ["4", "8"],
        "value_type": ["binary", "lightbulb"],
        "dot_counts": ["yes", "no"],
        "paper_size": ["a4", "letter"],
    }
    return valid_options
