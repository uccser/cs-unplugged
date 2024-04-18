"""Convert boolean value to yes or no."""


def bool_to_yes_no(value, error_on_invalid=False):
    """Convert value if boolean to yes or no.

    Args:
        boolean: Value to check.
        error_on_invalid: Boolean to state if an exception should be raised
            if the value isn't valid.

    Returns:
        "yes" if boolean is True, "no" if False,
        otherwise the value is returned.

    Raises:
        ValueError if value isn't "yes" or "no".
    """
    if type(value) is bool and value:
        return "yes"
    elif type(value) is bool:
        return "no"
    elif error_on_invalid:
        raise ValueError("Expected True or False.")
    else:
        return value
