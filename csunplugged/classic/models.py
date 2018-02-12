"""Models for the classic application."""

from django.db import models


class ClassicPage(models.Model):
    """Model for Classic CS Unplugged page in database."""

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

    def model_type(self):
        """Text name of ClassicPage model.

        Returns:
            Name of the model (str).
        """
        return "Classic CS Unplugged page"

    def __str__(self):
        """Text representation of ClassicPage object.

        Returns:
            Name of page (str).
        """
        return self.name
