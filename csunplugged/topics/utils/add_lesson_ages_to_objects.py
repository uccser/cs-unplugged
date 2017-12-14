"""Add lesson min and max ages to given list of objects."""

from topics.models import AgeGroup


def add_lesson_ages_to_objects(objects):
    """Add lesson min and max ages to given list of objects.

    Args:
        objects: List of objects of lessons.

    Returns:
        Modified list of objects.
    """
    age_groups = AgeGroup.objects.distinct()
    for item in objects:
        item_age_groups = list(age_groups.filter(lessons__id__in=item.lessons.all()))
        item.min_age = item_age_groups[0].ages.lower
        item.max_age = item_age_groups[-1].ages.upper
    return objects
