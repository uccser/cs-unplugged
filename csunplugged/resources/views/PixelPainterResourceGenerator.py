"""Class for Pixel Painter resource generator."""

from PIL import Image, ImageDraw, ImageFont
from math import ceil
from yattag import Doc
import string
from utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext as _


class PixelPainterResourceGenerator(BaseResourceGenerator):
    """Class for Pixel Painter resource generator."""

    additional_valid_options = {
        "method": ["black-white", "run-length-encoding", "greyscale", "colour"],
        "image": ["boat", "fish", "hot-air-balloon", "parrots"],
    }

    methods = {
        "black-white": {
            "name": _("Black and White"),
            "labels": {
                255: "0",
                0: "1"
            }
        },
        "run-length-encoding": {
            "name": _("Run length encoding"),
            "labels": {
                255: "0",
                0: "1"
            }
        },
        "greyscale": {
            "name": _("Greyscale"),
            "labels": {
                255: "00",
                168: "01",
                84: "10",
                0: "11"
            }
        },
        "colour": {
            "name": _("Colour"),
            "labels": {
                (255, 255, 255): "11111",  # White
                (0, 0, 0):       "00000",  # Black
                (255, 0, 0):     "11000",  # Red
                (255, 143, 0):   "11100",  # Orange
                (255, 243, 0):   "11110",  # Yellow
                (76, 219, 5):    "00110",  # Green
                (0, 162, 255):   "00001",  # Blue
                (138, 0, 255):   "10001"   # Purple
            }
        }
    }

    image_strings = {
        "boat": _("Boat"),
        "fish": _("Fish"),
        "hot-air-balloon": _("Hot air balloon"),
        "parrots": _("Parrots"),
    }

    STATIC_PATH = "static/img/resources/pixel-painter/{}"

    def data(self):
        """Create data for a copy of the Pixel Painter resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
        FONT = ImageFont.truetype(FONT_PATH, 80)
        FONT_SMALL = ImageFont.truetype(FONT_PATH, 50)
        TEXT_COLOUR = "#888"

        method = self.requested_options["method"]
        image_name = self.requested_options["image"]

        if method == "run-length-encoding":
            image_filename = "{}-black-white.png".format(image_name)
        else:
            image_filename = "{}-{}.png".format(image_name, method)
        image = Image.open(self.STATIC_PATH.format(image_filename))
        (image_width, image_height) = image.size

        COLUMNS_PER_PAGE = 15
        ROWS_PER_PAGE = 20
        BOX_SIZE = 200
        IMAGE_SIZE_X = BOX_SIZE * COLUMNS_PER_PAGE
        IMAGE_SIZE_Y = BOX_SIZE * ROWS_PER_PAGE
        LINE_COLOUR = "#666"
        LINE_WIDTH = 1

        pages = []
        if method == "run-length-encoding":
            pages_encoding = dict()

        number_column_pages = ceil(image_width / COLUMNS_PER_PAGE)
        number_row_pages = ceil(image_height / ROWS_PER_PAGE)
        page_grid_coords = self.create_page_grid_coords(number_column_pages, number_row_pages, image_name)

        grid_page = self.grid_reference_page(page_grid_coords, image_name)
        pages.append({"type": "html", "data": grid_page})

        # For each page row
        for number_row_page in range(0, number_row_pages):
            page_start_row = (number_row_page) * ROWS_PER_PAGE
            # For each page column
            for number_column_page in range(0, number_column_pages):
                page_start_column = (number_column_page) * COLUMNS_PER_PAGE
                # Create page
                page = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#fff")
                draw = ImageDraw.Draw(page)
                page_columns = min(COLUMNS_PER_PAGE, image_width - page_start_column)
                page_rows = min(ROWS_PER_PAGE, image_height - page_start_row)
                page_reference = page_grid_coords[number_row_page][number_column_page]
                page_reference_added = False

                if method == "run-length-encoding":
                    page_encoding = []

                # Draw grid
                grid_width = page_columns * BOX_SIZE
                grid_height = page_rows * BOX_SIZE

                for x_coord in range(0, page_columns * BOX_SIZE, BOX_SIZE):
                    draw.line(
                        [(x_coord, 0), (x_coord, grid_height)],
                        fill=LINE_COLOUR,
                        width=LINE_WIDTH
                    )
                draw.line(
                    [(page_columns * BOX_SIZE - 1, 0), (page_columns * BOX_SIZE - 1, grid_height)],
                    fill=LINE_COLOUR,
                    width=LINE_WIDTH
                )

                for y_coord in range(0, grid_height, BOX_SIZE):
                    draw.line(
                        [(0, y_coord), (grid_width, y_coord)],
                        fill=LINE_COLOUR,
                        width=LINE_WIDTH
                    )
                draw.line(
                    [(0, grid_height - 1), (grid_width, grid_height - 1)],
                    fill=LINE_COLOUR,
                    width=LINE_WIDTH
                )

                for row in range(0, page_rows):
                    if method == "run-length-encoding":
                        row_encoding = []
                        encoding_colour = "0"
                        encoding_count = 0

                    for column in range(0, page_columns):
                        pixel_value = image.getpixel((page_start_column + column, page_start_row + row))

                        try:
                            text = self.methods[method]["labels"][pixel_value]
                        except KeyError:
                            message = "Image: {}\n".format(image_name)
                            message += "Method: {}\n".format(method)
                            message += "Contains invalid pixel value: {}".format(pixel_value)
                            raise ValueError(message)

                        # Draw text
                        if method != "run-length-encoding":
                            text_width, text_height = draw.textsize(text, font=FONT)
                            text_coord_x = (column * BOX_SIZE) + (BOX_SIZE / 2) - (text_width / 2)
                            text_coord_y = (row * BOX_SIZE) + (BOX_SIZE / 2) - (text_height / 2)
                            draw.text(
                                (text_coord_x, text_coord_y),
                                text,
                                font=FONT,
                                fill=TEXT_COLOUR
                            )
                        else:
                            if text != encoding_colour:
                                row_encoding.append(encoding_count)
                                if text != encoding_colour:
                                    if encoding_colour == "0":
                                        encoding_colour = "1"
                                    else:
                                        encoding_colour = "0"
                                    encoding_count = 0
                            encoding_count += 1
                            if page_columns - 1 == column:
                                row_encoding.append(encoding_count)

                        # Add page grid reference
                        if isinstance(pixel_value, tuple):
                            pixel_value = pixel_value[-1]

                        if not page_reference_added and pixel_value > 0:
                            draw.text(
                                ((column * BOX_SIZE) + LINE_WIDTH * 4, (row * BOX_SIZE) + -4),
                                page_reference,
                                font=FONT_SMALL,
                                fill="#000"
                            )
                            page_reference_added = True
                    if method == "run-length-encoding":
                        page_encoding.append(row_encoding)
                if method == "run-length-encoding":
                    pages_encoding[page_reference] = page_encoding
                pages.append({"type": "image", "data": page})

        # Set first page of grid as thumbnail
        pages[1]["thumbnail"] = True

        if method == "run-length-encoding":
            encoding_html = self.create_run_length_encoding_html(page_grid_coords, pages_encoding)
            pages.insert(1, {"type": "html", "data": encoding_html})
        return pages

    def create_page_grid_coords(self, columns, rows, image):
        """Create a grid of page coordinates in a 2D array.

        Example:
            When asked for a grid for a 3x2 page grid, the result is:
            grid = [
             ["A1", "A2", "A3"],
             ["B1", "B2", "B3"]
            ]
            grid[0][0] = "A1"
            grid[0][1] = "A2"
            grid[2][1] = "C2"

            The first value refers to the image used.

        Args:
            columns: Number of page columns (int).
            rows: Number of page rows (int).
            image: Name of the image used (str).

        Returns:
            A 2D list containing page grid references as strings (list).
        """
        image_number = self.additional_valid_options["image"].index(image)
        LETTERS = string.ascii_uppercase
        page_grid_coords = [[""] * columns for i in range(rows)]
        for row in range(0, rows):
            for column in range(0, columns):
                page_grid_coords[row][column] = "{}{}{}".format(image_number, LETTERS[row], column + 1)
        return page_grid_coords

    def grid_reference_page(self, page_grid_coords, image_name):
        """Create page grid reference HTML.

        Args:
            page_grid_coords: A 2D list containing the page grid as strings (list).
            image_name: The name of the image used in this resource (str).

        Returns:
            HTML string for the grid reference page.
        """
        doc, tag, text, line = Doc().ttl()
        line("style", "#grid-table td {border:1px solid black;padding:1rem 0.5rem;}")
        with tag("h1"):
            text("Pixel Painter")
        with tag("h2"):
            text("Page grid reference for {} image".format(image_name))
        with tag("p"):
            text(
                "Once pixels on each page are filled in correctly, ",
                "cut each grid out and arrange in the following layout ",
                "(page names are in the top right corner)."
            )
        with tag("table", id="grid-table"):
            with tag("tbody"):
                for row_num in range(0, len(page_grid_coords)):
                    with tag("tr"):
                        for column_num in range(0, len(page_grid_coords[row_num])):
                            line("td", page_grid_coords[row_num][column_num])
        return doc.getvalue()

    def create_run_length_encoding_html(self, page_grid_coords, pages_encoding):
        """Create page HTML for run length encoding.

        Args:
            page_grid_coords: A 2D list containing the page grid as strings (list).
            pages_encoding: Dictionary of page references to list of run length encodings (dict).

        Returns:
            HTML string for the run length encoding page.
        """
        doc, tag, text, line = Doc().ttl()
        line("style", ".avoid-page-break {page-break-inside:avoid;}")
        with tag("h1"):
            text("Run Length Encodings")
        for index, row_of_page_references in enumerate(page_grid_coords):
            for page_reference in row_of_page_references:
                with tag("div", klass="avoid-page-break"):
                    with tag("h2"):
                        text("Encoding for page {}".format(page_reference))
                    page_encoding = pages_encoding[page_reference]
                    with tag("ul", klass="list-unstyled"):
                        for line_values in page_encoding:
                            line("li", ", ".join(str(number) for number in line_values))
        return doc.getvalue()

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        text = "{} - {} - {}".format(
            self.image_strings[self.requested_options["image"]],
            self.methods[self.requested_options["method"]]["name"],
            super().subtitle
        )
        return text

    def thumbnail(self):
        """Return thumbnail for resource request.

        Returns:
            Image for resource thumbnail.
        """
        method = self.requested_options["method"]
        image_name = self.requested_options["image"]

        if method == "run-length-encoding":
            image_filename = "{}-black-white.png".format(image_name)
        else:
            image_filename = "{}-{}.png".format(image_name, method)
        return Image.open(self.STATIC_PATH.format(image_filename))
