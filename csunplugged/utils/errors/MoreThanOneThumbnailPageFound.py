"""Exception for more than one thumbnail page in resource."""


class MoreThanOneThumbnailPageFound(Exception):
    """Exception for more than one thumbnail page in resource."""

    def __init__(self, generator):
        """Initialise exception.

        Args:
            generator: Resource generator (Child of BaseResourceGenerator).
        """
        super().__init__()
        self.generator_name = generator.__class__.__name__

    def __str__(self):
        """Override default error string.

        Returns:
            Error message for style error.
        """
        message = "{} returned more than one page as the designated thumbnail."
        return message.format(self.generator_name)
