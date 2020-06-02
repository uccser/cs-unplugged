"""Translation options for localised models.

Utilised by django-modeltranslation. See http://django-modeltranslation.readthedocs.io
"""

from modeltranslation.translator import translator, TranslationOptions
from at_home.models import (
    Activity,
    Challenge,
)


class ActivityTranslationOptions(TranslationOptions):
    """Translation options for Activity model."""

    fields = (
        "name",
        "introduction",
        "inside_the_computer",
        "project",
        "more_information",
        "activity_steps",
        "activity_extra_information",
    )
    fallback_undefined = {
        "inside_the_computer": None,
        "project": None,
        "more_information": None,
        "activity_extra_information": None,
    }


class ChallengeTranslationOptions(TranslationOptions):
    """Translation options for Challenge model."""

    fields = (
        "question",
        "answer",
    )


translator.register(Activity, ActivityTranslationOptions)
translator.register(Challenge, ChallengeTranslationOptions)
