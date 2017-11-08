from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.utils.resize_encode_resource_images import resize_encode_resource_images
from io import BytesIO
from PIL import Image
import base64


@tag("resource")
class ResizeEncodeResourceTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MM_TO_PIXEL_RATIO = 6
        self.A4_HEIGHT = 267
        self.LETTER_HEIGHT = 249

    def test_resize_encode_resource_images_image_a4_not_resized(self):
        image = Image.new("1", (100, 100))
        data = [{"type": "image", "data": image}]
        copy = resize_encode_resource_images("a4", data)
        copy_data = BytesIO(base64.b64decode(copy[0]["data"]))
        copy_image = Image.open(copy_data)
        self.assertEqual(image.size, copy_image.size)

    def test_resize_encode_resource_images_image_a4_resized(self):
        size = 3000
        ratio = (self.A4_HEIGHT * self.MM_TO_PIXEL_RATIO) / size
        expected_size = (int(size * ratio), int(size * ratio))
        image = Image.new("1", (size, size))
        data = [{"type": "image", "data": image}]
        copy = resize_encode_resource_images("a4", data)
        copy_data = BytesIO(base64.b64decode(copy[0]["data"]))
        copy_image = Image.open(copy_data)
        self.assertEqual(expected_size, copy_image.size)

    def test_resize_encode_resource_images_image_letter_not_resized(self):
        image = Image.new("1", (100, 100))
        data = [{"type": "image", "data": image}]
        copy = resize_encode_resource_images("letter", data)
        copy_data = BytesIO(base64.b64decode(copy[0]["data"]))
        copy_image = Image.open(copy_data)
        self.assertEqual(image.size, copy_image.size)

    def test_resize_encode_resource_images_image_letter_resized(self):
        size = 3000
        ratio = (self.LETTER_HEIGHT * self.MM_TO_PIXEL_RATIO) / size
        expected_size = (int(size * ratio), int(size * ratio))
        image = Image.new("1", (size, size))
        data = [{"type": "image", "data": image}]
        copy = resize_encode_resource_images("letter", data)
        copy_data = BytesIO(base64.b64decode(copy[0]["data"]))
        copy_image = Image.open(copy_data)
        self.assertEqual(expected_size, copy_image.size)

    def test_resize_encode_resource_images_invalid_size(self):
        self.assertRaises(
            ValueError,
            resize_encode_resource_images,
            "invalid size",
            dict()
        )
