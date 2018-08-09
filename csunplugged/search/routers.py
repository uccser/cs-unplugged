from haystack.routers import BaseRouter
from utils.search_index_utils import get_search_index_name
from django.utils.translation import get_language


class MultiLanguageRouter(BaseRouter):
    def for_read(self, **hints):
        return get_search_index_name(get_language())

    def for_write(self, **hints):
        return get_search_index_name(get_language())
