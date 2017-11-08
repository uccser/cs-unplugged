"""Create list of all possible valid resource combinations."""

import itertools
from utils.bool_to_yes_no import bool_to_yes_no


def resource_valid_configurations(valid_options, header_text=True):
    """Return list of all possible valid resource combinations.

    Args:
        valid_options: A dictionary containing all valid resource generation
                       options (dict).
        header_text: If true, add in valid options for header text (bool).

    Returns:
        List of dictionaries of valid combinations (list).
    """
    if header_text:
        valid_options["header_text"] = ["", "Example header"]
    # Change all booleans to text to mimic forms
    for (key, value) in valid_options.items():
        if isinstance(value, bool):
            valid_options[key] = bool_to_yes_no(value)
    valid_option_keys = sorted(valid_options)
    return [dict(zip(valid_option_keys, product)) for product in itertools.product(
        *(valid_options[valid_option_key] for valid_option_key in valid_option_keys)
    )]
