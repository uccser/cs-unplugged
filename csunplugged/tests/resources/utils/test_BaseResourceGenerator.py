from django.test import tag
from django.http import QueryDict
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.generate_resource_copy import generate_resource_copy
from unittest.mock import MagicMock
from utils.errors.ThumbnailPageNotFound import ThumbnailPageNotFound
from utils.errors.MoreThanOneThumbnailPageFound import MoreThanOneThumbnailPageFound
from io import BytesIO
from PIL import Image
import base64


@tag("resource")
class BaseResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.MM_TO_PIXEL_RATIO = 6
        self.A4_HEIGHT = 267
        self.LETTER_HEIGHT = 249

    def test_pdf_valid_generator(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        query = QueryDict("paper_size=a4")
        generator = get_resource_generator(resource.generator_module, query)
        copy = generate_resource_copy(generator)
        self.assertEqual(len(copy), 1)

    def test_pdf_image_a4_not_resized(self):
        image = Image.new("1", (100, 100))
        generator = MagicMock()
        generator.data.return_value = [{"type": "image", "data": image}]
        generator.requested_options = {"paper_size": "a4"}
        copy = generate_resource_copy(generator, thumbnail=True)
        copy_data = BytesIO(base64.b64decode(copy[0]["data"]))
        copy_image = Image.open(copy_data)
        self.assertEqual(image.size, copy_image.size)

    def test_pdf_image_a4_resized(self):
        size = 3000
        ratio = (self.A4_HEIGHT * self.MM_TO_PIXEL_RATIO) / size
        expected_size = (int(size * ratio), int(size * ratio))
        image = Image.new("1", (size, size))
        generator = MagicMock()
        generator.data.return_value = [{"type": "image", "data": image}]
        generator.requested_options = {"paper_size": "a4"}
        copy = generate_resource_copy(generator, thumbnail=True)
        copy_data = BytesIO(base64.b64decode(copy[0]["data"]))
        copy_image = Image.open(copy_data)
        self.assertEqual(expected_size, copy_image.size)

    def test_pdf_image_letter_not_resized(self):
        image = Image.new("1", (100, 100))
        generator = MagicMock()
        generator.data.return_value = [{"type": "image", "data": image}]
        generator.requested_options = {"paper_size": "letter"}
        copy = generate_resource_copy(generator, thumbnail=True)
        copy_data = BytesIO(base64.b64decode(copy[0]["data"]))
        copy_image = Image.open(copy_data)
        self.assertEqual(image.size, copy_image.size)

    def test_pdf_image_letter_resized(self):
        size = 3000
        ratio = (self.LETTER_HEIGHT * self.MM_TO_PIXEL_RATIO) / size
        expected_size = (int(size * ratio), int(size * ratio))
        image = Image.new("1", (size, size))
        generator = MagicMock()
        generator.data.return_value = [{"type": "image", "data": image}]
        generator.requested_options = {"paper_size": "letter"}
        copy = generate_resource_copy(generator, thumbnail=True)
        copy_data = BytesIO(base64.b64decode(copy[0]["data"]))
        copy_image = Image.open(copy_data)
        self.assertEqual(expected_size, copy_image.size)

    def test_generate_thumbnail_valid_single_page(self):
        generator = MagicMock()
        generator.data.return_value = [{"type": "html", "data": "Page 1"}]
        copy = generate_resource_copy(generator, thumbnail=True)
        self.assertEqual(len(copy), 1)
        self.assertEqual(copy[0]["data"], "Page 1")

    def test_generate_thumbnail_valid_multiple_pages(self):
        generator = MagicMock()
        generator.data.return_value = [
            {"type": "html", "data": "Page 1"},
            {"type": "html", "data": "Page 2", "thumbnail": True}
        ]
        copy = generate_resource_copy(generator, thumbnail=True)
        self.assertEqual(len(copy), 1)
        self.assertEqual(copy[0]["data"], "Page 2")

    def test_generate_thumbnail_none_given(self):
        generator = MagicMock()
        generator.data.return_value = [
            {"type": "html", "data": ""},
            {"type": "html", "data": ""}
        ]
        self.assertRaises(
            ThumbnailPageNotFound,
            generate_resource_copy,
            generator,
            True
        )

    def test_generate_thumbnail_more_than_one_given(self):
        generator = MagicMock()
        generator.data.return_value = [
            {"type": "html", "data": "", "thumbnail": True},
            {"type": "html", "data": "", "thumbnail": True}
        ]
        self.assertRaises(
            MoreThanOneThumbnailPageFound,
            generate_resource_copy,
            generator,
            True
        )
