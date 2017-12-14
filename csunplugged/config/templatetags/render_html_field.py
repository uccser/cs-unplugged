"""Module for the custom render_html_field template tag."""

from django import template

register = template.Library()


def render_html_with_static(html):
    """Render the HTML with the static template tag.

    Args:
        html (str): String of HTML to render.

    Returns:
        Rendered string of HTML.
    """
    return template.Template("{% load static %}" + html).render(template.Context())


@register.simple_tag
def render_html_field(html):
    """Render the HTML with the static template tag.

    Args:
        html (str): String of HTML to render.

    Returns:
        Rendered string of HTML.
    """
    return render_html_with_static(html)
