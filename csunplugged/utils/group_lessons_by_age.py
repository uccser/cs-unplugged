"""Return ordered groups of lessons."""

from collections import OrderedDict
from topics.models import (
    AgeRange,
    LessonNumber,
)


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
    for age_range in AgeRange.objects.distinct():
        ages = (age_range.ages.lower, age_range.ages.upper)
        for lesson in age_range.lessons.filter(id__in=lessons).order_by("lessonnumber"):
            lesson.number = LessonNumber.objects.get(lesson=lesson, age_range=age_range).number
            if ages in grouped_lessons.keys():
                grouped_lessons[ages].append(lesson)
            else:
                grouped_lessons[ages] = [lesson]
    return grouped_lessons
