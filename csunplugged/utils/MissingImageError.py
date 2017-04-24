"""Exception raised when an image cannot be found in static folder."""


class MissingImageError(Exception):
    """Exception raised when an image cannot be found in static folder."""

    def __init__(self, image, message):
        """Create MissingImageError object.

        Args:
            image: file path given in markdown text for missing image.
            message: explanation of why error was thrown.
        """
        super().__init__(message)
        self.image = image
        self.message = message
