"""Module for checking required files found within Markdown conversions."""

import os
import os.path
from django.contrib.staticfiles import finders
from utils.errors.CouldNotFindImageError import CouldNotFindImageError


def check_converter_required_files(required_files, md_file_path):
    """Process data within required files found by Markdown converter.

    Args:
        required_files (dict): Dictionary of required files data.
    """
    render_scratch_images(required_files["scratch_images"])
    find_image_files(required_files["images"], md_file_path)


def render_scratch_images(scratch_images):
    """Write Scratch data for image rendering by Gulp script.

    Args:
        scratch_images (list): List of named tuples containing
            scratch image data to be rendered.
    """
    FILEPATH_TEMPLATE = "temp/scratch-blocks-{hash}.txt"
    if scratch_images and not os.path.exists("temp"):
        os.makedirs("temp")
    for scratch_image in scratch_images:
        filepath = FILEPATH_TEMPLATE.format(hash=scratch_image.hash)
        if not os.path.isfile(filepath):
            with open(filepath, "w") as scratch_temp_file:
                scratch_temp_file.write(scratch_image.text)


def find_image_files(images, md_file_path):
    """Confirm each image is in static folder.

    Args:
        images (set): image file names

    Raises:
        CouldNotFindImageError: when image file cannot be found
    """
    for image in images:
        if not finders.find(image):
            raise CouldNotFindImageError(image, md_file_path)
