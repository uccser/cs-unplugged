"""Module for importing a resource view module."""

import importlib


def get_resource_generator(generator_module, requested_options=None):
    """Return view module for resource.

    Args:
        generator_module: Name of resource generator (str).
        requested_options: QueryDict of requested_options (QueryDict).

    Returns:
        Instance of resource generator for given resource.
    """
    generator_class_name = generator_module
    module_path = "resources.views.{}".format(generator_class_name)
    module = importlib.import_module(module_path)
    generator_class = getattr(module, generator_class_name)
    generator = generator_class(requested_options)
    return generator
