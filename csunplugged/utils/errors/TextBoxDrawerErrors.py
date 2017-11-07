"""Exceptions relating to the TextBoxDrawer utility class."""


class TextBoxDrawerError(Exception):
    """Base exception for TextBoxDrawer errors."""

    pass


class MissingSVGFile(TextBoxDrawerError):
    """Raised when an SVG file could not be found."""

    pass


class TextBoxNotFoundInSVG(TextBoxDrawerError):
    """Raised when a given textbox id could not be found in the SVG file."""

    pass
