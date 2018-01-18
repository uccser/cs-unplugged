"""Search index for topics models.

Note: Document boosting for Whoosh backend is with keyword '_boost' instead
      of 'boost'.
"""

from haystack import indexes
from topics.models import (
    Topic,
    UnitPlan,
    Lesson,
    ProgrammingChallenge,
    CurriculumIntegration,
    CurriculumArea,
)


class TopicIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for Topic model."""

    text = indexes.CharField(document=True, use_template=True)

    def prepare(self, obj):
        """Set boost of Topic model for index.

        Args:
            obj (Topic): Topic object.

        Returns:
            Dictionary of data.
        """
        data = super(TopicIndex, self).prepare(obj)
        data["_boost"] = 2
        return data

    def get_model(self):
        """Return the Topic model.

        Returns:
            Topic object.
        """
        return Topic


class UnitPlanIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for UnitPlan model."""

    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr="topic")

    def prepare(self, obj):
        """Set boost of UnitPlan model for index.

        Args:
            obj (UnitPlan): UnitPlan object.

        Returns:
            Dictionary of data.
        """
        data = super(UnitPlanIndex, self).prepare(obj)
        data["_boost"] = 1.5
        return data

    def get_model(self):
        """Return the UnitPlan model.

        Returns:
            UnitPlan object.
        """
        return UnitPlan


class LessonIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for Lesson model."""

    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr="topic")
    unit_plan = indexes.CharField(model_attr="unit_plan")
    curriculum_areas = indexes.MultiValueField()

    def prepare(self, obj):
        """Set boost of Lesson model for index.

        Args:
            obj (Lesson): Lesson object.

        Returns:
            Dictionary of data.
        """
        data = super(LessonIndex, self).prepare(obj)
        data["_boost"] = 1.2
        return data

    def prepare_curriculum_areas(self, obj):
        """Create data for curriculum_areas index value.

        Args:
            obj (Lesson): Lesson object.

        Returns:
            List of curriculum area primary keys as strings.
        """
        curriculum_areas = CurriculumArea.objects.filter(
            learning_outcomes__in=obj.learning_outcomes.all()
        ).distinct()
        areas = set()
        for curriculum_area in curriculum_areas:
            areas.add(str(curriculum_area.pk))
            if curriculum_area.parent:
                areas.add(str(curriculum_area.parent.pk))
        return list(areas)

    def get_model(self):
        """Return the Lesson model.

        Returns:
            Lesson object.
        """
        return Lesson


class CurriculumIntegrationIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for CurriculumIntegration model."""

    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr="topic")
    curriculum_areas = indexes.MultiValueField()

    def prepare(self, obj):
        """Set boost of CurriculumIntegration model for index.

        Args:
            obj (CurriculumIntegration): CurriculumIntegration object.

        Returns:
            Dictionary of data.
        """
        data = super(CurriculumIntegrationIndex, self).prepare(obj)
        data["_boost"] = 0.7
        return data

    def prepare_curriculum_areas(self, obj):
        """Create data for curriculum_areas index value.

        Args:
            obj (CurriculumIntegration): CurriculumIntegration object.

        Returns:
            List of curriculum area primary keys as strings.
        """
        areas = set()
        for curriculum_area in obj.curriculum_areas.all():
            areas.add(str(curriculum_area.pk))
            if curriculum_area.parent:
                areas.add(str(curriculum_area.parent.pk))
        return list(areas)

    def get_model(self):
        """Return the CurriculumIntegration model.

        Returns:
            CurriculumIntegration object.
        """
        return CurriculumIntegration


class ProgrammingChallengeIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for ProgrammingChallenge model."""

    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr="topic")

    def prepare(self, obj):
        """Set boost of ProgrammingChallenge model for index.

        Args:
            obj (ProgrammingChallenge): ProgrammingChallenge object.

        Returns:
            Dictionary of data.
        """
        data = super(ProgrammingChallengeIndex, self).prepare(obj)
        data["_boost"] = 0.4
        return data

    def get_model(self):
        """Return the ProgrammingChallenge model.

        Returns:
            ProgrammingChallenge object.
        """
        return ProgrammingChallenge
