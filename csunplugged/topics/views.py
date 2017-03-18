from django.shortcuts import get_object_or_404
from django.views import generic

from .models import (
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
    template_name = 'topics/index.html'
    context_object_name = 'all_topics'

    def get_queryset(self):
        """Return all topics"""
        return Topic.objects.order_by('name')


class TopicView(generic.DetailView):
    model = Topic
    template_name = 'topics/topic.html'
    slug_url_kwarg = 'topic_slug'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TopicView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the connected unit plans
        context['unit_plans'] = UnitPlan.objects.filter(topic=self.object).order_by('name')
        # Add in a QuerySet of all the connected programming exercises
        programming_exercises = ProgrammingExercise.objects.filter(topic=self.object)
        context['programming_exercises'] = programming_exercises.order_by('exercise_set_number', 'exercise_number')
        # Add in a QuerySet of all the connected curriculum integrations
        context['curriculum_integrations'] = CurriculumIntegration.objects.filter(topic=self.object).order_by('number')
        return context


class UnitPlanView(generic.DetailView):
    model = UnitPlan
    template_name = 'topics/unit_plan.html'
    context_object_name = 'unit_plan'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get('topic_slug', None),
            slug=self.kwargs.get('unit_plan_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnitPlanView, self).get_context_data(**kwargs)
        # Loading object under consistent context names for breadcrumbs
        context['topic'] = self.object.topic
        # Add all the connected lessons
        context['lessons'] = self.object.unit_plan_lessons.order_by('min_age', 'max_age', 'number')
        return context


class LessonView(generic.DetailView):
    model = Lesson
    template_name = 'topics/lesson.html'
    context_object_name = 'lesson'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get('topic_slug', None),
            unit_plan__slug=self.kwargs.get('unit_plan_slug', None),
            slug=self.kwargs.get('lesson_slug', None),
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LessonView, self).get_context_data(**kwargs)
        # Loading objects under consistent context names for breadcrumbs
        context['topic'] = self.object.topic
        context['unit_plan'] = self.object.unit_plan
        # Add all the connected curriculum links
        context['lesson_curriculum_links'] = self.object.curriculum_links.all()
        # Add all the connected learning outcomes
        context['lesson_learning_outcomes'] = self.object.learning_outcomes.all()
        # Add all the connected classroom resources
        context['lesson_classroom_resources'] = self.object.classroom_resources.all()
        # Add all the connected generated resources
        related_resources = self.object.generated_resources.all()
        generated_resources = []
        for related_resource in related_resources:
            generated_resource = dict()
            generated_resource['slug'] = related_resource.slug
            generated_resource['name'] = related_resource.name
            generated_resource['thumbnail'] = related_resource.thumbnail_static_path
            relationship = ConnectedGeneratedResource.objects.get(resource=related_resource, lesson=self.object)
            generated_resource['description'] = relationship.description
            generated_resources.append(generated_resource)
        context['lesson_generated_resources'] = generated_resources

        return context


class ProgrammingExerciseList(generic.ListView):
    model = ProgrammingExercise
    template_name = 'topics/programming_exercise_list.html'
    context_object_name = 'all_programming_exercises'

    def get_queryset(self, **kwargs):
        """Return all activities for topic"""
        topic_slug = self.kwargs.get('topic_slug', None)
        exercises = ProgrammingExercise.objects.filter(topic__slug=topic_slug)
        return exercises.order_by('exercise_set_number', 'exercise_number')

    def get_context_data(self, **kwargs):
        context = super(ProgrammingExerciseList, self).get_context_data(**kwargs)
        # Loading objects under consistent context names for breadcrumbs
        context['topic'] = get_object_or_404(Topic, slug=self.kwargs.get('topic_slug', None))
        return context


class ProgrammingExerciseView(generic.DetailView):
    model = ProgrammingExercise
    template_name = 'topics/programming_exercise.html'
    context_object_name = 'programming_exercise'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get('topic_slug', None),
            slug=self.kwargs.get('programming_exercise_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProgrammingExerciseView, self).get_context_data(**kwargs)
        # Loading object under consistent context names for breadcrumbs
        context['topic'] = self.object.topic
        # Add all the connected learning outcomes
        context['programming_exercise_learning_outcomes'] = self.object.learning_outcomes.all()
        context['implementations'] = self.object.implementations.all().select_related()
        return context


class ProgrammingExerciseLanguageSolutionView(generic.DetailView):
    model = ProgrammingExerciseLanguageImplementation
    template_name = 'topics/programming_exercise_language_solution.html'
    context_object_name = 'implementation'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get('topic_slug', None),
            exercise__slug=self.kwargs.get('programming_exercise_slug', None),
            language__slug=self.kwargs.get('programming_language_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProgrammingExerciseLanguageSolutionView, self).get_context_data(**kwargs)
        # Loading object under consistent context names for breadcrumbs
        context['topic'] = self.object.topic
        context['programming_exercise'] = self.object.exercise
        return context


class CurriculumIntegrationList(generic.ListView):
    model = CurriculumIntegration
    template_name = 'topics/curriculum_integration_list.html'
    context_object_name = 'all_curriculum_integrations'

    def get_queryset(self, **kwargs):
        """Return all integrations for topic"""
        return CurriculumIntegration.objects.filter(
            topic__slug=self.kwargs.get('topic_slug', None)
        ).select_related().order_by('number')

    def get_context_data(self, **kwargs):
        context = super(CurriculumIntegrationList, self).get_context_data(**kwargs)
        # Loading objects under consistent context names for breadcrumbs
        context['topic'] = get_object_or_404(Topic, slug=self.kwargs.get('topic_slug', None))
        return context


class CurriculumIntegrationView(generic.DetailView):
    model = CurriculumIntegration
    queryset = CurriculumIntegration.objects.all()
    template_name = 'topics/curriculum_integration.html'
    context_object_name = 'integration'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get('topic_slug', None),
            slug=self.kwargs.get('integration_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CurriculumIntegrationView, self).get_context_data(**kwargs)
        # Loading objects under consistent context names for breadcrumbs
        context['topic'] = self.object.topic
        # Add in a QuerySet of all the connected curriculum links
        context['integration_curriculum_links'] = self.object.curriculum_links.all()
        return context


class OtherResourcesView(generic.DetailView):
    model = Topic
    template_name = 'topics/topic-other-resources.html'
    slug_url_kwarg = 'topic_slug'


class ProgrammingExerciseDifficultyView(generic.DetailView):
    model = ProgrammingExerciseDifficulty
    template_name = 'topics/programming_exercise_difficulty.html'
    context_object_name = 'difficulty'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model,
            level=self.kwargs.get('programming_exercise_difficulty_level', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProgrammingExerciseDifficultyView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the connected programming exercises
        context['programming_exercises'] = self.object.difficulty_programming_exercises.all()
        return context
