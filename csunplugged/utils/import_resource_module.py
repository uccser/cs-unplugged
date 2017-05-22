"""Module for importing a resource view module."""

import importlib


def import_resource_module(resource):
    """Return view module for resource.

    Args:
        resource: Resource model object.

    Returns:
        Python module for resource.
    """
    resource_view = resource.generation_view
    if resource_view.endswith(".py"):
        resource_view = resource_view[:-3]
    module_path = "resources.views.{}".format(resource_view)
    return importlib.import_module(module_path)
