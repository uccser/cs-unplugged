"""Test class for TextBoxDrawer."""

from django.test import SimpleTestCase
from utils.TextBoxDrawer import TextBoxDrawer, TextBox, DEFAULT_FONT
from PIL import ImageFont, Image, ImageDraw
from lxml import etree as ET
import os
import math
from utils.errors.TextBoxDrawerErrors import (
    MissingSVGFile,
    TextBoxNotFoundInSVG
)

BASE_PATH = "tests/utils/text_box_drawer"

class TextBoxDrawerTest(SimpleTestCase):

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
            tbd = TextBoxDrawer(image, None, svg)

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
        box = tbd.get_box("onrectangle")

    def test_get_box_invalid_id(self):
        svg = os.path.join(BASE_PATH, "basic.svg")
        image = Image.new("RGB", (2000, 4000))
        tbd = TextBoxDrawer(image, None, svg)
        with self.assertRaises(TextBoxNotFoundInSVG):
            box = tbd.get_box("invalid")

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

    # def test_fit_text_one_line(self):
    #
    # def test_fit_text_multiline(self):
    #
    # def test_fit_text_decrease_fontsize(self):
    #
    # def test_write_text_box_object_basic(self):
    #
    # def test_write_text_box_object_rotated(self):
