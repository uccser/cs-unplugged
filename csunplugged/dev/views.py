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

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['topics'] = Topic.objects.order_by('name')

        context['unit_plans'] = {}
        context['lessons'] = {}

        # build dictionaries for each unit plan and lesson
        for topic in context['topics']:
            # TODO watch this fall apart as multiple unit plans are added to same topic
            unit_plan = UnitPlan.objects.get(topic=topic)
            context['unit_plans'][topic.name] = unit_plan
            context['lessons'][unit_plan.name] = unit_plan.lessons_by_age_group()

        return context
