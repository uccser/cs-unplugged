"""Views for the dev application."""

from django.views import generic

from topics.models import (
    Topic,
    CurriculumArea,
    CurriculumIntegration,
    UnitPlan,
    ProgrammingExercise,
    ProgrammingExerciseDifficulty,
    ProgrammingExerciseLanguage,
    LearningOutcome,
    GlossaryTerm,
)


class IndexView(generic.TemplateView):
    """View for the dev application homepage."""

    template_name = "dev/index.html"
    context_object_name = "all_topics"

    def get_context_data(self, **kwargs):
        """Return context for dev homepage.

        Returns:
            A dictionary of context data.
        """
        context = super(IndexView, self).get_context_data(**kwargs)

        # Get topic, unit plan and lesson lists
        context["topics"] = Topic.objects.order_by("name")
        context["unit_plans"] = []

        # Build dictionaries for each unit plan and lesson
        for topic in context["topics"]:
            topic.unit_plans = UnitPlan.objects.filter(topic=topic)
            for unit_plan in topic.unit_plans:
                unit_plan.lessons = unit_plan.lessons_by_age_group()
            topic.integrations = CurriculumIntegration.objects.filter(topic=topic).order_by("number")
            topic.programming_exercises = ProgrammingExercise.objects.filter(topic=topic).order_by(
                "exercise_set_number", "exercise_number"
            )
            context["unit_plans"] += topic.unit_plans

        # Get curriculum area list
        context["curriculum_areas"] = {}
        for parent in CurriculumArea.objects.filter(parent=None):
            context["curriculum_areas"][parent] = [child for child in CurriculumArea.objects.filter(parent=parent)]

        # Get learning outcome list
        context["learning_outcomes"] = LearningOutcome.objects.all().order_by("slug")

        # Get learning outcome list
        context["programming_exercise_languages"] = ProgrammingExerciseLanguage.objects.all()

        # Get learning outcome list
        context["programming_exercise_difficulties"] = ProgrammingExerciseDifficulty.objects.all()

        # Get glossary term list
        context["glossary_terms"] = GlossaryTerm.objects.all().order_by("term")

        return context
