from modeltranslation.utils import fallbacks
from django import template

def disable_translation_fallback(parser, token):
    nodelist = parser.parse(('end_disable_translation_fallback',))
    parser.delete_first_token()
    return DisableTranslationFallbackNode(nodelist)

class DisableTranslationFallbackNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        with fallbacks(False):
            output = self.nodelist.render(context)
        return output

register = template.Library()
disable_translation_fallback = register.tag(disable_translation_fallback)
