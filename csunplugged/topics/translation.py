"""Translation options for localised models.

Utilised by django-modeltranslation. See http://django-modeltranslation.readthedocs.io
"""

from modeltranslation.translator import translator, TranslationOptions
from topics.models import (
    Topic,
    ProgrammingChallenge,
    ProgrammingChallengeImplementation,
    Lesson,
    CurriculumIntegration,
    GlossaryTerm,
    CurriculumArea,
    LearningOutcome,
    AgeGroup,
    ClassroomResource,
    ResourceDescription,
    ProgrammingChallengeDifficulty,
    ProgrammingChallengeLanguage,
)


class TopicTranslationOptions(TranslationOptions):
    """Translation options for Topic model."""

    fields = ("name", "content", "other_resources")
    fallback_undefined = {
        "content": None,
        "other_resources": None
    }


class ProgrammingChallengeTranslationOptions(TranslationOptions):
    """Translation options for ProgrammingChallenge model."""

    fields = ("name", "content", "extra_challenge")
    fallback_undefined = {
        "content": None,
        "extra_challenge": None,
    }


class ProgrammingChallengeImplementationTranslationOptions(TranslationOptions):
    """Translation options for ProgrammingChallengeImplementation model."""

    fields = ("expected_result", "hints", "solution")
    fallback_undefined = {
        "expected_result": None,
        "hints": None,
        "solution": None
    }


class LessonTranslationOptions(TranslationOptions):
    """Translation options for Lesson model."""

    fields = ("name", "content", "computational_thinking_links", "programming_challenges_description", "heading_tree")
    fallback_undefined = {
        "content": None,
        "computational_thinking_links": None,
        "programming_challenges_description": None,
        "heading_tree": None
    }


class CurriculumIntegrationTranslationOptions(TranslationOptions):
    """Translation options for CurriculumIntegration model."""

    fields = ("name", "content")
    fallback_undefined = {
        "content": None,
    }


class GlossaryTermTranslationOptions(TranslationOptions):
    """Translation options for GlossaryTerm model."""

    fields = ("term", "definition")
    fallback_undefined = {
        "term": None,
        "definition": None
    }


class CurriculumAreaTranslationOptions(TranslationOptions):
    """Translation options for CurriculumArea model."""

    fields = ("name",)
    fallback_undefined = {
        "name": None,
    }


class LearningOutcomeTranslationOptions(TranslationOptions):
    """Translation options for LearningOutcome model."""

    fields = ("text",)
    fallback_undefined = {
        "text": None,
    }


class AgeGroupTranslationOptions(TranslationOptions):
    """Translation options for AgeGroup model."""

    fields = ("description",)
    fallback_undefined = {
        "description": None,
    }


class ClassroomResourceTranslationOptions(TranslationOptions):
    """Translation options for ClassroomResource model."""

    fields = ("description",)
    fallback_undefined = {
        "description": None,
    }


class ResourceDescriptionTranslationOptions(TranslationOptions):
    """Translation options for ResourceDescription model."""

    fields = ("description",)
    fallback_undefined = {
        "description": None,
    }


class ProgrammingChallengeDifficultyTranslationOptions(TranslationOptions):
    """Translation options for ProgrammingChallengeDifficulty model."""

    fields = ("name",)
    fallback_undefined = {
        "name": None,
    }


class ProgrammingChallengeLanguageTranslationOptions(TranslationOptions):
    """Translation options for ProgrammingChallengeLanguage model."""

    fields = ("name", "programming_reminders")
    fallback_undefined = {
        "name": None,
    }


translator.register(Topic, TopicTranslationOptions)
translator.register(ProgrammingChallenge, ProgrammingChallengeTranslationOptions)
translator.register(ProgrammingChallengeImplementation, ProgrammingChallengeImplementationTranslationOptions)
translator.register(Lesson, LessonTranslationOptions)
translator.register(CurriculumIntegration, CurriculumIntegrationTranslationOptions)
translator.register(GlossaryTerm, GlossaryTermTranslationOptions)
translator.register(CurriculumArea, CurriculumAreaTranslationOptions)
translator.register(LearningOutcome, LearningOutcomeTranslationOptions)
translator.register(AgeGroup, AgeGroupTranslationOptions)
translator.register(ClassroomResource, ClassroomResourceTranslationOptions)
translator.register(ResourceDescription, ResourceDescriptionTranslationOptions)
translator.register(ProgrammingChallengeDifficulty, ProgrammingChallengeDifficultyTranslationOptions)
translator.register(ProgrammingChallengeLanguage, ProgrammingChallengeLanguageTranslationOptions)
