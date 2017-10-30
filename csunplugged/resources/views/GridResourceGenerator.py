"""Class for Grid resource generator."""

from PIL import Image, ImageDraw
from utils.BaseResourceGenerator import BaseResourceGenerator

GRID_COLUMNS = 8
GRID_ROWS = 8
BOX_SIZE = 500
IMAGE_SIZE_X = BOX_SIZE * GRID_COLUMNS
IMAGE_SIZE_Y = BOX_SIZE * GRID_ROWS
LINE_COLOUR = "#000000"
LINE_WIDTH = 3


class GridResourceGenerator(BaseResourceGenerator):
    """Class for Grid resource generator."""

    def data(self):
        """Create data for a copy of the Grid resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        page = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#fff")
        draw = ImageDraw.Draw(page)
        for x_coord in range(0, IMAGE_SIZE_X, BOX_SIZE):
            draw.line(
                [(x_coord, 0), (x_coord, IMAGE_SIZE_Y)],
                fill=LINE_COLOUR,
                width=LINE_WIDTH
            )
        draw.line(
            [(IMAGE_SIZE_X - 1, 0), (IMAGE_SIZE_X - 1, IMAGE_SIZE_Y)],
            fill=LINE_COLOUR,
            width=LINE_WIDTH
        )
        for y_coord in range(0, IMAGE_SIZE_Y, BOX_SIZE):
            draw.line(
                [(0, y_coord), (IMAGE_SIZE_X, y_coord)],
                fill=LINE_COLOUR,
                width=LINE_WIDTH
            )
        draw.line(
            [(0, IMAGE_SIZE_Y - 1), (IMAGE_SIZE_X, IMAGE_SIZE_Y - 1)],
            fill=LINE_COLOUR,
            width=LINE_WIDTH
        )

        return {"type": "image", "data": page}
