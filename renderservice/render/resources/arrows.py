"""Module for generating Arrows resource."""

from PIL import Image, ImageDraw


def resource_image(task, resource_manager):
    """Create a image for Arrows resource.

    Args:
        task: Dicitionary of requested document options.
        resource_manager: File loader for external resources.

    Returns:
        A list of Pillow image objects.
    """
    image_path = "img/resources/arrows/arrows.png"
    data = resource_manager.load(image_path)
    image = Image.open(data)
    ImageDraw.Draw(image)
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
    return task["paper_size"]


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "paper_size": ["a4", "letter"]
    }
