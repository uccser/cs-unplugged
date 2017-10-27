"""Exception for missing thumbnail page in resource."""


class ThumbnailPageNotFound(Exception):
    """Exception for missing thumbnail page in resource."""

    def __init__(self, generator):
        """Initialise exception.

        Args:
            generator: Resource generator (Child of BaseResourceGenerator).
        """
        message = "{} did not return a page with a designated thumbnail.".format(generator.__class__.__name__)
        super().__init__(message)
