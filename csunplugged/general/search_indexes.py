"""Search index for GeneralPage model."""

from haystack import indexes
from lxml.html import fromstring
from lxml.cssselect import CSSSelector
from django.template.loader import render_to_string
from django.template.exceptions import TemplateSyntaxError
from general.models import GeneralPage

CONTENT_NOT_FOUND_ERROR_MESSAGE = ("General page requires content wrapped in "
                                   "an element with ID 'general-page-content'")


class GeneralPageIndex(indexes.SearchIndex, indexes.Indexable):
    """Search index for GeneralPage model."""

    text = indexes.CharField(document=True)

    def prepare(self, obj):
        """Set boost of GeneralPage model for index.

        Args:
            obj (GeneralPage): GeneralPage object.

        Returns:
            Dictionary of data.
        """
        data = super(GeneralPageIndex, self).prepare(obj)
        data["_boost"] = 0.8
        return data

    def prepare_text(self, obj):
        """Return text for indexing.

        Args:
            obj (GeneralPage): Object for indexing.

        Returns:
            String for indexing.
        """
        rendered = render_to_string(obj.template, {"LANGUAGE_CODE": "en"})
        html = fromstring(rendered)
        selector = CSSSelector("#general-page-content")
        try:
            contents = selector(html)[0].text_content()
        except IndexError:
            raise TemplateSyntaxError(CONTENT_NOT_FOUND_ERROR_MESSAGE)
        return contents

    def get_model(self):
        """Return the GeneralPage model.

        Returns:
            GeneralPage object.
        """
        return GeneralPage
