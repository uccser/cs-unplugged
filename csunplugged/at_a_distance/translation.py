"""Translation options for localised models.

Utilised by django-modeltranslation. See http://django-modeltranslation.readthedocs.io
"""

from modeltranslation.translator import translator, TranslationOptions
from at_a_distance.models import Lesson


class LessonTranslationOptions(TranslationOptions):
    """Translation options for Activity model."""

    fields = (
        "name",
        "introduction",
    )
    fallback_undefined = {
        "name": None,
        "introduction": None,
    }


translator.register(Lesson, LessonTranslationOptions)
