"""Module for the custom render_html_field template tag."""

from django import template
from django.template import Template, Variable, Context, TemplateSyntaxError

register = template.Library()


def render_html_with_static(html):
    """Render the HTML with the static template tag.

    Args:
        html (str): String of HTML to render.

    Returns:
        Rendered string of HTML.
    """
    return Template("{% load static %}" + html).render(Context())


@register.simple_tag
def render_html_field(html):
    return render_html_with_static(html)
