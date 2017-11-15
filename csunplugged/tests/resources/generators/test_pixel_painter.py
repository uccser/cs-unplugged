from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.PixelPainterResourceGenerator import PixelPainterResourceGenerator
from filecmp import cmp
from copy import deepcopy
import os


@tag("resource")
class PixelPainterResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_output_path = "tests/output/"
        os.makedirs(os.path.dirname(self.test_output_path), exist_ok=True)

    def test_pixel_painter_resource_generator_invalid_pixel_black_white(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.additional_valid_options = deepcopy(generator.additional_valid_options)
        generator.additional_valid_options["image"].append("invalid")
        generator.requested_options = QueryDict("image=invalid&method=black-white&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )

    def test_pixel_painter_resource_generator_invalid_pixel_greyscale(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.additional_valid_options = deepcopy(generator.additional_valid_options)
        generator.additional_valid_options["image"].append("invalid")
        generator.requested_options = QueryDict("image=invalid&method=greyscale&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )

    def test_pixel_painter_resource_generator_invalid_pixel_colour(self):
        generator = PixelPainterResourceGenerator()
        generator.STATIC_PATH = "tests/resources/generators/assets/pixel-painter/{}"
        generator.additional_valid_options = deepcopy(generator.additional_valid_options)
        generator.additional_valid_options["image"].append("invalid")
        generator.requested_options = QueryDict("image=invalid&method=colour&paper_size=a4")
        self.assertRaises(
            ValueError,
            generator.data,
        )

    def test_pixel_painter_resource_generator_thumbnail(self):
        test_output_path = os.path.join(self.test_output_path, "pixel-painter-thumbnail-test-1.png")
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
        test_output_path = os.path.join(self.test_output_path, "pixel-painter-thumbnail-test-2.png")
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

    def test_subtitle_boat_binary_a4(self):
        query = QueryDict("image=boat&method=black-white&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Boat - Black and White - a4"
        )

    def test_subtitle_boat_binary_letter(self):
        query = QueryDict("image=boat&method=black-white&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Boat - Black and White - letter"
        )

    def test_subtitle_boat_run_length_a4(self):
        query = QueryDict("image=boat&method=run-length-encoding&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Boat - Run length encoding - a4"
        )

    def test_subtitle_boat_run_length_letter(self):
        query = QueryDict("image=boat&method=run-length-encoding&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Boat - Run length encoding - letter"
        )

    def test_subtitle_boat_greyscale_a4(self):
        query = QueryDict("image=boat&method=greyscale&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Boat - Greyscale - a4"
        )

    def test_subtitle_boat_greyscale_letter(self):
        query = QueryDict("image=boat&method=greyscale&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Boat - Greyscale - letter"
        )

    def test_subtitle_boat_colour_a4(self):
        query = QueryDict("image=boat&method=colour&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Boat - Colour - a4"
        )

    def test_subtitle_boat_colour_letter(self):
        query = QueryDict("image=boat&method=colour&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Boat - Colour - letter"
        )

    def test_subtitle_fish_binary_a4(self):
        query = QueryDict("image=fish&method=black-white&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fish - Black and White - a4"
        )

    def test_subtitle_fish_binary_letter(self):
        query = QueryDict("image=fish&method=black-white&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fish - Black and White - letter"
        )

    def test_subtitle_fish_run_length_a4(self):
        query = QueryDict("image=fish&method=run-length-encoding&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fish - Run length encoding - a4"
        )

    def test_subtitle_fish_run_length_letter(self):
        query = QueryDict("image=fish&method=run-length-encoding&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fish - Run length encoding - letter"
        )

    def test_subtitle_fish_greyscale_a4(self):
        query = QueryDict("image=fish&method=greyscale&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fish - Greyscale - a4"
        )

    def test_subtitle_fish_greyscale_letter(self):
        query = QueryDict("image=fish&method=greyscale&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fish - Greyscale - letter"
        )

    def test_subtitle_fish_colour_a4(self):
        query = QueryDict("image=fish&method=colour&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fish - Colour - a4"
        )

    def test_subtitle_fish_colour_letter(self):
        query = QueryDict("image=fish&method=colour&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fish - Colour - letter"
        )

    def test_subtitle_parrots_binary_a4(self):
        query = QueryDict("image=parrots&method=black-white&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Parrots - Black and White - a4"
        )

    def test_subtitle_parrots_binary_letter(self):
        query = QueryDict("image=parrots&method=black-white&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Parrots - Black and White - letter"
        )

    def test_subtitle_parrots_run_length_a4(self):
        query = QueryDict("image=parrots&method=run-length-encoding&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Parrots - Run length encoding - a4"
        )

    def test_subtitle_parrots_run_length_letter(self):
        query = QueryDict("image=parrots&method=run-length-encoding&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Parrots - Run length encoding - letter"
        )

    def test_subtitle_parrots_greyscale_a4(self):
        query = QueryDict("image=parrots&method=greyscale&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Parrots - Greyscale - a4"
        )

    def test_subtitle_parrots_greyscale_letter(self):
        query = QueryDict("image=parrots&method=greyscale&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Parrots - Greyscale - letter"
        )

    def test_subtitle_parrots_colour_a4(self):
        query = QueryDict("image=parrots&method=colour&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Parrots - Colour - a4"
        )

    def test_subtitle_parrots_colour_letter(self):
        query = QueryDict("image=parrots&method=colour&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Parrots - Colour - letter"
        )

    def test_subtitle_hot_air_balloon_binary_a4(self):
        query = QueryDict("image=hot-air-balloon&method=black-white&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hot air balloon - Black and White - a4"
        )

    def test_subtitle_hot_air_balloon_binary_letter(self):
        query = QueryDict("image=hot-air-balloon&method=black-white&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hot air balloon - Black and White - letter"
        )

    def test_subtitle_hot_air_balloon_run_length_a4(self):
        query = QueryDict("image=hot-air-balloon&method=run-length-encoding&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hot air balloon - Run length encoding - a4"
        )

    def test_subtitle_hot_air_balloon_run_length_letter(self):
        query = QueryDict("image=hot-air-balloon&method=run-length-encoding&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hot air balloon - Run length encoding - letter"
        )

    def test_subtitle_hot_air_balloon_greyscale_a4(self):
        query = QueryDict("image=hot-air-balloon&method=greyscale&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hot air balloon - Greyscale - a4"
        )

    def test_subtitle_hot_air_balloon_greyscale_letter(self):
        query = QueryDict("image=hot-air-balloon&method=greyscale&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hot air balloon - Greyscale - letter"
        )

    def test_subtitle_hot_air_balloon_colour_a4(self):
        query = QueryDict("image=hot-air-balloon&method=colour&paper_size=a4")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hot air balloon - Colour - a4"
        )

    def test_subtitle_hot_air_balloon_colour_letter(self):
        query = QueryDict("image=hot-air-balloon&method=colour&paper_size=letter")
        generator = PixelPainterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hot air balloon - Colour - letter"
        )
