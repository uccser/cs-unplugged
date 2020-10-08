"""Return ordered groups of lessons."""

from collections import OrderedDict
from topics.models import (
    AgeGroup,
    LessonNumber,
)


def group_lessons_by_age(lessons, only_programming_exercises=False):
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
    for age_group in AgeGroup.objects.distinct():
        for lesson in age_group.lessons.filter(id__in=lessons).order_by("lessonnumber"):
            if not only_programming_exercises or (only_programming_exercises and lesson.has_programming_challenges()):
                lesson.number = LessonNumber.objects.get(lesson=lesson, age_group=age_group).number
                if age_group in grouped_lessons.keys():
                    grouped_lessons[age_group].append(lesson)
                else:
                    grouped_lessons[age_group] = [lesson]
    return grouped_lessons
