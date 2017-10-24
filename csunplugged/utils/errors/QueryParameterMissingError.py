"""Exception for missing query parameter."""

class QueryParameterMissingError(Exception):
    """Exception for missing parameter in a GET query."""

    def __init__(self, parameter):
        """Initialise exception.

        Args:
            parameter: The query parameter for the exception (str).
        """

        message = "Parameter '{}' not specified.".format(parameter)
        super().__init__(message)
