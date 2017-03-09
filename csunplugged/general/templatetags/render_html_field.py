from django import template
from django.template import Template, Variable, TemplateSyntaxError


class RenderHTMLFieldNode(template.Node):
    def __init__(self, item_to_be_rendered):
        self.item_to_be_rendered = Variable(item_to_be_rendered)

    def render(self, context):
        try:
            actual_item = '{% load static %}\n' + self.item_to_be_rendered.resolve(context)
            return Template(actual_item).render(context)
        except template.VariableDoesNotExist:
            return ''


def render_html_field(parser, token):
    bits = token.split_contents()
    if len(bits) != 2:
        raise TemplateSyntaxError("'%s' takes only one argument"
                                  " (a variable representing a template to render)" % bits[0])
    return RenderHTMLFieldNode(bits[1])


register = template.Library()
render_html_field = register.tag(render_html_field)
