"""Exception for invalid query parameter."""


class QueryParameterInvalidError(Exception):
    """Exception for invalid parameter in a GET query."""

    def __init__(self, parameter, value):
        """Initialise exception.

        Args:
            parameter: The query parameter for the exception (str).
            value: The value for the given parameter (str).
        """
        super().__init__()
        self.parameter = parameter
        self.value = value

    def __str__(self):
        """Override default error string.

        Returns:
            Error message for empty config file.
        """
        text = "Value '{}' for parameter '{}' is not valid."
        return text.format(self.value, self.parameter)
