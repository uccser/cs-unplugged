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

    text = indexes.NgramField(document=True, use_template=True)

    def prepare(self, obj):
        data = super(TopicIndex, self).prepare(obj)
        data["_boost"] = 1.4
        return data

    def get_model(self):
        """Return the Topic model.

        Returns:
            Topic object.
        """
        return Topic


class UnitPlanIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for UnitPlan model."""

    text = indexes.NgramField(document=True, use_template=True)
    topic = indexes.CharField(model_attr="topic")

    def prepare(self, obj):
        data = super(UnitPlanIndex, self).prepare(obj)
        data["_boost"] = 1.2
        return data

    def get_model(self):
        """Return the UnitPlan model.

        Returns:
            UnitPlan object.
        """
        return UnitPlan


class LessonIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for Lesson model."""

    text = indexes.NgramField(document=True, use_template=True)
    topic = indexes.CharField(model_attr="topic")
    unit_plan = indexes.CharField(model_attr="unit_plan")

    def prepare(self, obj):
        data = super(LessonIndex, self).prepare(obj)
        data["_boost"] = 1
        return data

    def get_model(self):
        """Return the Lesson model.

        Returns:
            Lesson object.
        """
        return Lesson


class CurriculumIntegrationIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for CurriculumIntegration model."""

    text = indexes.NgramField(document=True, use_template=True, boost=1.2)
    topic = indexes.CharField(model_attr="topic")
    curriculum_areas = indexes.MultiValueField()

    def prepare(self, obj):
        data = super(CurriculumIntegrationIndex, self).prepare(obj)
        data["_boost"] = 0.8
        return data

    def prepare_curriculum_areas(self, obj):
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

    text = indexes.NgramField(document=True, use_template=True)
    topic = indexes.CharField(model_attr="topic")

    def prepare(self, obj):
        data = super(ProgrammingChallengeIndex, self).prepare(obj)
        data["_boost"] = 0.4
        return data

    def get_model(self):
        """Return the ProgrammingChallenge model.

        Returns:
            ProgrammingChallenge object.
        """
        return ProgrammingChallenge
