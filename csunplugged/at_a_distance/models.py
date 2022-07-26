"""Models for the at a distance application."""

from os.path import join
from django.urls import reverse
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _
from utils.TranslatableModel import TranslatableModel
from at_a_distance.settings import AT_A_DISTANCE_SLIDES_TEMPLATE_BASE_PATH


class LessonManager(models.Manager):
    """Custom manager for Lesson class."""

    def get_queryset(self):
        """Prefetch related supporting resources."""
        return super().get_queryset().prefetch_related('supporting_resources')


class Lesson(TranslatableModel):
    """Model for an at a distance lesson in database."""

    MODEL_NAME = _("At A Disance Lesson")

    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=200, default="")
    order_number = models.PositiveSmallIntegerField()
    icon = models.CharField(max_length=150, null=True)
    objects = LessonManager()

    # Suitability attributes
    NOT_SUITABLE = 'not-suitable'
    SUITABLE = 'suitable'
    NOT_RECOMMENDED = 'not-recommended'
    SUITABILITY_CHOICES = [
        (NOT_SUITABLE, _('Not suitable')),
        (SUITABLE, _('Suitable')),
        (NOT_RECOMMENDED, _('Not recommended')),
    ]
    suitable_for_teaching_students = models.CharField(
        max_length=15,
        choices=SUITABILITY_CHOICES,
        default=NOT_SUITABLE,
    )
    suitable_for_teaching_educators = models.CharField(
        max_length=15,
        choices=SUITABILITY_CHOICES,
        default=NOT_SUITABLE,
    )

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
        """Return the path to the lesson slides."""
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


class SupportingResourceManager(models.Manager):
    """Custom manager for SupportingResource class."""

    def get_queryset(self):
        """Return supporting resources for the current language."""
        return super().get_queryset().filter(language=get_language())


class SupportingResource(models.Model):
    """Model for a supporting resource to a lesson.

    This model is not translatable as supporting resources may be
    completely different for each language.
    """

    order_number = models.PositiveSmallIntegerField()
    text = models.TextField()
    url = models.URLField()
    language = models.CharField(max_length=10)
    lesson = models.ForeignKey(
        Lesson,
        null=True,
        related_name="supporting_resources",
        on_delete=models.CASCADE,
    )
    objects = SupportingResourceManager()

    class Meta:
        """Set consistent ordering of supporting resources."""

        ordering = ["order_number", ]
