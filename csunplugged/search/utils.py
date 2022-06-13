"""Search utility functions."""

import copy
from django.db.models import Value
from django.contrib.postgres.search import SearchVector
from lxml.html import fromstring
from lxml.cssselect import CSSSelector
from django.template.loader import render_to_string
from django.template.exceptions import TemplateSyntaxError

CONTENT_NOT_FOUND_ERROR_MESSAGE = ("General page requires content wrapped in "
                                   "an element with ID 'general-page-content'")


def concat_field_values(*args):
    """Return string of field values for search indexing.

    Args:
        Any number of QuerySet objects, the result of value_list calls.

    Returns:
        String for search indexing.
    """
    field_names = []
    for queryset in args:
        for instance in queryset:
            for field in instance:
                field_names.append(str(field))
    return ' '.join(field_names)


def get_search_index_updater(instance):
    """Return function for updating search index of instance."""
    components = instance.index_contents()
    pk = instance.pk

    def on_commit():
        search_vector_list = []
        for weight, text in components.items():
            search_vector_list.append(
                SearchVector(Value(text), weight=weight)
            )
        search_vectors = search_vector_list[0]
        for search_vector in search_vector_list[1:]:
            search_vectors += search_vector

        instance.__class__.objects.filter(pk=pk).update(
            search_vector=search_vectors
        )
        print(f'Rebuilt index for {instance} ({instance.__class__})')
    return on_commit


def get_template_text(template):
    """Return text for indexing.

    Args:
        template (string): Path to template to get text from.

    Returns:
        String for indexing.
    """
    rendered = render_to_string(template, {"LANGUAGE_CODE": "en"})
    html = fromstring(rendered)
    selector = CSSSelector("#general-page-content")
    try:
        contents = selector(html)[0].text_content()
    except IndexError:
        raise TemplateSyntaxError(CONTENT_NOT_FOUND_ERROR_MESSAGE)
    return contents


def get_search_model_types(search_model_types_list):
    """Return dictionary of search model types.

    Args:
        search_model_types: List of dicts of search base data to
                            to be fleshed out into full dictionary.

    Return:
        Dictionary of search model types, keyed by search model ID.
    """
    model_types = dict()
    for model_data in search_model_types_list:
        model_types[get_search_model_id(model_data['class'])] = model_data
    return model_types


def get_search_model_id(model):
    """Return search ID for model.

    Args:
        model: Class to get search ID for.

    Returns:
        String identifying class.
    """
    module_name = model._meta.app_label.lower()
    class_name = model._meta.object_name.lower()
    return f'{module_name}.{class_name}'


def get_model_filter_options(search_model_types):
    """Return of model options for search type filter.

    Args:
        search_model_types (dict): Dictionary of search model type data.

    Return:
        List of dictionaries of model options.
    """
    options = []
    for (model_id, model_data) in search_model_types.items():
        options.append(
            {
                'name': model_data['class'].MODEL_NAME,
                'value': model_id,
                'selected': False,
            }
        )
    return options


def updated_model_filter_options(model_options, selected_options):
    """Update a set of model filters with selected options.

    Args:
        model_options (list): List of dictionaries of model options.
        selected_options (list): List of selected values.

    Returns:
        Updated list of dictionaries of model options.
    """
    model_options = copy.deepcopy(model_options)
    for model_option in model_options:
        if model_option['value'] in selected_options:
            model_option['selected'] = True
    return model_options
