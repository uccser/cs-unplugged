"""Module for checking required files found within Markdown conversions."""

import os
import os.path
from django.conf import settings
from utils.errors.CouldNotFindImageError import CouldNotFindImageError


def check_converter_required_files(required_files, md_file_path):
    """Process data within required files found by Markdown converter.

    Args:
        required_files: Dictionary of required files data (dict).
    """
    render_scratch_images(required_files["scratch_images"])
    find_image_files(required_files["images"], md_file_path)


def render_scratch_images(scratch_images):
    """Write Scratch data for image rendering by Gulp script.

    Args:
        scratch_images: List of named tuples containing
            scratch image data to be rendered (list).
    """
    base_directory = settings.SCRATCH_GENERATION_LOCATION
    FILEPATH_TEMPLATE = os.path.join(base_directory, "scratch-blocks-{hash}.txt")
    if scratch_images and not os.path.exists(base_directory):
        os.makedirs(base_directory)
    for scratch_image in scratch_images:
        filepath = FILEPATH_TEMPLATE.format(hash=scratch_image.hash)
        if not os.path.isfile(filepath):
            with open(filepath, "w") as scratch_temp_file:
                scratch_temp_file.write(scratch_image.text)


def find_image_files(images, md_file_path):
    """Confirm each image is in static folder.

    Args:
        images: image file names (set).
        md_file_path: path to Markdown file (str).

    Raises:
        CouldNotFindImageError: when image file cannot be found.
    """
    for image in images:
        if not os.path.exists(os.path.join(settings.STATIC_ROOT, image)):
            raise CouldNotFindImageError(image, md_file_path)
