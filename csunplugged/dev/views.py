from django.views import generic

from topics.models import (
    Topic,
    CurriculumArea,
    CurriculumIntegration,
    UnitPlan,
    ProgrammingExercise,
)


class IndexView(generic.ListView):
    template_name = 'dev/index.html'
    context_object_name = 'all_topics'

    def get_queryset(self):
        """Return all topics"""
        return Topic.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Get topic, unit plan and lesson lists
        context['topics'] = Topic.objects.order_by('name')
        context['unit_plans'] = []

        # Build dictionaries for each unit plan and lesson
        for topic in context['topics']:
            topic.unit_plans = UnitPlan.objects.filter(topic=topic)
            for unit_plan in topic.unit_plans:
                unit_plan.lessons = unit_plan.lessons_by_age_group()
            context['unit_plans'] += topic.unit_plans
        print(context['unit_plans'])

        # Get curriculum area clist
        context['curriculum_areas'] = CurriculumArea.objects.all()

        # Get curriculum integration list
        context['cur_int_activites'] = CurriculumIntegration.objects.all()

        # Get programming exercise list
        context['programming_exercises'] = ProgrammingExercise.objects.all().order_by(
            'exercise_set_number', 'exercise_number'
        )

        return context
