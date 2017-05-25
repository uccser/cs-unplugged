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
        The value for a key is a sorted list of lessons.
        The dictionary is ordered by minimum age, then maximum age.
    """
    grouped_lessons = OrderedDict()
    lessons = lessons.order_by("min_age", "max_age", "number")
    for lesson in lessons:
        if (lesson.min_age, lesson.max_age) in grouped_lessons:
            grouped_lessons[(lesson.min_age, lesson.max_age)].append(lesson)
        else:
            grouped_lessons[(lesson.min_age, lesson.max_age)] = [lesson]
    return grouped_lessons
