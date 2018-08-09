from haystack.indexes import SearchIndex
from django.utils import translation
from utils.search_index_utils import get_search_index_language


class LanguageIndex(SearchIndex):

    def index_queryset(self, using=None):
        """
        Get the default QuerySet to index when doing a full update.
        Subclasses can override this method to avoid indexing certain objects.
        """
        with translation.override(get_search_index_language(using)):
            objects = self.get_model().translated_objects.all()
        return objects
