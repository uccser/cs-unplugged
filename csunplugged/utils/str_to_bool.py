"""Convert string to boolean value."""


def str_to_bool(value, error_on_invalid=False):
    """Convert string to boolean value.

    Args:
        value: String to convert to boolean.
        error_on_invalid: Boolean to state if an exception should be raised
            if the value isn't valid.

    Returns:
        True if value is "yes" or "True",
        False if "no" or "False".

    Raises:
        ValueError if value isn't as expected, when error_on_invalid is True.
    """
    if value in ["yes", "True"]:
        return True
    elif value in ["no", "False"]:
        return False
    elif error_on_invalid:
        raise ValueError("Expected 'yes', 'True', 'no', or 'False'. Received: {}.".format(value))
    else:
        return value
