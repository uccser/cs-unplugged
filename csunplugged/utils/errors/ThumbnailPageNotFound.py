"""Exception for missing thumbnail page in resource."""


class ThumbnailPageNotFound(Exception):
    """Exception for missing thumbnail page in resource."""

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
        message = "{} did not return a page with a designated thumbnail."
        return message.format(self.generator_name)
