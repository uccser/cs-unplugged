from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.PixelPainterResourceGenerator import PixelPainterResourceGenerator


@tag("resource")
class PixelPainterResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_pixel_painter_resource_generation_invalid_pixel_black_white(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.requested_options = QueryDict("image=invalid&method=black-white&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )

    def test_pixel_painter_resource_generation_invalid_pixel_greyscale(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.requested_options = QueryDict("image=invalid&method=greyscale&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )

    def test_pixel_painter_resource_generation_invalid_pixel_colour(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.requested_options = QueryDict("image=invalid&method=colour&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )
