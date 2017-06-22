"""Convert boolean value to yes or no."""


def bool_to_yes_no(value):
    """Convert value if boolean to yes or no.

    Args:
        boolean: Value to check.

    Returns:
        "yes" if boolean is True, "no" if False,
        or changed otherwise.
    """
    if type(value) == bool and value:
        return "yes"
    elif type(value) == bool:
        return "no"
    else:
        return value
