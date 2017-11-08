"""Test class for ThumbnailPageNotFound error."""

from django.test import SimpleTestCase
from utils.errors.ThumbnailPageNotFound import ThumbnailPageNotFound
from unittest.mock import Mock


class ThumbnailPageNotFoundTest(SimpleTestCase):
    """Test class for ThumbnailPageNotFound error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        generator = Mock()
        generator.__class__.__name__ = "Name"
        exception = ThumbnailPageNotFound(generator)
        self.assertEqual(exception.generator_name, "Name")

    def test_string(self):
        generator = Mock()
        generator.__class__.__name__ = "Name"
        exception = ThumbnailPageNotFound(generator)
        self.assertEqual(
            exception.__str__(),
            "Name did not return a page with a designated thumbnail."
        )
