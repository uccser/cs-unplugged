"""Module for custom search view."""
from haystack.generic_views import SearchView
from .forms import CustomSearchForm


class CustomSearchView(SearchView):
    """View for custom search."""

    form_class = CustomSearchForm
