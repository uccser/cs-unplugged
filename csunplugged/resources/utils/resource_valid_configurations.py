"""Create list of all possible valid resource combinations."""

import itertools
from utils.bool_to_yes_no import bool_to_yes_no
from copy import deepcopy


def resource_valid_configurations(valid_options, header_text=True):
    """Return list of all possible valid resource combinations.

    Args:
        valid_options: A dictionary containing all valid resource generation
                       options (dict).
        header_text: If true, add in valid options for header text (bool).

    Returns:
        List of dictionaries of valid combinations (list).
    """
    valid_options = deepcopy(valid_options)
    if header_text:
        valid_options["header_text"] = ["", "Example header"]
    # Change all booleans to text to mimic forms
    for (key, values) in valid_options.items():
        for i in range(0, len(values)):
            if isinstance(values[i], bool):
                values[i] = bool_to_yes_no(values[i])
    valid_option_keys = sorted(valid_options)
    return [dict(zip(valid_option_keys, product)) for product in itertools.product(
        *(valid_options[valid_option_key] for valid_option_key in valid_option_keys)
    )]
