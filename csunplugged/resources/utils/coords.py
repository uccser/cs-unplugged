"""Helper functions for dealing with coordinates."""


def calculate_box_vertices(top_left, width, height):
    """Calculate vertices of box.

    Args:
        top_left (tuple of two ints): An x and y of top left corner of box.
        width (int): Width of box.
        height (int): Height of box.

    Returns:
        List of four (x, y) tuples of the four corners of the box.
        In order: top left, top right, bottom right, bottom left.
    """
    x, y = top_left
    top_right = (x + width, y)
    bottom_left = (x, y + height)
    bottom_right = (x + width, y + height)
    return [top_left, top_right, bottom_right, bottom_left]
