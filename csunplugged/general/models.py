"""Models for the general application."""

from django.db import models
from django.urls import reverse


class GeneralPage(models.Model):
    """Model for general page in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Return the canonical URL for a GeneralPage.

        Returns:
            URL as string.
        """
        return reverse(self.url_name)

    def model_type(self):
        """Text name of GeneralPage model.

        Returns:
            Name of the model (str).
        """
        return "General page"

    def __str__(self):
        """Text representation of GeneralPage object.

        Returns:
            Name of page (str).
        """
        return self.name
