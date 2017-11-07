from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.PixelPainterResourceGenerator import PixelPainterResourceGenerator
from filecmp import cmp


@tag("resource")
class PixelPainterResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_pixel_painter_resource_generator_invalid_pixel_black_white(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.additional_valid_options["image"].append("invalid")
        generator.requested_options = QueryDict("image=invalid&method=black-white&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )

    def test_pixel_painter_resource_generator_invalid_pixel_greyscale(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.additional_valid_options["image"].append("invalid")
        generator.requested_options = QueryDict("image=invalid&method=greyscale&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )

    def test_pixel_painter_resource_generator_invalid_pixel_colour(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.additional_valid_options["image"].append("invalid")
        generator.requested_options = QueryDict("image=invalid&method=colour&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )

    def test_pixel_painter_resource_generator_thumbnail(self):
        test_output_path = "tests/output/pixel-painter-thumbnail-test-1.png"
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.requested_options = QueryDict("image=boat&method=black-white&paper_size=a4")
        generator.save_thumbnail("Test", test_output_path)
        compare_result = cmp(
            test_output_path,
            "tests/resources/generators/assets/pixel-painter/boat-black-white.png",
            shallow=False
        )
        self.assertTrue(compare_result)

    def test_pixel_painter_resource_generator_thumbnail_run_length(self):
        test_output_path = "tests/output/pixel-painter-thumbnail-test-2.png"
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.requested_options = QueryDict("image=boat&method=run-length-encoding&paper_size=a4")
        generator.save_thumbnail("Test", test_output_path)
        compare_result = cmp(
            test_output_path,
            "tests/resources/generators/assets/pixel-painter/boat-black-white.png",
            shallow=False
        )
        self.assertTrue(compare_result)
