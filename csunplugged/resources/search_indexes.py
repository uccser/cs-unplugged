"""Search index for resources model."""

from haystack import indexes
from search.search_indexes import LanguageIndex
from resources.models import Resource


class ResourceIndex(LanguageIndex, indexes.Indexable):
    """Search index for Resource model."""

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """Return the Resource model.

        Returns:
            Resource object.
        """
        return Resource
