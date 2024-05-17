"""Class for Pixel Painter resource generator."""

from PIL import Image, ImageDraw, ImageFont
from math import ceil
from yattag import Doc
import string
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter

METHOD_VALUES = {
    "black-white": _("Black and White (2 possible binary values)"),
    "run-length-encoding": _("Black and White (2 possible binary values) in Run Length Encoding"),
    "greyscale": _("Greyscale (4 possible binary values)"),
    "colour": _("Colour (8 possible binary values)")
}

IMAGE_VALUES = {
    "star": _("Star - 1 page"),
    "teacup": _("Teacup - 1 page"),
    "cat": _("Cat - 1 page"),
    "fish": _("Fish - 6 pages"),
    "kauri-tree": _("Kauri tree - 6 pages"),
    "butterfly": _("Butterfly - 6 pages"),
    "hot-air-balloon": _("Hot air balloon - 8 pages"),
    "boat": _("Boat - 9 pages"),
    "parrots": _("Parrots - 32 pages"),
}


class PixelPainterResourceGenerator(BaseResourceGenerator):
    """Class for Pixel Painter resource generator."""

    methods = {
        "black-white": {
            "name": _("Black and White"),
            "labels": {
                255: "1",
                0: "0"
            }
        },
        "run-length-encoding": {
            "name": _("Run length encoding"),
            "labels": {
                255: "1",
                0: "0"
            }
        },
        "greyscale": {
            "name": _("Greyscale"),
            "labels": {
                255: "11",
                168: "10",
                84: "01",
                0: "00"
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
        "star": _("Star"),
        "teacup": _("Teacup"),
        "cat": _("Cat"),
        "boat": _("Boat"),
        "fish": _("Fish"),
        "hot-air-balloon": _("Hot air balloon"),
        "parrots": _("Parrots"),
        "kauri-tree": _("Kauri tree"),
        "butterfly": _("Butterfly"),
    }

    STATIC_PATH = "static/img/resources/pixel-painter/{image}/{filename}"
    FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
    FONT = ImageFont.truetype(FONT_PATH, 80)
    FONT_SMALL = ImageFont.truetype(FONT_PATH, 50)
    TEXT_COLOUR = "#888"
    COLUMNS_PER_PAGE = 15
    ROWS_PER_PAGE = 20
    BOX_SIZE = 200
    IMAGE_SIZE_X = BOX_SIZE * COLUMNS_PER_PAGE
    IMAGE_SIZE_Y = BOX_SIZE * ROWS_PER_PAGE
    LINE_COLOUR = "#666"
    LINE_WIDTH = 1

    @classmethod
    def get_additional_options(cls):
        """Additional options for PixelPainterResourceGenerator."""
        return {
            "method": EnumResourceParameter(
                name="method",
                description=_("Colouring type"),
                values=METHOD_VALUES,
                default="black-white"
            ),
            "image": EnumResourceParameter(
                name="image",
                description=_("Image"),
                values=IMAGE_VALUES,
                default="fish"
            ),
        }

    def data(self):
        """Create data for a copy of the Pixel Painter resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        method = self.options["method"].value
        image_name = self.options["image"].value
        image = self.base_image
        (image_width, image_height) = image.size

        pages = []
        if method == "run-length-encoding":
            pages_encoding = dict()

        number_column_pages = ceil(image_width / self.COLUMNS_PER_PAGE)
        number_row_pages = ceil(image_height / self.ROWS_PER_PAGE)
        page_grid_coords = self.create_page_grid_coords(number_column_pages, number_row_pages, image_name)

        grid_page = self.grid_reference_page(page_grid_coords, self.image_strings[image_name])
        pages.append({"type": "html", "data": grid_page})

        # For each page row
        for number_row_page in range(0, number_row_pages):
            page_start_row = (number_row_page) * self.ROWS_PER_PAGE
            # For each page column
            for number_column_page in range(0, number_column_pages):
                page_start_column = (number_column_page) * self.COLUMNS_PER_PAGE
                # Create page
                page = Image.new("RGB", (self.IMAGE_SIZE_X, self.IMAGE_SIZE_Y), "#fff")
                draw = ImageDraw.Draw(page)
                page_columns = min(self.COLUMNS_PER_PAGE, image_width - page_start_column)
                page_rows = min(self.ROWS_PER_PAGE, image_height - page_start_row)
                page_reference = page_grid_coords[number_row_page][number_column_page]
                self.draw_grid(draw, page_columns, page_rows, self.BOX_SIZE, self.LINE_COLOUR, self.LINE_WIDTH)

                if method == "run-length-encoding":
                    page_encoding = self.get_run_length_encoding(
                        image,
                        page_start_column,
                        page_columns,
                        page_start_row,
                        page_rows,
                        image_name,
                        method
                    )
                    pages_encoding[page_reference] = page_encoding
                else:
                    self.add_pixel_labels(
                        image,
                        draw,
                        page_start_column,
                        page_columns,
                        page_start_row,
                        page_rows,
                        image_name,
                        method
                    )

                self.add_page_reference(
                    image,
                    draw,
                    page_start_column,
                    page_columns,
                    page_start_row,
                    page_rows,
                    page_reference
                )

                pages.append({"type": "image", "data": page})

        if method in ["greyscale", "colour"]:
            legend_html = self.create_pixel_legend(self.methods[method]["labels"].items())
            legend_html = "<div style='display:inline;page-break-inside:avoid;'>{}</div>".format(legend_html)
            legend_html *= number_row_pages * number_column_pages
            pages.append({"type": "html", "data": legend_html})
        elif method == "run-length-encoding":
            encoding_html = self.create_run_length_encoding_html(page_grid_coords, pages_encoding)
            pages.insert(1, {"type": "html", "data": encoding_html})
        return pages

    def add_pixel_labels(self, image, draw, page_start_column, page_columns,
                         page_start_row, page_rows, image_name, method):
        """Draw pixel labels onto grid.

        Args:
            image (Image): Image to get pixel from.
            draw (ImageDraw): The draw object to add the text onto.
            page_start_column (int): Number of column on image this page starts from.
            page_columns (int): Number of column on this page.
            page_start_row (int): Number of row on image this page starts from.
            page_rows (int): Number of row on this page.
            image_name (str): Name of the image.
            method (str): Type of image used.
        """
        for row in range(0, page_rows):
            for column in range(0, page_columns):
                text = self.get_pixel_label(
                    image,
                    (page_start_column + column, page_start_row + row),
                    image_name,
                    method
                )

                # Draw text
                left, top, right, bottom = draw.textbbox((0, 0), text, font=self.FONT)
                text_width, text_height = right - left, bottom - top
                text_coord_x = (column * self.BOX_SIZE) + (self.BOX_SIZE / 2) - (text_width / 2)
                text_coord_y = (row * self.BOX_SIZE) + (self.BOX_SIZE / 2) - (text_height / 2)
                draw.text(
                    (text_coord_x, text_coord_y),
                    text,
                    font=self.FONT,
                    fill=self.TEXT_COLOUR
                )

    def get_run_length_encoding(self, image, page_start_column, page_columns,
                                page_start_row, page_rows, image_name, method):
        """Return run length encoding values for page.

        Args:
            image (Image): Image to get pixel from.
            page_start_column (int): Number of column on image this page starts from.
            page_columns (int): Number of column on this page.
            page_start_row (int): Number of row on image this page starts from.
            page_rows (int): Number of row on this page.
            image_name (str): Name of the image.
            method (str): Type of image used.
        """
        page_encoding = []
        for row in range(0, page_rows):
            row_encoding = []
            encoding_colour = "1"
            encoding_count = 0

            for column in range(0, page_columns):
                text = self.get_pixel_label(
                    image,
                    (page_start_column + column, page_start_row + row),
                    image_name,
                    method
                )
                if text != encoding_colour:
                    row_encoding.append(encoding_count)
                    if encoding_colour == "0":
                        encoding_colour = "1"
                    else:
                        encoding_colour = "0"
                    encoding_count = 0
                encoding_count += 1
                if page_columns - 1 == column:
                    row_encoding.append(encoding_count)
            page_encoding.append(row_encoding)
        return page_encoding

    def add_page_reference(self, image, draw, page_start_column, page_columns,
                           page_start_row, page_rows, page_reference):
        """Draw page reference onto first pixel that is not black.

        Args:
            image (Image): Image to get pixel from.
            draw (ImageDraw): The draw object to add the text onto.
            page_start_column (int): Number of column on image this page starts from.
            page_columns (int): Number of column on this page.
            page_start_row (int): Number of row on image this page starts from.
            page_rows (int): Number of row on this page.
            page_reference (str): Label of page reference.
        """
        page_reference_added = False
        row = 0
        while not page_reference_added and row < page_rows:
            column = 0
            while not page_reference_added and row < page_columns:
                pixel_value = image.getpixel((page_start_column + column, page_start_row + row))
                if isinstance(pixel_value, tuple):
                    is_black = pixel_value == (0, 0, 0)
                else:
                    is_black = pixel_value == 0
                if not is_black:
                    draw.text(
                        ((column * self.BOX_SIZE) + self.LINE_WIDTH * 4, (row * self.BOX_SIZE) + -4),
                        page_reference,
                        font=self.FONT_SMALL,
                        fill="#000"
                    )
                    page_reference_added = True
                column += 1
            row += 1

    @classmethod
    def get_pixel_label(cls, image, coords, image_name, method):
        """Return label of specific pixel on given image.

        Args:
            image (Image): Image to get pixel from.
            coords (tuple): A tuple of x and y coordinate numbers of the pixel.
            image_name (str): Name of the image.
            method (str): Type of image used.

        Returns:
            String of pixel label.
        """
        pixel_value = image.getpixel(coords)
        try:
            text = cls.methods[method]["labels"][pixel_value]
        except KeyError:
            message = "Image: {}\n".format(image_name)
            message += "Method: {}\n".format(method)
            message += "Contains invalid pixel value: {}".format(pixel_value)
            raise ValueError(message)
        return text

    def draw_grid(self, draw, page_columns, page_rows, square_size, line_colour, line_width):
        """Draw grid onto image.

        Args:
            draw (ImageDraw): The image to draw on.
            page_columns (int): Number of columns on page.
            page_rows (int): Number of rows on page.
            square_size (int): Pixel size of grid squares on page.
            line_colour (str): Hex code of grid line colour.
            line_width (int): Pixel width of grid lines.
        """
        grid_width = page_columns * square_size
        grid_height = page_rows * square_size

        for x_coord in range(0, page_columns * square_size, square_size):
            draw.line(
                [(x_coord, 0), (x_coord, grid_height)],
                fill=line_colour,
                width=line_width
            )
        draw.line(
            [(page_columns * square_size - 1, 0), (page_columns * square_size - 1, grid_height)],
            fill=line_colour,
            width=line_width
        )

        for y_coord in range(0, grid_height, square_size):
            draw.line(
                [(0, y_coord), (grid_width, y_coord)],
                fill=line_colour,
                width=line_width
            )
        draw.line(
            [(0, grid_height - 1), (grid_width, grid_height - 1)],
            fill=line_colour,
            width=line_width
        )

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
        image_number = self.options["image"].index(image)
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
        method = self.options["method"].value
        doc, tag, text, line = Doc().ttl()
        line("style", "#grid-table td {border:1px solid black;padding:1rem 0.5rem;}")
        with tag("h1"):
            text(_("Pixel Painter"))
        with tag("p"):
            text(_("This page should be kept secret from students."))
        with tag("h2"):
            text(_("Page grid reference for {} image").format(image_name))
        with tag("p"):
            text(_(
                "Once pixels on each page are filled in correctly, "
                "cut each grid out and arrange in the following layout "
                "(page names are in the top right corner)."
            ))
        with tag("div", style="padding-bottom:1cm;"):
            with tag("table", id="grid-table", style="padding-bottom:1cm;"):
                with tag("tbody"):
                    for row_num in range(0, len(page_grid_coords)):
                        with tag("tr"):
                            for column_num in range(0, len(page_grid_coords[row_num])):
                                line("td", page_grid_coords[row_num][column_num])

        if method in ["greyscale", "colour"]:
            with tag("p"):
                if method == "greyscale":
                    text(_("The pixel values are using 2 bit colour values."))
                if method == "colour":
                    text(_("The pixel values are using 5 bit RGB colour values (2 red, 2 green, 1 blue)."))
                text(" ")
                text(_("Extra pixel legends are at the end of this document for students."))
        html = doc.getvalue()
        html += self.create_pixel_legend(self.methods[method]["labels"].items())
        return html

    def create_pixel_legend(self, items):
        """Create pixel legend HTML.

        Args:
            items (dict): Items in the legend to display.

        Returns:
            HTML string for pixel legend.
        """
        doc, tag, text, line = Doc().ttl()
        line("style", "#pixel-legend td {border:1px solid black;padding:0.5rem 0.5rem;white-space:nowrap;}")
        with tag("table", id="pixel-legend", style="display:inline;"):
            with tag("tbody"):
                with tag("tr"):
                    line("td", _("Pixel legend"), colspan="2", style="font-weight:bold;text-align:center;")
                for (values, label) in items:
                    with tag("tr"):
                        if isinstance(values, tuple):
                            line("td", " ", style="background-color:rgb{};width:3em;".format(values))
                        else:
                            line("td", " ", style="background-color:rgb({0},{0},{0});width:3em;".format(values))
                        line("td", label)
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
        with tag("h1"):
            text(_("Run Length Encodings"))
        for index, row_of_page_references in enumerate(page_grid_coords):
            for page_reference in row_of_page_references:
                with tag("div", klass="page-break"):
                    with tag("h2"):
                        text(_("Encoding for page {}").format(page_reference))
                    page_encoding = pages_encoding[page_reference]
                    with tag("ul", klass="list-unstyled"):
                        for line_values in page_encoding:
                            line("li", ", ".join(str(number) for number in line_values))
        return doc.getvalue()

    def get_image_filename(self, image_name, method):
        """Return filename for requested image.

        Args:
            image_name (str): Name of the image.
            method (str): Type of image used.

        Returns:
            Image filename (str).
        """
        if method == "run-length-encoding":
            image_filename = "{}-black-white.png".format(image_name)
        else:
            image_filename = "{}-{}.png".format(image_name, method)
        return image_filename

    @property
    def base_image(self):
        """Get Image object of resource.

        Returns:
            Image object of image.
        """
        method = self.options["method"].value
        image_name = self.options["image"].value
        image_filename = self.get_image_filename(image_name, method)
        return Image.open(self.STATIC_PATH.format(image=image_name, filename=image_filename))

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        text = "{} - {} - {}".format(
            self.image_strings[self.options["image"].value],
            self.methods[self.options["method"].value]["name"],
            super().subtitle
        )
        return text

    def save_thumbnail(self, resource_name, path):
        """Return custom thumbnails for resource request.

        Args:
            resource_name: Name of the resource (str).
            path: The path to write the thumbnail to (str).

        The images are not resized as the images used are small already.
        """
        image = self.base_image
        (width, height) = image.size
        minimum_pixel_width = 400
        ratio = ceil(minimum_pixel_width / width)
        enlarged_size = (width * ratio, height * ratio)
        enlarged_image = image.resize(enlarged_size, resample=Image.NEAREST)
        enlarged_image.save(path)
