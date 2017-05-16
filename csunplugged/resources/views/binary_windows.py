"""Module for generating Binary Windows resource."""

import os.path
from PIL import Image, ImageDraw, ImageFont
from django.http import Http404


def resource_image(get_request, resource):
    """Create a image for Binary Windows resource.

    Args:
        get_request: HTTP request object (Request)
        resource: Object of resource data (Resource).

    Returns:
        A list of Pillow image objects (list of Image objects).
    """
    BASE_IMAGE_PATH = "static/img/resources/binary-windows/"
    FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
    FONT = ImageFont.truetype(FONT_PATH, 300)

    # Retrieve parameters
    number_of_bits = get_request.get("number_bits", None)
    if number_of_bits is None:
        raise Http404("Number of bits parameter not specified.")
    if number_of_bits not in ["4", "8"]:
        raise Http404("Number of bits parameter not valid.")

    images = []

    # Add first image
    image = Image.open(os.path.join(BASE_IMAGE_PATH, "binary-windows-1-to-8.png"))

    text_coord_x = 660
    text_coord_y = 1700
    for i in range(4):
        draw = ImageDraw.Draw(image)
        text = "1"
        text_width, text_height = draw.textsize(text, font=FONT)
        coord_x = text_coord_x - (text_width / 2)
        coord_y = text_coord_y - (text_height / 2)
        draw.text(
            (coord_x, coord_y),
            text,
            font=FONT,
            fill="#000"
        )
        text_coord_x += 724
    image = image.rotate(90, expand=True)
    images.append(image)

    # Add back page
    images.append(back_page(BASE_IMAGE_PATH, FONT))

    # Add second page if required
    if number_of_bits == "8":
        image = Image.open(os.path.join(BASE_IMAGE_PATH, "binary-windows-16-to-128.png"))
        text_coord_x = 660
        for i in range(4):
            draw = ImageDraw.Draw(image)
            text = "1"
            text_width, text_height = draw.textsize(text, font=FONT)
            coord_x = text_coord_x - (text_width / 2)
            coord_y = text_coord_y - (text_height / 2)
            draw.text(
                (coord_x, coord_y),
                text,
                font=FONT,
                fill="#000"
            )
            text_coord_x += 724
        image = image.rotate(90, expand=True)
        images.append(image)

        # Add back page
        images.append(back_page(BASE_IMAGE_PATH, FONT))

    return images


def back_page(BASE_IMAGE_PATH, FONT):
    """Return a Pillow object of back page of Binary Windows.

    Args:
        BASE_IMAGE_PATH: Base image path for finding images (str).
        FONT: Pillow ImageFont for writing text (ImageFont).

    Returns:
        Pillow Image of back page (Image).
    """
    image = Image.open(os.path.join(BASE_IMAGE_PATH, "binary-windows-blank.png"))
    text_coord_x = 660
    text_coord_y = 650
    for i in range(4):
        draw = ImageDraw.Draw(image)
        text = "0"
        text_width, text_height = draw.textsize(text, font=FONT)
        coord_x = text_coord_x - (text_width / 2)
        coord_y = text_coord_y - (text_height / 2)
        draw.text(
            (coord_x, coord_y),
            text,
            font=FONT,
            fill="#000"
        )
        text_coord_x += 724
    image = image.rotate(90, expand=True)
    return image


def subtitle(get_request, resource):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        get_request: HTTP request object (Request).
        resource: Object of resource data (Resource).

    Returns:
        text for subtitle (str)
    """
    return "Example subtitle"
