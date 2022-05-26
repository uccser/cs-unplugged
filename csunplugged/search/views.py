"""Module for custom search view."""

from itertools import chain
from django.views import generic
from django.db.models import (
    F,
    # Value,
    # BooleanField,
    # Case,
    # When,
)
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
)
# from topics.models import CurriculumArea
from search.settings import (
    SEARCH_MODEL_TYPES,
    SEARCH_MODEL_FILTER_VALUES,
)
from search.utils import updated_model_filter_options


class SearchView(generic.TemplateView):
    """View for search."""

    template_name = 'search/index.html'

    def get_context_data(self, *args, **kwargs):
        """Return context dictionary for search view.

        Returns:
            Dictionary of context values.
        """
        context = super().get_context_data(*args, **kwargs)
        context['models'] = SEARCH_MODEL_FILTER_VALUES

        # Get request query parmaters
        query_text = self.request.GET.get('q')
        selected_models = self.request.GET.getlist('models')
        # selected_curriculum_areas = self.request.GET.getlist('curriculum_areas')
        get_request = bool(self.request.GET)

        if get_request:
            context['search'] = get_request

            search_request_data = SEARCH_MODEL_TYPES.copy()
            models_to_ignore = []

            for (model_id, model_data) in search_request_data.items():
                if not selected_models or model_id in selected_models:
                    model_data['results'] = model_data['class'].objects.all()
                else:
                    models_to_ignore.append(model_id)

            # Delete unused models after iterating
            for model_id in models_to_ignore:
                del search_request_data[model_id]

            # Search by text query if provided
            if query_text:
                query = SearchQuery(query_text, search_type="websearch")
                for (model_id, model_data) in search_request_data.items():
                    model_data['results'] = model_data['results'].filter(
                        search_vector=query
                    ).annotate(
                        rank=SearchRank(
                            F('search_vector'), query
                        ) + model_data['boost']
                    ).filter(
                        rank__gt=0
                    ).order_by(
                        '-rank'
                    )

            # Concatenate all results
            results = []
            for model_data in search_request_data.values():
                results.append(
                    model_data['results'].select_related(
                        *model_data['select_related']
                    ).prefetch_related(
                        *model_data['prefetch_related']
                    )
                )
            results = chain(*results)

            # Order results if query text provided
            if query_text:
                results = sorted(
                    results,
                    key=lambda instance: instance.rank,
                    reverse=True,
                )
            else:
                results = list(results)

            # Organise curriculum areas
            # curriculum_areas = CurriculumArea.objects.order_by(
            #     'number', '-parent', 'name'
            # ).values(
            #     'pk', 'colour', 'name', 'parent__pk'
            # )
            # grouped_curriculum_areas = []
            # for curriculum_area in curriculum_areas:
            #     if selected_curriculum_areas:
            #         if str(curriculum_area['pk']) in selected_curriculum_areas:
            #             curriculum_area['selected'] = 'true'
            #     if curriculum_area['parent__pk']:
            #         grouped_curriculum_areas[-1]['children'].append(curriculum_area)
            #     else:
            #         curriculum_area['children'] = []
            #         grouped_curriculum_areas.append(curriculum_area)

            context['query'] = query_text
            context['models'] = updated_model_filter_options(
                SEARCH_MODEL_FILTER_VALUES,
                selected_models,
            )
            # context['curriculum_areas'] = grouped_curriculum_areas
            context['results'] = results
            context['results_count'] = len(results)
        return context
