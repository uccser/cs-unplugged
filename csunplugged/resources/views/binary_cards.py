"""Module for generating Binary Cards resource."""

from PIL import Image


def resource_image(get_request, resource):
    """Create a image for Binary Cards resource.

    Args:
        get_request: HTTP request object
        resource: Object of resource data.

    Returns:
        A Pillow image object.
    """
    IMAGE_PATHS = [
        "static/img/resources/binary-cards/binary-cards-1-dot.png",
        "static/img/resources/binary-cards/binary-cards-2-dots.png",
        "static/img/resources/binary-cards/binary-cards-4-dots.png",
        "static/img/resources/binary-cards/binary-cards-8-dots.png",
        "static/img/resources/binary-cards/binary-cards-16-dots.png",
        "static/img/resources/binary-cards/binary-cards-32-dots.png",
        "static/img/resources/binary-cards/binary-cards-64-dots.png",
        "static/img/resources/binary-cards/binary-cards-128-dots.png",
    ]

    images = []

    for image_path in IMAGE_PATHS:
        image = Image.open(image_path)
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
    return resource.name
