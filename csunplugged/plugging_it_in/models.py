"""Models for the plugging_it_in application."""

from django.db import models
from utils.TranslatableModel import TranslatableModel
from topics.models import ProgrammingChallenge


class TestCase(TranslatableModel):
    """Model for a test case linked to a programming challenge question."""

    number = models.PositiveSmallIntegerField(default=1)
    test_input = models.TextField(blank=True)
    expected_output = models.TextField(blank=True)
    question_type = models.CharField(max_length=20)
    challenge = models.ForeignKey(
        ProgrammingChallenge,
        on_delete=models.CASCADE,
        related_name="test_cases"
    )

    class Meta:
        """Meta information for class."""

        verbose_name = 'Test Case'
