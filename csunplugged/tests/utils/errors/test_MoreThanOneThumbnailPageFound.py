"""Test class for MoreThanOneThumbnailPageFound error."""

from django.test import SimpleTestCase
from utils.errors.MoreThanOneThumbnailPageFound import MoreThanOneThumbnailPageFound
from unittest.mock import Mock


class MoreThanOneThumbnailPageFoundTest(SimpleTestCase):
    """Test class for MoreThanOneThumbnailPageFound error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        generator = Mock()
        generator.__class__.__name__ = "Name"
        exception = MoreThanOneThumbnailPageFound(generator)
        self.assertEqual(exception.generator_name, "Name")

    def test_string(self):
        generator = Mock()
        generator.__class__.__name__ = "Name"
        exception = MoreThanOneThumbnailPageFound(generator)
        self.assertEqual(
            exception.__str__(),
            "Name returned more than one page as the designated thumbnail."
        )
