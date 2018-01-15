from django import forms
from haystack.forms import ModelSearchForm
from topics.models import (
    Lesson,
    CurriculumIntegration,
    CurriculumArea,
)


class CustomSearchForm(ModelSearchForm):

    curriculum_areas = forms.ModelMultipleChoiceField(
        queryset=CurriculumArea.objects.all(),
        required=False
    )

    def all_items(self):
        """Workaround to return all items in search index.

        See https://github.com/django-haystack/django-haystack/issues/1021

        Returns:
            Queryset of all items.
        """
        # TODO: Implement test to check all items are returned.
        return self.searchqueryset.all().exclude(content="%"*100)

    def search(self):
        if not self.is_valid():
            search_query_set = self.no_query_found()
        elif not self.cleaned_data.get('q'):
            search_query_set = self.all_items()
        else:
            search_query_set = self.searchqueryset.auto_query(self.cleaned_data['q'])
            if self.load_all:
                search_query_set = search_query_set.load_all()

        search_query_set = search_query_set.models(*self.get_models())

        # Filter items by curriculum areas if given in query
        # --------------------------------------------------------------------
        # TODO: Investigate the approach of this filter.
        #
        # Currently the given filter is provided as a QuerySet, but the search
        # index saves the curriculum areas for objects (currently only
        # curriculum integrations) as a list of primary keys, but stored as
        # strings rather than integers. This may be due to the way data is
        # stored.
        #
        # Because of this, the logic below must covert the QuerySet of the
        # filter into a list of primary key strings.
        # --------------------------------------------------------------------
        if self.cleaned_data["curriculum_areas"]:
            query_ids = list(map(str, self.cleaned_data["curriculum_areas"].values_list("pk", flat=True)))
            search_query_set = search_query_set.models(Lesson, CurriculumIntegration).filter(
                curriculum_areas__in=query_ids
            )

        return search_query_set
