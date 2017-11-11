"""Module for the custom translate_url template tag."""

from django.template import Library
from django.core.urlresolvers import resolve, reverse
from django.utils.translation import activate, get_language

register = Library()


@register.simple_tag(takes_context=True)
def translate_url(context, lang=None, *args, **kwargs):
    """Get active page's url for a specified language.

    Usage: {% translate_url 'en' %}
    """
    url = context["request"].path
    url_parts = resolve(url)

    cur_language = get_language()
    try:
        activate(lang)
        url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
    finally:
        activate(cur_language)

    return str(url)
