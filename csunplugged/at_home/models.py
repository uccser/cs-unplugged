"""Models for the at home application."""

from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.TranslatableModel import TranslatableModel


class Activity(TranslatableModel):
    """Model for an activity in database."""

    MODEL_NAME = _("Activity")

    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=150, default="")
    icon = models.CharField(max_length=150, null=True)
    order_number = models.PositiveSmallIntegerField(unique=True)
    # The following are stored as HTML from Markdown files
    introduction = models.TextField(default="")
    inside_the_computer = models.TextField(default="")
    project = models.TextField(default="")
    more_information = models.TextField(default="")
    # The following is stored as HTML from a YAML file
    activity_steps = models.TextField(default="")
    # TODO: Add challenges

    def get_absolute_url(self):
        """Return the canonical URL for an activity.

        Returns:
            URL as string.
        """
        return reverse("at_home:activity", kwargs={"activity_slug": self.slug})

    def __str__(self):
        """Text representation of an activity object.

        Returns:
            Name of an activity (str).
        """
        return self.name

    class Meta:
        """Set consistent ordering of activities."""

        ordering = ["order_number", ]
