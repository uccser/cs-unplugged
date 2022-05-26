"""Models for the classic application."""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class ClassicPage(models.Model):
    """Model for Classic CS Unplugged page in database."""

    MODEL_NAME = _("Classic CS Unplugged page")

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    redirect = models.URLField()
    search_vector = SearchVectorField(null=True)

    def get_absolute_url(self):
        """Return the canonical URL for a ClassicPage.

        Returns:
            URL as string.
        """
        return self.redirect

    def __str__(self):
        """Text representation of ClassicPage object.

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
        }

    class Meta:
        """Meta options for model."""

        indexes = [
            GinIndex(fields=['search_vector'])
        ]
