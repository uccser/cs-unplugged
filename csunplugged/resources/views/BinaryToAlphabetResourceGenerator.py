"""Class for Binary to Alphabet resource generator."""

from PIL import Image, ImageDraw, ImageFont
from utils.BaseResourceGenerator import BaseResourceGenerator


class BinaryToAlphabetResourceGenerator(BaseResourceGenerator):
    """Class for Binary to Alphabet resource generator."""

    additional_valid_options = {
        "worksheet_version": ["student", "teacher"],
    }


    def data(self):
        """Create a image for Binary to Alphabet resource.

        Returns:
            A dictionary for the resource page.
        """
        # Retrieve relevant image
        worksheet_version = self.requested_options["worksheet_version"]
        if worksheet_version == "student":
            image_path = "static/img/resources/binary-to-alphabet/table.png"
        else:
            image_path = "static/img/resources/binary-to-alphabet/table-teacher.png"
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        font_size = 30
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font = ImageFont.truetype(font_path, font_size)

        # Draw headings
        column_headings = ["Base 10", "Binary", "Letter"]
        heading_coord_x = 18
        heading_coord_y = 6

        i = 0
        while i < 9:  # 9 = number of columns

            if i % 3 == 0:
                text = str(column_headings[0])
            elif i % 3 == 1:
                text = str(column_headings[1])
            else:
                text = str(column_headings[2])

            draw.text(
                (heading_coord_x, heading_coord_y),
                text,
                font=font,
                fill="#000"
            )

            heading_coord_x += 113

            i += 1

        # Draw numbers
        # Column data: (min number, max number), x coord
        columns_data = [((0, 9), 58), ((9, 18), 397), ((18, 27), 736)]

        for column_set in columns_data:
            start, end = column_set[0]
            base_coord_x = column_set[1]
            base_coord_y = 75

            for number in range(start, end):
                text = str(number)
                text_width, text_height = draw.textsize(text, font=font)
                coord_x = base_coord_x - (text_width / 2)
                coord_y = base_coord_y - (text_height / 2)

                draw.text(
                    (coord_x, coord_y),
                    text,
                    font=font,
                    fill="#000"
                )

                base_coord_y += 54

        image = image.rotate(90, expand=True)
        return {"type": "image", "data": image}

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            Text for subtitle (str).
        """
        text = "{} - {}".format(
            self.requested_options["worksheet_version"],
            super().subtitle
        )
        return text
