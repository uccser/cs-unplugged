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
    project = models.TextField(default="", null=True, blank=True)
    more_information = models.TextField(default="")
    # The following is stored as HTML from a YAML file
    activity_steps = models.TextField(default="")
    activity_extra_information = models.TextField(default="")

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


class Challenge(TranslatableModel):
    """Model for activity challenge in database."""

    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="challenges",
    )
    order_number = models.PositiveSmallIntegerField()
    question = models.TextField(default="")
    answer = models.CharField(max_length=200, default="")
    image = models.CharField(max_length=150, null=True, blank=True)
    image_description = models.TextField(default="")

    def __str__(self):
        """Text representation of a challenge object.

        Returns:
            ID of a challenge (str).
        """
        return f"Challenge #{self.order_number}"

    class Meta:
        """Set consistent ordering of activities."""

        ordering = ["order_number", ]
        unique_together = ['activity', 'order_number']


class ChallengeSubmission(models.Model):
    """Model for activity challenge submission in database."""

    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE,
        related_name="challenge_submissions",
    )
    datetime = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=25)
    answer = models.CharField(max_length=200, default="")
    correct = models.BooleanField()
