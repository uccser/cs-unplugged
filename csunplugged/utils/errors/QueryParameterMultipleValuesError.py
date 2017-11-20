"""Exception for missing query parameter."""


class QueryParameterMultipleValuesError(Exception):
    """Exception for missing parameter in a GET query."""

    def __init__(self, parameter, values):
        """Initialise exception.

        Args:
            parameter: The query parameter for the exception (str).
        """
        super().__init__()
        self.parameter = parameter
        self.values = values

    def __str__(self):
        """Override default error string.

        Returns:
            Error message for empty config file.
        """
        text = "Parameter '{}' must only have one value, but multiple were given ({})."
        return text.format(self.parameter, self.value)
