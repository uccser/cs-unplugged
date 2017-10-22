"""Class for Treasure Hunt resource generator."""

from PIL import Image, ImageDraw, ImageFont
from random import sample
from utils.BaseResourceGenerator import BaseResourceGenerator

IMAGE_PATH = "static/img/resources/treasure-hunt/{}.png"


class TreasureHuntResourceGenerator(BaseResourceGenerator):
    """Class for Treasure Hunt resource generator."""

    additional_valid_options = {
        "prefilled_values": ["blank", "easy", "medium", "hard"],
        "number_order": ["sorted", "unsorted"],
        "instructions": [True, False],
        "art": ["colour", "bw"],
    }

    def __init__(self, requested_options=None):
        """Constructor for BaseResourceGenerator.

        Args:
            request: HTTP request object (HttpRequest).
        """
        # TODO: Call super __init__
        self.valid_options = BaseResourceGenerator.default_valid_options
        self.valid_options.update(self.additional_valid_options)
        if requested_options:
            self.requested_options = self.process_requested_options(requested_options)
            self.check_requested_options()
            self.set_number_range()

    def data(self):
        """Create data for a copy of the Treasure Hunt resource.

        Returns:
            A dictionary of the two pages for the resource.
        """
        pages = []
        font_path = "static/fonts/PatrickHand-Regular.ttf"

        prefilled_values = self.requested_options["prefilled_values"]
        number_order = self.requested_options["number_order"]
        instructions = self.requested_options["instructions"]
        art_style = self.requested_options["art"]

        if instructions:
            image = Image.open(IMAGE_PATH.format("instructions"))
            ImageDraw.Draw(image)
            pages.append({"type": "image", "data": image})

        image = Image.open(IMAGE_PATH.format(art_style))
        draw = ImageDraw.Draw(image)

        # Add numbers to image if required
        if prefilled_values != "blank":
            font = ImageFont.truetype(font_path, self.font_size)

            total_numbers = 26
            numbers = sample(range(self.range_min, self.range_max), total_numbers)
            if number_order == "sorted":
                numbers.sort()

            base_coord_y = 506
            coord_y_increment = 199
            base_coords_x = [390, 700]
            for i in range(0, total_numbers):
                text = str(numbers[i])
                text_width, text_height = draw.textsize(text, font=font)

                coord_x = base_coords_x[i % 2] - (text_width / 2)
                coord_y = base_coord_y - (text_height / 2)
                if i % 2 == 1:
                    coord_y -= 10
                    base_coord_y += coord_y_increment
                draw.text(
                    (coord_x, coord_y),
                    text,
                    font=font,
                    fill="#000"
                )

            text = "{} - {} to {}".format(number_order.title(), self.range_min, self.range_max - 1)
            font = ImageFont.truetype(font_path, 75)
            text_width, text_height = draw.textsize(text, font=font)
            coord_x = 1220 - (text_width / 2)
            coord_y = 520 - (text_height / 2)
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill="#000",
            )
        pages.append({"type": "image", "data": image})
        return pages

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str)
        """
        prefilled_values = self.requested_options["prefilled_values"]
        number_order = self.requested_options["number_order"]
        instructions = self.requested_options["instructions"]
        art_style = self.requested_options["art"]

        if prefilled_values == "blank":
            range_text = "blank"
        else:
            SUBTITLE_TEMPLATE = "{} - {} to {}"
            number_order_text = number_order.title()
            range_text = SUBTITLE_TEMPLATE.format(number_order_text, self.range_min, self.range_max - 1)

        if art_style == "colour":
            art_style_text = "full colour"
        else:
            art_style_text = "black and white"

        if instructions:
            instructions_text = "with instructions"
        else:
            instructions_text = "without instructions"

        return "{} - {} - {} - {}".format(range_text, art_style_text, instructions_text, super().subtitle)

    def set_number_range(self):
        """Return number range tuple for resource.

        Args:
            request: HTTP request object (HttpRequest).

        Returns:
            Tuple of (range_min, range_max, font_size)
        """
        prefilled_values = self.requested_options.get("prefilled_values", None)
        self.range_min = 0
        if prefilled_values == "easy":
            self.range_max = 100
            self.font_size = 55
        elif prefilled_values == "medium":
            self.range_max = 1000
            self.font_size = 50
        elif prefilled_values == "hard":
            self.range_max = 10000
            self.font_size = 45
