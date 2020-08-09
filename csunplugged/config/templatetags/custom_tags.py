"""Module for the custom dictionary look up template tag."""

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    """Return the value in a dictionary given a key."""
    return dictionary.get(key)
