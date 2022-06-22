"""Models for the at a distance application."""

from os.path import join
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.TranslatableModel import TranslatableModel
from at_a_distance.settings import AT_A_DISTANCE_SLIDES_TEMPLATE_BASE_PATH


class Lesson(TranslatableModel):
    """Model for an at a distance lesson in database."""

    MODEL_NAME = _("At A Disance Lesson")

    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=200, default="")
    order_number = models.PositiveSmallIntegerField(unique=True)
    icon = models.CharField(max_length=150, null=True)
    # Content
    introduction = models.TextField(default="")
    video = models.URLField(blank=True)

    def get_absolute_url(self):
        """Return the canonical URL for an activity.

        Returns:
            URL as string.
        """
        return reverse("at_a_distance:lesson", kwargs={"lesson_slug": self.slug})

    def get_slides_path(self):
        return join(
            AT_A_DISTANCE_SLIDES_TEMPLATE_BASE_PATH,
            f'{self.slug}.html'
        )

    def __str__(self):
        """Text representation of a lesson object.

        Returns:
            Name of a lesson (str).
        """
        return self.name

    class Meta:
        """Set consistent ordering of lessons."""

        ordering = ["order_number", ]
