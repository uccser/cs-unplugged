from django.db import models
from django.utils.translation import get_language
from django.contrib.postgres.fields import ArrayField, JSONField, IntegerRangeField
from django.utils.translation import get_language
from django.db.models import Q


class TranslatedModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            Q(languages__contains=[get_language()])
        )

class UntranslatedModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            ~Q(languages__contains=[get_language()])
        )


class TranslatableModel(models.Model):
    """Abstract base class for models needing to store list of available languages."""

    languages = ArrayField(models.CharField(max_length=5), size=100, default=[])

    objects = models.Manager()
    translated_objects = TranslatedModelManager()
    untranslated_objects = UntranslatedModelManager()

    class Meta:
        """Mark class as abstract."""

        abstract = True

    @property
    def translation_available(self):
        """Check if model content is available in current language."""
        return get_language() in self.languages

    # def __getattr__(self, name):
    #     if name.endswith('_no_fallback'):
    #         field = name[:-len('_no_fallback')]
    #         return getattr(self, name)
    #     else:
    #         raise AttributeError
