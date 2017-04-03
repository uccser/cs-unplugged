class MissingImageError(Exception):
    """Exception raised when an expected image cannot be found
        in static/
        image: file path given in md text for missing image
        message: explanation of why error was thrown
    """

    def __init__(self, image, message):
        super().__init__(message)
        self.image = image
        self.message = message
