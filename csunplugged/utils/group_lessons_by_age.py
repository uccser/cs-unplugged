"""Return ordered groups of lessons."""

from collections import OrderedDict


def group_lessons_by_age(age_ranges):
    """Return ordered groups of lessons.

    Lessons are grouped by the lesson minimum age and maximum ages,
    and then order by number.

    Args:
        lessons: QuerySet of AgeRange objects (QuerySet).

    Returns:
        A ordered dictionary of grouped lessons.
        The key is a tuple of the minimum age and maximum ages for
        the lessons.
        The value for a key is a sorted list of lessons (ordered by number).
    """
    grouped_lessons = OrderedDict()
    age_ranges = age_ranges.order_by("age_range")
    for age_range in age_ranges:
        bounds = (age_range.age_range.lower, age_range.age_range.upper)
        grouped_lessons[bounds] = [lesson for lesson in age_range.lessons.order_by("number").all()]
    return grouped_lessons
