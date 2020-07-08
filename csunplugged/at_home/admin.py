"""Admin configuration for at home application."""

from django.contrib import admin
from at_home.models import ChallengeSubmission


class ChallengeSubmissionAdmin(admin.ModelAdmin):
    """Configuration for displaying challenge submissions in admin."""

    list_display = ('datetime', 'language', 'challenge', 'answer', 'correct')
    list_filter = ('challenge', 'correct', 'language')
    ordering = ('datetime', )


admin.site.register(ChallengeSubmission, ChallengeSubmissionAdmin)
