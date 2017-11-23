"""Exception for missing query parameter."""


class QueryParameterMissingError(Exception):
    """Exception for missing parameter in a GET query."""

    def __init__(self, parameter):
        """Initialise exception.

        Args:
            parameter: The query parameter for the exception (str).
        """
        super().__init__()
        self.parameter = parameter

    def __str__(self):
        """Override default error string.

        Returns:
            Error message for empty config file.
        """
        text = "Parameter '{}' not specified."
        return text.format(self.parameter)
