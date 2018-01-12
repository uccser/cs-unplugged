from django import forms
from haystack.forms import ModelSearchForm
from topics.models import CurriculumArea
from haystack.inputs import AutoQuery


class CustomSearchForm(ModelSearchForm):
    # curriculum_areas = forms.ModelMultipleChoiceField(
    #     queryset=CurriculumArea.objects.all(),
    #     required=False
    # )

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

        # if self.cleaned_data["curriculum_areas"]:
        #     search_query_set = search_query_set.filter(
        #         curriculum_areas__in=self.cleaned_data["curriculum_areas"]
        #     )

        return search_query_set
