"""Translation options for localised models.

Utilised by django-modeltranslation. See http://django-modeltranslation.readthedocs.io
"""

from modeltranslation.translator import translator, TranslationOptions
from topics.models import (
    Topic,
    UnitPlan,
    ProgrammingChallenge,
    ProgrammingChallengeImplementation,
    Lesson,
    CurriculumIntegration,
    GlossaryTerm
)


class TopicTranslationOptions(TranslationOptions):
    """Translation options for Topic model."""

    fields = ('name', 'content', 'other_resources')


class UnitPlanTranslationOptions(TranslationOptions):
    """Translation options for UnitPlan model."""

    fields = ('name', 'content', 'computational_thinking_links', 'heading_tree')


class ProgrammingChallengeTranslationOptions(TranslationOptions):
    """Translation options for ProgrammingChallenge model."""

    fields = ('name', 'content', 'extra_challenge')


class ProgrammingChallengeImplementationTranslationOptions(TranslationOptions):
    """Translation options for ProgrammingChallengeImplementation model."""

    fields = ('expected_result', 'hints', 'solution')


class LessonTranslationOptions(TranslationOptions):
    """Translation options for Lesson model."""
    fields = ('name', 'content', 'computational_thinking_links', 'programming_challenges_description', 'heading_tree')


class CurriculumIntegrationTranslationOptions(TranslationOptions):
    """Translation options for CurriculumIntegration model."""

    fields = ('name', 'content')


class GlossaryTermTranslationOptions(TranslationOptions):
    """Translation options for GlossaryTerm model."""

    fields = ('term', 'definition')


translator.register(Topic, TopicTranslationOptions)
translator.register(UnitPlan, UnitPlanTranslationOptions)
translator.register(ProgrammingChallenge, ProgrammingChallengeTranslationOptions)
translator.register(ProgrammingChallengeImplementation, ProgrammingChallengeImplementationTranslationOptions)
translator.register(Lesson, LessonTranslationOptions)
translator.register(CurriculumIntegration, CurriculumIntegrationTranslationOptions)
translator.register(GlossaryTerm, GlossaryTermTranslationOptions)
