"""Sort QuerySet with translated items first, then untranslated items."""

from django.db.models.query import QuerySet


def translated_first(items):
    """Sort items with translated items first, then untranslated items.

    Args:
        items (QuerySet): Set of items to sort.

    Returns:
        List of sorted items.
    """
    if not isinstance(items, QuerySet):
        raise TypeError("Can only sort QuerySet")
    translated = []
    untranslated = []
    for item in items:
        if item.translation_available:
            translated.append(item)
        else:
            untranslated.append(item)
    return translated + untranslated
