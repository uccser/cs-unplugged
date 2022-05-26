"""Module for the search result template tag."""

from os.path import join
from django.template.defaulttags import register
from django.template.loader import render_to_string
from search.utils import get_search_model_id
from search.settings import SEARCH_RESULT_TEMPLATE_DIRECTORY, SEARCH_MODEL_TYPES


@register.simple_tag
def search_result_template(result):
    """Return the value in a dictionary given a key."""
    class_id = get_search_model_id(type(result))
    context = {'result': result}

    render_func = SEARCH_MODEL_TYPES[class_id].get('render_function', None)
    if render_func:
        context.update(render_func(result))
    template = join(SEARCH_RESULT_TEMPLATE_DIRECTORY, class_id + '.html')
    return render_to_string(template, context)
