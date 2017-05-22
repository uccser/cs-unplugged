"""Module for creating GET query string from dictionary."""


def query_string(values):
    """Create a GET query to append to a URL from the given values.

    Args:
        values: A dictionary of keys/values of GET parameters.

    Returns:
        String of GET query.
    """
    string = "?"
    for index, (key, value) in enumerate(values.items()):
        string += "{key}={value}".format(key=key, value=value)
        if index < len(values):
            string += "&"
    return string
