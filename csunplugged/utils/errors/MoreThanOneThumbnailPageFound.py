"""Exception for more than one thumbnail page in resource."""


class MoreThanOneThumbnailPageFound(Exception):
    """Exception for more than one thumbnail page in resource."""

    def __init__(self, generator):
        """Initialise exception.

        Args:
            generator: Resource generator (Child of BaseResourceGenerator).
        """
        message = "{} returned more than one page as the designated thumbnail.".format(generator.__class__.__name__)
        super().__init__(message)
