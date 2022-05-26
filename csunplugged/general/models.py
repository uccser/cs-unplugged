"""Models for the general application."""

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from search.utils import get_template_text


class GeneralPage(models.Model):
    """Model for general page in database."""

    MODEL_NAME = _("General page")

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)
    search_vector = SearchVectorField(null=True)

    def get_absolute_url(self):
        """Return the canonical URL for a GeneralPage.

        Returns:
            URL as string.
        """
        return reverse(self.url_name)

    def __str__(self):
        """Text representation of GeneralPage object.

        Returns:
            Name of page (str).
        """
        return self.name

    def index_contents(self):
        """Return dictionary for search indexing.

        Returns:
            Dictionary of content for search indexing. The dictionary keys
            are the weightings of content, and the dictionary values
            are strings of content to index.
        """
        return {
            'A': self.name,
            'B': get_template_text(self.template),
        }

    class Meta:
        """Meta options for model."""

        indexes = [
            GinIndex(fields=['search_vector'])
        ]
