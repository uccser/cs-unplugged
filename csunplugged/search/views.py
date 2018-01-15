"""Module for custom search view."""
from haystack.generic_views import SearchView
from django.db.models.functions import Concat
from search.forms import CustomSearchForm
from topics.models import CurriculumArea


class CustomSearchView(SearchView):
    """View for custom search."""

    form_class = CustomSearchForm

    def get_context_data(self, *args, **kwargs):
        """Return context dictionary for custom search view.

        Returns:
            Dictionary of context values.
        """
        context = super(CustomSearchView, self).get_context_data(*args, **kwargs)
        context["curriculum_areas"] = CurriculumArea.objects.annotate(
            display_name=Concat("parent__name", "name")
        ).order_by("display_name").values("pk", "colour", "parent__name", "name")
        return context
