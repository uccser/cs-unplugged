"""Search index for ClassicPage model."""

from haystack import indexes
from classic.models import ClassicPage


class ClassicPageIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for ClassicPage model."""

    text = indexes.CharField(document=True, use_template=True)

    def prepare(self, obj):
        """Set boost of ClassicPage model for index.

        Args:
            obj (ClassicPage): ClassicPage object.

        Returns:
            Dictionary of data.
        """
        data = super(ClassicPageIndex, self).prepare(obj)
        data["_boost"] = 0.6
        return data

    def get_model(self):
        """Return the Resource model.

        Returns:
            Resource object.
        """
        return ClassicPage
