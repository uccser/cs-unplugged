"""Search index for topics models."""

from haystack import indexes
from topics.models import CurriculumIntegration


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
