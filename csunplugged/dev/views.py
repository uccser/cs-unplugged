from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.views import generic

from topics.models import (
    Topic,
    CurriculumIntegration,
    UnitPlan,
    Lesson,
    ProgrammingExercise,
    ProgrammingExerciseLanguageImplementation,
    ConnectedGeneratedResource,
    ProgrammingExerciseDifficulty,
)


class IndexView(generic.ListView):
    template_name = 'dev/index.html'
    context_object_name = 'all_topics'

    def get_queryset(self):
        """Return all topics"""
        return Topic.objects.order_by('name')