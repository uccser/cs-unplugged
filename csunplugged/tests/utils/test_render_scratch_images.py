"""Test class for render_scratch_images in check_required_files module."""

from django.test import SimpleTestCase, override_settings
from utils import check_required_files
from utils.errors.CouldNotFindImageError import CouldNotFindImageError
from unittest.mock import Mock
import os.path
import shutil

SCRATCH_PATH = "temp/tests/scratch/"


@override_settings(SCRATCH_GENERATION_LOCATION=SCRATCH_PATH)
class RenderScratchImagesTest(SimpleTestCase):
    """Test class for render_scratch_images in check_required_files module."""

    def tearDown(self):
        """Automatically called after each test."""
        shutil.rmtree(SCRATCH_PATH)

    def test_render_scratch_images_single(self):
        images = [
            create_scratch_data(1)
        ]
        check_required_files.render_scratch_images(images)
        self.assertEqual(
            "Say 1\n",
            open(os.path.join(SCRATCH_PATH, "scratch-blocks-1.txt")).read()
        )

    def test_render_scratch_images_multiple(self):
        images = [
            create_scratch_data(1),
            create_scratch_data(2),
            create_scratch_data(3),
            create_scratch_data(4),
        ]
        check_required_files.render_scratch_images(images)
        self.assertEqual(
            "Say 1\n",
            open(os.path.join(SCRATCH_PATH, "scratch-blocks-1.txt")).read()
        )
        self.assertEqual(
            "Say 2\n",
            open(os.path.join(SCRATCH_PATH, "scratch-blocks-2.txt")).read()
        )
        self.assertEqual(
            "Say 3\n",
            open(os.path.join(SCRATCH_PATH, "scratch-blocks-3.txt")).read()
        )
        self.assertEqual(
            "Say 4\n",
            open(os.path.join(SCRATCH_PATH, "scratch-blocks-4.txt")).read()
        )

    def test_render_scratch_images_duplicate(self):
        images = [
            create_scratch_data(1),
            create_scratch_data(1),
            create_scratch_data(1),
        ]
        check_required_files.render_scratch_images(images)
        self.assertEqual(
            "Say 1\n",
            open(os.path.join(SCRATCH_PATH, "scratch-blocks-1.txt")).read()
        )

    def test_render_scratch_images_no_images_no_folder(self):
        check_required_files.render_scratch_images([])
        self.assertFalse(os.path.isdir(SCRATCH_PATH))
        os.makedirs(SCRATCH_PATH)

    def test_render_scratch_images_one_images_no_folder(self):
        check_required_files.render_scratch_images([create_scratch_data(1)])
        self.assertTrue(os.path.isdir(SCRATCH_PATH))

    def test_render_scratch_images_no_images_exists_folder(self):
        os.makedirs(SCRATCH_PATH)
        check_required_files.render_scratch_images([])
        self.assertTrue(os.path.isdir(SCRATCH_PATH))

    def test_render_scratch_images_one_images_exists_folder(self):
        os.makedirs(SCRATCH_PATH)
        check_required_files.render_scratch_images([create_scratch_data(1)])
        self.assertTrue(os.path.isdir(SCRATCH_PATH))

def create_scratch_data(number):
    data = Mock()
    data.hash = str(number)
    data.text = "Say {}\n".format(number)
    return data
