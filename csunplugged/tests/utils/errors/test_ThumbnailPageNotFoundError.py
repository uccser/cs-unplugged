"""Test class for ThumbnailPageNotFoundError error."""

from django.test import SimpleTestCase
from utils.errors.ThumbnailPageNotFoundError import ThumbnailPageNotFoundError
from unittest.mock import Mock


class ThumbnailPageNotFoundErrorTest(SimpleTestCase):
    """Test class for ThumbnailPageNotFoundError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        generator = Mock()
        generator.__class__.__name__ = "Name"
        exception = ThumbnailPageNotFoundError(generator)
        self.assertEqual(exception.generator_name, "Name")

    def test_string(self):
        generator = Mock()
        generator.__class__.__name__ = "Name"
        exception = ThumbnailPageNotFoundError(generator)
        self.assertEqual(
            exception.__str__(),
            "Name did not return a page with a designated thumbnail."
        )
