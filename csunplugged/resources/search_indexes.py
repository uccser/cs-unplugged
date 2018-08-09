"""Search index for resources model."""

from haystack import indexes
from resources.models import Resource


class ResourceIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for Resource model."""

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """Return the Resource model.

        Returns:
            Resource object.
        """
        return Resource
