"""Test class for TextBoxDrawer."""

import os
import math
from PIL import ImageFont, Image, ImageDraw
from lxml import etree as ET
from django.test import SimpleTestCase
from django.utils import translation
from utils.TextBoxDrawer import TextBoxDrawer, TextBox, DEFAULT_FONT
from utils.errors.TextBoxDrawerErrors import (
    MissingSVGFile,
    TextBoxNotFoundInSVG
)

BASE_PATH = "tests/utils/text_box_drawer"


class TextBoxDrawerTest(SimpleTestCase):

    def test_initialisation_no_svg(self):
        image = Image.new("RGB", (2000, 4000))
        TextBoxDrawer(image, None)

    def test_initialisation_basic_svg(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (2000, 4000))
        tbd = TextBoxDrawer(image, None, svg)
        self.assertIsInstance(tbd.svg, ET._Element)
        self.assertAlmostEqual(tbd.width_ratio, 2)
        self.assertAlmostEqual(tbd.height_ratio, 4)

    def test_initialisation_missing_svg(self):
        svg = os.path.join(BASE_PATH, "missing.svg")
        image = Image.new("RGB", (1000, 1000))
        with self.assertRaises(MissingSVGFile):
            TextBoxDrawer(image, None, svg)

    def test_get_box_core(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        # In PNG Space, x is *2, and y is *4 from SVG Space
        image = Image.new("RGB", (2000, 4000))
        tbd = TextBoxDrawer(image, None, svg)
        box = tbd.get_box("box1")

        self.assertIsInstance(box, TextBox)
        self.assertIsInstance(box.vertices, list)
        self.assertEqual(4, len(box.vertices))
        x, y = box.vertices[0]
        # SVG x=100, *2 to convert into PNG space
        self.assertAlmostEqual(2 * 100, x)
        # SVG y=200, *4 to convert into PNG space
        self.assertAlmostEqual(4 * 200, y)
        # SVG width=50, *2 to convert into PNG space
        self.assertAlmostEqual(2 * 50.0, box.width)
        # SVG height=75, *4 to convert into PNG space
        self.assertAlmostEqual(4 * 75.0, box.height)
        self.assertEqual("#006838", box.color)
        self.assertEqual("static/fonts/PatrickHand-Regular.ttf", box.font_path)
        # SVG font size is 48px, converted into PNG space
        self.assertEqual(4 * 48, box.font_size)
        self.assertIsInstance(box.font_size, int)
        self.assertEqual(0, box.angle)

    def test_get_box_id_on_rect_element(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (2000, 4000))
        tbd = TextBoxDrawer(image, None, svg)
        tbd.get_box("onrectangle")

    def test_get_box_invalid_id(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (2000, 4000))
        tbd = TextBoxDrawer(image, None, svg)
        with self.assertRaises(TextBoxNotFoundInSVG):
            tbd.get_box("invalid")

    def test_get_box_id_with_digit(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (2000, 4000))
        tbd = TextBoxDrawer(image, None, svg)
        tbd.get_box("element2")

    def test_get_box_id_start_with_digit(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (2000, 4000))
        tbd = TextBoxDrawer(image, None, svg)
        tbd.get_box("123")

    def test_get_box_id_with_underscore(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (2000, 4000))
        tbd = TextBoxDrawer(image, None, svg)
        tbd.get_box("element_2")

    def text_get_box_with_tspan(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (1000, 1000))
        tbd = TextBoxDrawer(image, None, svg)
        box = tbd.get_box("withtspan")
        self.assertEqual("#414042", box.color)
        self.assertEqual("static/fonts/PatrickHand-Regular.ttf", box.font_path)
        self.assertEqual(48, box.font_size)
        self.assertIsInstance(box.font_size, int)

    def text_get_box_without_style(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (1000, 1000))
        tbd = TextBoxDrawer(image, None, svg)
        box = tbd.get_box("withoutstyle")
        self.assertEqual(None, box.color)
        self.assertEqual(None, box.font_path)
        self.assertEqual(None, box.font_size)

    def test_get_box_rotated(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (1000, 1000))
        tbd = TextBoxDrawer(image, None, svg)
        box = tbd.get_box("rotated")
        self.assertAlmostEqual(math.radians(45.0), box.angle, places=3)

        # Check location of bottom left corner
        bottomleft_x, bottomleft_y = box.vertices[3]
        self.assertAlmostEqual(bottomleft_x, 1/math.sqrt(2) * box.width, places=1)
        self.assertAlmostEqual(bottomleft_y, 1/math.sqrt(2) * box.height, places=1)

    def test_fallback_font_if_required_valid_font(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (1000, 1000))
        tbd = TextBoxDrawer(image, None, svg)
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font = tbd.fallback_font_if_required(font_path, "abc")
        self.assertEqual(font_path, font)

    def test_fallback_font_if_required_ordinal_too_high(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (1000, 1000))
        tbd = TextBoxDrawer(image, None, svg)
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        new_font_path = tbd.fallback_font_if_required(font_path, chr(300))
        self.assertNotEqual(font_path, new_font_path)
        self.assertEqual(DEFAULT_FONT, new_font_path)

    def test_fallback_font_none_given(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (1000, 1000))
        tbd = TextBoxDrawer(image, None, svg)
        font_path = tbd.fallback_font_if_required(None, "abc")
        self.assertEqual(DEFAULT_FONT, font_path)

    def test_fit_text_one_line(self):
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font_size = 50
        font = ImageFont.truetype(font_path, font_size)
        text = "This is a string"
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        new_font_size, lines, new_text_width, new_text_height = TextBoxDrawer.fit_text(
            text,
            text_width * 2,
            text_height * 2,
            font_path,
            font_size,
            4
        )

        self.assertEqual(1, len(lines))
        self.assertEqual(text, lines[0])
        self.assertEqual(font_size, new_font_size)
        self.assertIsInstance(new_text_width, int)
        self.assertIsInstance(new_text_height, int)

    def test_fit_text_multiline(self):
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font_size = 50
        font = ImageFont.truetype(font_path, font_size)
        text = "This is a string"
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        new_font_size, lines, new_text_width, new_text_height = TextBoxDrawer.fit_text(
            text,
            text_width * 0.8,  # Make box slightly narrower than text, to force 2 lines
            text_height * 5,
            font_path,
            font_size,
            4
        )
        self.assertEqual(2, len(lines))
        self.assertEqual(text, "".join(lines))
        self.assertEqual(font_size, new_font_size)
        self.assertIsInstance(new_text_width, int)
        self.assertIsInstance(new_text_height, int)

    def test_fit_text_decrease_fontsize(self):
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font_size = 50
        font = ImageFont.truetype(font_path, font_size)
        text = "This is a string"
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        new_font_size, lines, new_text_width, new_text_height = TextBoxDrawer.fit_text(
            text,
            text_width * 0.8,  # Make box slightly narrower than text, to force 2 lines
            text_height,  # Make box too short to force smaller text
            font_path,
            font_size,
            4
        )
        self.assertEqual(text, "".join(lines))
        self.assertTrue(new_font_size < font_size)
        self.assertTrue(new_font_size > 1)
        self.assertIsInstance(new_text_width, int)
        self.assertIsInstance(new_text_height, int)

    def test_fit_text_valid_fontsize(self):
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font_size = 10
        text = "This is a string"
        font = ImageFont.truetype(font_path, font_size * 2)
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        new_font_size, lines, new_text_width, new_text_height = TextBoxDrawer.fit_text(
            text,
            text_width,
            text_height,
            font_path,
            font_size,
            4
        )
        self.assertEqual(new_font_size, font_size)

    def test_fit_text_one_decrease_loop(self):
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font_size = 10
        text = "This is a string"
        font = ImageFont.truetype(font_path, font_size)
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        new_font_size, lines, new_text_width, new_text_height = TextBoxDrawer.fit_text(
            text,
            text_width - 1,  # Force one decrease loop
            text_height,
            font_path,
            font_size,
            4
        )
        self.assertTrue(new_font_size < font_size)

    def test_fit_text_multiple_decrease_loop(self):
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font_size = 100
        text = "This is a string"
        font = ImageFont.truetype(font_path, font_size)
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        new_font_size, lines, new_text_width, new_text_height = TextBoxDrawer.fit_text(
            text,
            text_width * 0.5,  # Force many decrease loops
            text_height,
            font_path,
            font_size,
            4
        )
        self.assertTrue(new_font_size < font_size)

    def test_fit_text_no_text(self):
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font_size = 10
        text = ""
        font = ImageFont.truetype(font_path, font_size)
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        new_font_size, lines, new_text_width, new_text_height = TextBoxDrawer.fit_text(
            text,
            text_width,
            text_height,
            font_path,
            font_size,
            4
        )
        self.assertEqual(new_font_size, 0)
        self.assertEqual(lines, "")
        self.assertEqual(new_text_width, 0)
        self.assertEqual(new_text_height, 0)

    def test_fit_text_smoke_test_one_word(self):
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font_size = 10
        text = "word"
        font = ImageFont.truetype(font_path, font_size)
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        new_font_size, lines, new_text_width, new_text_height = TextBoxDrawer.fit_text(
            text,
            text_width,
            text_height,
            font_path,
            font_size,
            4
        )

    def test_write_text_box_defaults_smoke_test(self):
        image = Image.new("RGB", (2000, 4000))
        draw = ImageDraw.Draw(image)
        tbd = TextBoxDrawer(image, draw)
        vertices = [
            (0, 0), (200, 0), (200, 100), (0, 100)
        ]
        width = 200
        height = 100
        box = TextBox(vertices, width, height)
        tbd.write_text_box(
            box,
            "This is a string",
        )

    def test_write_text_box_object_defaults_smoke_test(self):
        image = Image.new("RGB", (1000, 1000))
        draw = ImageDraw.Draw(image)
        vertices = [
            (0, 0), (200, 0), (200, 100), (0, 100)
        ]
        width = 200
        height = 100
        box = TextBox(vertices, width, height)
        TextBoxDrawer.write_text_box_object(
            image,
            draw,
            box,
            "This is a string",
        )

    def test_write_text_box_object_justification_smoke_test(self):
        image = Image.new("RGB", (1000, 1000))
        draw = ImageDraw.Draw(image)
        vertices = [
            (0, 0), (200, 0), (200, 100), (0, 100)
        ]
        width = 200
        height = 100
        box = TextBox(vertices, width, height)
        for horiz_just in ["left", "center", "right"]:
            for vert_just in ["top", "center", "bottom"]:
                TextBoxDrawer.write_text_box_object(
                    image,
                    draw,
                    box,
                    "This is a string",
                    horiz_just=horiz_just,
                    vert_just=vert_just,
                )
        with translation.override("he"):
            for horiz_just in ["left", "center", "right"]:
                for vert_just in ["top", "center", "bottom"]:
                    TextBoxDrawer.write_text_box_object(
                        image,
                        draw,
                        box,
                        "עברית‬",
                        horiz_just=horiz_just,
                        vert_just=vert_just,
                    )

    def test_write_text_box_object_params_smoke_test(self):
        image = Image.new("RGB", (1000, 1000))
        draw = ImageDraw.Draw(image)
        vertices = [
            (0, 0), (200, 0), (200, 100), (0, 100)
        ]
        width = 200
        height = 100
        box = TextBox(vertices, width, height)
        TextBoxDrawer.write_text_box_object(
            image,
            draw,
            box,
            "This is a string",
            font_path="static/fonts/PatrickHand-Regular",
            font_size=17,
            line_spacing=10,
            color="#013291"
        )

    def test_write_text_box_object_rotated_smoke_test(self):
        image = Image.new("RGB", (1000, 1000))
        draw = ImageDraw.Draw(image)
        vertices = [
            (0, 200), (0, 0), (100, 0), (100, 200)
        ]
        width = 200
        height = 100
        rotation = 90
        box = TextBox(vertices, width, height, angle=rotation)
        TextBoxDrawer.write_text_box_object(
            image,
            draw,
            box,
            "This is a string",
        )

    def test_default_font_override_ja(self):
        image = Image.new("RGB", (2000, 4000))
        draw = ImageDraw.Draw(image)
        tbd = TextBoxDrawer(image, draw)
        with translation.override("ja"):
            self.assertEqual(
                tbd.get_default_font(),
                "static/fonts/NotoSansCJKjp-Regular.otf"
            )

    def test_default_font_override_he(self):
        image = Image.new("RGB", (2000, 4000))
        draw = ImageDraw.Draw(image)
        tbd = TextBoxDrawer(image, draw)
        with translation.override("he"):
            self.assertEqual(
                tbd.get_default_font(),
                "static/fonts/OpenSansHebrew-Regular.ttf"
            )

    def test_default_font_override_ar(self):
        image = Image.new("RGB", (2000, 4000))
        draw = ImageDraw.Draw(image)
        tbd = TextBoxDrawer(image, draw)
        with translation.override("ar"):
            self.assertEqual(
                tbd.get_default_font(),
                "static/fonts/DejaVuSans.ttf"
            )
