"""Test class for find_image_files in check_required_files module."""

from django.test import SimpleTestCase, override_settings
from utils import check_required_files
from utils.errors.CouldNotFindImageError import CouldNotFindImageError
from unittest.mock import Mock


class FindImageFilesTest(SimpleTestCase):
    """Test class for find_image_files in check_required_files module."""

    def test_find_image_files_valid(self):
        images = {"img/logo.png", "img/favicon.ico"}
        check_required_files.find_image_files(images, "md file path")

    def test_find_image_files_missing(self):
        images = {"img/logo.png", "img/invalid-image.jaypheg"}
        self.assertRaises(
            CouldNotFindImageError,
            check_required_files.find_image_files,
            images,
            "md file path"
        )
