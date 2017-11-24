"""Models for the resources application."""

from django.db import models
from utils.TranslatableModel import TranslatableModel


class Resource(TranslatableModel):
    """Model for resource in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200, default="")
    generator_module = models.CharField(max_length=200)
    thumbnail_static_path = models.CharField(max_length=200)
    copies = models.BooleanField()
    content = models.TextField(default="")

    def __str__(self):
        """Text representation of Resource object.

        Returns:
            Name of resource (str).
        """
        return self.name
