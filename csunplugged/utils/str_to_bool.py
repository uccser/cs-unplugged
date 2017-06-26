"""Convert string to boolean value."""


def str_to_bool(value):
    """Convert string to boolean value.

    Args:
        value: String to convert to boolean.

    Returns:
        True if value is "yes" or "True",
        False if "no" or "False".

    Raises:
        ValueError if value isn't as expected.
    """
    if value in ["yes", "True"]:
        return True
    elif value in ["no", "False"]:
        return False
    else:
        raise ValueError("Expected 'yes', 'True', 'no', or 'False'.")
