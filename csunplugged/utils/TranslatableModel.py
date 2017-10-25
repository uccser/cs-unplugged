from django.db import models
from django.utils.translation import get_language
from django.contrib.postgres.fields import ArrayField, JSONField, IntegerRangeField


class TranslatableModel(models.Model):
    """Abstract base class for models needing to store list of available languages."""

    languages = ArrayField(models.CharField(max_length=5), size=100, default=[])

    class Meta:
        """Mark class as abstract."""

        abstract = True

    @property
    def translation_available(self):
        """Check if model content is available in current language."""
        return get_language() in self.languages
