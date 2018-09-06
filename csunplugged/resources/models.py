"""Models for the resources application."""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from utils.TranslatableModel import TranslatableModel


class Resource(TranslatableModel):
    """Model for resource in database."""

    MODEL_NAME = _("Printable")

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200, default="")
    generator_module = models.CharField(max_length=200)
    copies = models.BooleanField()
    content = models.TextField(default="")

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

    class Meta:
        """Meta class settings."""

        ordering = ["name"]
