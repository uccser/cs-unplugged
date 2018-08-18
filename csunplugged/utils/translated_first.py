"""Sort MultilingualQuerySet with translated items first, then untranslated items."""

from modeltranslation.manager import MultilingualQuerySet


def translated_first(items):
    """Sort items with translated items first, then untranslated items.

    Args:
        items (MultilingualQuerySet): Set of items to sort.

    Returns:
        List of sorted items.
    """
    if not isinstance(items, MultilingualQuerySet):
        raise TypeError("Can only sort MultilingualQuerySets")
    translated = []
    untranslated = []
    for item in items:
        if item.translation_available:
            translated.append(item)
        else:
            untranslated.append(item)
    return translated + untranslated
