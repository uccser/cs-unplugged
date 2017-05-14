"""Search index for topics models."""

from haystack import indexes
from topics.models import (
    Topic,
    UnitPlan,
    Lesson,
    ProgrammingExercise,
    CurriculumIntegration,
    CurriculumArea,
)


class TopicIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for Topic model."""

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """Return the Topic model.

        Returns:
            Topic object.
        """
        return Topic


class UnitPlanIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for UnitPlan model."""

    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr='topic')

    def get_model(self):
        """Return the UnitPlan model.

        Returns:
            UnitPlan object.
        """
        return UnitPlan


class LessonIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for Lesson model."""

    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr='topic')
    unit_plan = indexes.CharField(model_attr='unit_plan')

    def get_model(self):
        """Return the Lesson model.

        Returns:
            Lesson object.
        """
        return Lesson


class ProgrammingExerciseIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for ProgrammingExercise model."""

    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr='topic')

    def get_model(self):
        """Return the ProgrammingExercise model.

        Returns:
            ProgrammingExercise object.
        """
        return ProgrammingExercise


class CurriculumIntegrationIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for CurriculumIntegration model."""

    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr='topic')

    def get_model(self):
        """Return the CurriculumIntegration model.

        Returns:
            CurriculumIntegration object.
        """
        return CurriculumIntegration


class CurriculumAreaIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for CurriculumArea model."""

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """Return the CurriculumArea model.

        Returns:
            CurriculumArea object.
        """
        return CurriculumArea
