from haystack.generic_views import SearchView
from .forms import CustomSearchForm


class CustomSearchView(SearchView):
    """My custom search view."""

    form_class = CustomSearchForm

    def get_context_data(self, *args, **kwargs):
        context = super(CustomSearchView, self).get_context_data(*args, **kwargs)
        return context
