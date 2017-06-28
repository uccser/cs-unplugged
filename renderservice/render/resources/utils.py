"""Common utility functions for resources."""


def bool_to_yes_no(boolean):
    """Convert value to yes or no.

    Args:
        boolean: Value to check.

    Returns:
        "yes" if boolean is True, "no" if False.

    Raises:
        ValueError if value isn't "yes" or "no".
    """
    if type(value) is bool and value:
        return "yes"
    elif type(value) is bool:
        return "no"
    raise ValueError("Expected True or False.")

def bool_to_yes_no_or_pass_thru(value):
    """Convert value if boolean to yes or no.

    Args:
        value: Value to check.

    Returns:
        "yes" if boolean is True, "no" if False,
        otherwise the value is returned.

    Raises:
        ValueError if value isn't "yes" or "no".
    """
    try:
        return bool_to_yes_no(value)
    except ValueError:
        return value
