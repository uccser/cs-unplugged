"""Models for the resources application."""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from utils.TranslatableModel import TranslatableModel
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class Resource(TranslatableModel):
    """Model for resource in database."""

    MODEL_NAME = _("Printable")

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200, default="")
    generator_module = models.CharField(max_length=200)
    copies = models.BooleanField()
    content = models.TextField(default="")
    search_vector = SearchVectorField(null=True)

    def get_absolute_url(self):
        """Return the canonical URL for a resource.

        Returns:
            URL as string.
        """
        kwargs = {
            "resource_slug": self.slug
        }
        return reverse("resources:resource", kwargs=kwargs)

    def __str__(self):
        """Text representation of Resource object.

        Returns:
            Name of resource (str).
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
            'B': self.content,
        }

    class Meta:
        """Meta options for model."""

        ordering = ["name"]
        indexes = [
            GinIndex(fields=['search_vector'])
        ]
