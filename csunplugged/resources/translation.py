from modeltranslation.translator import translator, TranslationOptions
from resources.models import Resource


class ResourceTranslationOptions(TranslationOptions):
    """Translation options for Resource model."""

    fields = ("name", "content")
    fallback_undefined = {
        "content": None,
    }

translator.register(Resource, ResourceTranslationOptions)
