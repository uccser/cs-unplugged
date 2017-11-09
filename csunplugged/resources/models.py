"""Models for the resources application."""

from django.db import models


class Resource(models.Model):
    """Model for resource in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    webpage_template = models.CharField(max_length=200)
    generator_module = models.CharField(max_length=200)
    thumbnail_static_path = models.CharField(max_length=200)
    copies = models.BooleanField()

    def __str__(self):
        """Text representation of Resource object.

        Returns:
            Name of resource (str).
        """
        return self.name
