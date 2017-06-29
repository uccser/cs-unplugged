"""Module for generating Train Stations resource."""

from PIL import Image


def resource_image(task, resource_manager):
    """Create a image for Train Stations resource.

    Args:
        task: Dicitionary of requested document options.
        resource_manager: File loader for external resources.

    Returns:
        A list of Pillow image objects.
    """
    image_path = "img/resources/train-stations/train-stations-tracks-{}.png"
    track_type = task["tracks"]
    data = resource_manager.load(image_path.format(track_type))
    image = Image.open(data)
    image = image.rotate(90, expand=True)
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
    return "{} tracks - {}".format(
        task["tracks"],
        task["paper_size"]
    )


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "tracks": ["circular", "twisted"],
        "paper_size": ["a4", "letter"]
    }
