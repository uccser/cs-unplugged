"""Models for the classic application."""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class ClassicPage(models.Model):
    """Model for Classic CS Unplugged page in database."""

    MODEL_NAME = _("Classic CS Unplugged page")

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    redirect = models.URLField()

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
