"""Exception for invalid query parameter."""

class QueryParameterInvalidError(Exception):
    """Exception for invalid parameter in a GET query."""

    def __init__(self, parameter, value):
        """Initialise exception.

        Args:
            parameter: The query parameter for the exception (str).
            value: The value for the given parameter (str).
        """

        message = "Value '{}' for parameter '{}' is not valid.".format(value, parameter)
        super().__init__(message)
