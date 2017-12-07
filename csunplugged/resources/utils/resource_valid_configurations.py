"""Create list of all possible valid resource combinations."""

import itertools
from copy import deepcopy


def resource_valid_configurations(valid_options):
    """Return list of all possible valid resource combinations.

    Args:
        valid_options: A dictionary containing all valid resource generation
                       options (dict).

    Returns:
        List of dictionaries of valid combinations (list).
    """
    valid_options = deepcopy(valid_options)
    valid_option_keys = sorted(valid_options)
    return [dict(zip(valid_option_keys, product)) for product in itertools.product(
        *(valid_options[valid_option_key] for valid_option_key in valid_option_keys)
    )]
