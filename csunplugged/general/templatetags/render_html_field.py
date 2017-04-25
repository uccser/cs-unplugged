"""Module for the custom render_html_field template tag."""

from django import template
from django.template import Template, Variable, TemplateSyntaxError


class RenderHTMLFieldNode(template.Node):
    """Class used for the custom render_html_field template tag."""

    def __init__(self, item_to_be_rendered):
        """Create the RenderHTMLFieldNode object."""
        self.item_to_be_rendered = Variable(item_to_be_rendered)

    def render(self, context):
        """Render the text with the static template tag.

        Returns:
            Rendered string of text, or an empty string if the render
            fails to convert.
        """
        try:
            actual_item = '{% load static %}\n' + self.item_to_be_rendered.resolve(context)
            return Template(actual_item).render(context)
        except template.VariableDoesNotExist:
            return ''


def render_html_field(parser, token):
    """Run when the render_html_field template tag is used.

    Returns:
        Rendered string of text, or an empty string if the render
        fails to convert.
    """
    bits = token.split_contents()
    if len(bits) != 2:
        raise TemplateSyntaxError("'%s' takes only one argument"
                                  " (a variable representing a template to render)" % bits[0])
    return RenderHTMLFieldNode(bits[1])


register = template.Library()
render_html_field = register.tag(render_html_field)
