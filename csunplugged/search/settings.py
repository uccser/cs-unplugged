"""Settings for the search application."""

from topics.models import (
    Topic,
    Lesson,
    ProgrammingChallenge,
    CurriculumIntegration,
    LessonNumber,
    CurriculumArea,
)
from classic.models import ClassicPage
from resources.models import Resource
from general.models import GeneralPage
from at_home.models import Activity
from search.utils import (
    get_search_model_types,
    get_model_filter_options,
)

SEARCH_PAGINATION = 25
SEARCH_RESULT_TEMPLATE_DIRECTORY = 'search/result/'


def lesson_render_function(lesson):
    """Provide additional context for rendering lesson results.

    Args:
        lesson (Lesson): Instance of search result.

    Returns:
        Dictionary of additional items to add to the render context.
    """
    lesson_ages = []
    lesson_numbers = LessonNumber.objects.filter(lesson=lesson).select_related('age_group')
    for lesson_number in lesson_numbers:
        lesson_ages.append(
            {
                "lower": lesson_number.age_group.ages.lower,
                "upper": lesson_number.age_group.ages.upper,
                "number": lesson_number.number,
            }
        )
    curriculum_areas = CurriculumArea.objects.filter(
        learning_outcomes__in=lesson.learning_outcomes.all()
    ).select_related('parent').distinct()

    additional_context = {
        'lesson_ages': lesson_ages,
        'curriculum_areas': curriculum_areas,
    }
    return additional_context


# List of dicts of class, boost value, required prefetches.
SEARCH_CLASSES_AND_BOOSTS = [
    {
        'class': Topic,
        'boost': 2,
        'curriculum_area_filtered': False,
        'select_related': [],
        'prefetch_related': [],
    },
    {
        'class': Lesson,
        'boost': 1.2,
        'curriculum_area_filtered': True,
        'select_related': ['topic'],
        'prefetch_related': ['learning_outcomes'],
        'render_function': lesson_render_function,
    },
    {
        'class': Resource,
        'boost': 1,
        'curriculum_area_filtered': False,
        'select_related': [],
        'prefetch_related': [],
    },
    {
        'class': GeneralPage,
        'boost': 0.9,
        'curriculum_area_filtered': False,
        'select_related': [],
        'prefetch_related': [],
    },
    {
        'class': Activity,
        'boost': 0.8,
        'curriculum_area_filtered': False,
        'select_related': [],
        'prefetch_related': [],
    },
    {
        'class': CurriculumIntegration,
        'boost': 0.7,
        'curriculum_area_filtered': True,
        'select_related': ['topic'],
        'prefetch_related': ['curriculum_areas', 'curriculum_areas__parent'],
    },
    {
        'class': ClassicPage,
        'boost': 0.6,
        'curriculum_area_filtered': False,
        'select_related': [],
        'prefetch_related': [],
    },
    {
        'class': ProgrammingChallenge,
        'boost': 0.4,
        'curriculum_area_filtered': False,
        'select_related': ['topic'],
        'prefetch_related': ['difficulty'],
    },
]


# Settings calculated from SEARCH_MODEL_TYPES
SEARCH_MODEL_TYPES = get_search_model_types(SEARCH_CLASSES_AND_BOOSTS)
SEARCH_MODEL_FILTER_VALUES = get_model_filter_options(SEARCH_MODEL_TYPES)
