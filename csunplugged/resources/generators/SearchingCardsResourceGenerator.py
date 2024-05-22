"""Class for Searching Cards resource generator."""

from random import sample, shuffle
from math import ceil
from PIL import Image, ImageDraw, ImageFont
from yattag import Doc
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter, BoolResourceParameter

IMAGE_PATH = "static/img/resources/searching-cards/{}-cards-{}.png"
X_BASE_COORD = 1803
X_COORD_DECREMENT = 516
Y_COORD = 200
FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
FONT = ImageFont.truetype(FONT_PATH, 200)

NUMBER_CARDS_VALUES = {
    "15": "15",
    "31": "31",
}
MIN_VALUE = 1
MAX_NUMBER_VALUE = {
    "cards": _("Number of cards (15 or 31)"),
    "99": _("1 to 99"),
    "999": _("1 to 999"),
    "blank": _("Blank")
}


class SearchingCardsResourceGenerator(BaseResourceGenerator):
    """Class for Searching Cards resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for SearchingCardsResourceGenerator."""
        return {
            "number_cards": EnumResourceParameter(
                name="number_cards",
                description=_("Number of cards"),
                values=NUMBER_CARDS_VALUES,
                default="15"
            ),
            "max_number": EnumResourceParameter(
                name="max_number",
                description=_("Range of numbers"),
                values=MAX_NUMBER_VALUE,
                default="number"
            ),
            "help_sheet": BoolResourceParameter(
                name="help_sheet",
                description=_("Include teacher guide sheet"),
                default=True
            ),
        }

    def data(self):
        """Create a image for Searching Cards resource.

        Returns:
            A list of dictionaries for each resource page.
        """
        pages = []
        number_cards = int(self.options["number_cards"].value)
        max_number = self.options["max_number"].value
        help_sheet = self.options["help_sheet"].value

        if max_number == "cards":
            numbers = list(range(MIN_VALUE, number_cards + 1))
            shuffle(numbers)
            range_text = _("{} to {}").format(MIN_VALUE, number_cards)
        elif max_number != "blank":
            numbers = sample(range(MIN_VALUE, int(max_number) + 1), number_cards)
            range_text = _("{} to {}").format(MIN_VALUE, max_number)
        else:
            numbers = []
            range_text = _("Add list of numbers below:")

        if help_sheet:
            pages.append({"type": "html", "data": self.create_help_sheet(numbers, range_text)})

        number_of_pages = range(ceil(number_cards / 4))
        for (page_number, page) in enumerate(number_of_pages):
            if page == number_of_pages[-1]:
                image_path = IMAGE_PATH.format(3, 1)
            else:
                image_path = IMAGE_PATH.format(4, page + 1)

            image = Image.open(image_path)

            if max_number != "blank":
                draw = ImageDraw.Draw(image)
                page_numbers = numbers[:4]
                numbers = numbers[4:]
                coord_x = X_BASE_COORD
                for number in page_numbers:
                    text = str(number)
                    left, top, right, bottom = draw.textbbox((0, 0), text, font=FONT)
                    text_width, text_height = right - left, bottom - top
                    draw.text(
                        (coord_x - (text_width / 2), Y_COORD - (text_height / 2)),
                        text,
                        font=FONT,
                        fill="#000"
                    )
                    coord_x -= X_COORD_DECREMENT

            image = image.rotate(90, expand=True)
            page_data = {"type": "image", "data": image}
            if page_number == 0:
                page_data["thumbnail"] = True
            pages.append(page_data)
        return pages

    def create_help_sheet(self, numbers, range_text):
        """Create helper sheet for resource.

        Args:
            numbers: Numbers used for activity (list).
            range_text: String describing range of numbers (str).

        Returns:
            Pillow image object (Image).
        """
        doc, tag, text, line = Doc().ttl()
        with tag("div"):
            with tag("h1"):
                text(_("Teacher guide sheet for binary search activity"))
            with tag("p"):
                text(_(
                    "Use this sheet to circle the number you are asking your class "
                    "to look for when you are demonstrating how the binary search "
                    "works. This allows you to demonstrate the maximum number of "
                    "searches it would take. When students are playing the number "
                    "hunt game, they can choose any number. Avoid those numbers that are "
                    "underlined as they are key binary search positions (avoiding them is a "
                    "good thing to do for demonstrations, but in practice students, "
                    "or computers, won’t intentionally avoid these)."
                ))
            with tag("h2"):
                text(_("Sorted numbers"))
            with tag("p"):
                with tag("em"):
                    text(range_text)
            with tag("p"):
                numbers.sort()
                red_number_jump = (len(numbers) + 1) // 4
                text = ""
                for (index, number) in enumerate(numbers):
                    if (index + 1) % red_number_jump == 0:
                        text += "<u>{}</u> - ".format(number)
                    else:
                        text += "{} - ".format(number)
                text = text[:-3]
                doc.asis(text)
        return doc.getvalue()

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        max_number = self.options["max_number"].value
        help_sheet = self.options["help_sheet"].value
        number_cards = self.options["number_cards"].value

        if max_number == "blank":
            range_text = _("Blank")
        elif max_number == "cards":
            range_text = _("{} to {}").format(MIN_VALUE, number_cards)
        else:
            range_text = _("{} to {}").format(MIN_VALUE, max_number)

        if help_sheet:
            help_text = _("with helper sheet")
        else:
            help_text = _("without helper sheet")
        text = " - ".join([
            _("{} cards").format(number_cards),
            str(range_text),
            str(help_text),
            super().subtitle
        ])
        return text
