"""Return ordered groups of lessons."""

from collections import OrderedDict


def group_lessons_by_age(lessons):
    """Return ordered groups of lessons.

    Lessons are grouped by the lesson minimum age and maximum ages,
    and then order by number.

    Args:
        lessons: QuerySet of Lesson objects (QuerySet).

    Returns:
        A ordered dictionary of grouped lessons.
        The key is a tuple of the minimum age and maximum ages for
        the lessons.
        The value for a key is a sorted list of lessons (ordered by number).
    """
    grouped_lessons = OrderedDict()
    lessons = lessons.order_by("number")
    for lesson in lessons:
        for age_range in lesson.age_range.all():
            ages = (age_range.age_range.lower, age_range.age_range.upper)
            if ages in grouped_lessons.keys():
                grouped_lessons[ages].append(lesson)
            else:
                grouped_lessons[ages] = [lesson]
    return grouped_lessons
