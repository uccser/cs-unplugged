"""Views for the topics application."""

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import JsonResponse, Http404
from config.templatetags.render_html_field import render_html_with_static
from topics.utils.add_lesson_ages_to_objects import add_lesson_ages_to_objects
from resources.utils.get_thumbnail import get_thumbnail_static_path_for_resource
from utils.translated_first import translated_first
from utils.group_lessons_by_age import group_lessons_by_age
from django.utils.translation import get_language
from .models import (
    Topic,
    CurriculumIntegration,
    UnitPlan,
    Lesson,
    LessonNumber,
    ProgrammingChallenge,
    ProgrammingChallengeNumber,
    ProgrammingChallengeImplementation,
    ResourceDescription,
    GlossaryTerm,
)


class IndexView(generic.ListView):
    """View for the topics application homepage."""

    template_name = "topics/index.html"
    context_object_name = "topics"

    def get_queryset(self):
        """Get queryset of all topics.

        Returns:
            Queryset of Topic objects ordered by name.
        """
        topics = Topic.objects.order_by("name").prefetch_related(
            "unit_plans",
            "lessons",
            "curriculum_integrations",
            "programming_challenges",
        )
        return translated_first(topics)

    def get_context_data(self, **kwargs):
        """Provide the context data for the index view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        add_lesson_ages_to_objects(self.object_list)
        return context


class TopicView(generic.DetailView):
    """View for a specific topic."""

    model = Topic
    template_name = "topics/topic.html"
    slug_url_kwarg = "topic_slug"

    def get_context_data(self, **kwargs):
        """Provide the context data for the topic view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(TopicView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the connected unit plans
        unit_plans = self.object.unit_plans.order_by("name")
        context["unit_plans"] = add_lesson_ages_to_objects(unit_plans)
        # Add in a QuerySet of all the connected curriculum integrations
        context["curriculum_integrations"] = self.object.curriculum_integrations.order_by("number")
        return context


class UnitPlanView(generic.DetailView):
    """View for a specific unit plan."""

    model = UnitPlan
    template_name = "topics/unit-plan.html"
    context_object_name = "unit_plan"

    def get_object(self, **kwargs):
        """Retrieve object for the unit plan view.

        Returns:
            UnitPlan object, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            slug=self.kwargs.get("unit_plan_slug", None)
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the unit plan view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(UnitPlanView, self).get_context_data(**kwargs)
        # Loading object under consistent context names for breadcrumbs
        context["topic"] = self.object.topic
        # Add all the connected lessons
        context["grouped_lessons"] = group_lessons_by_age(self.object.lessons.all())
        return context


class UnitPlanDescriptionView(generic.DetailView):
    """View for a specific unit plan."""

    model = UnitPlan
    template_name = "topics/unit-plan-description.html"
    context_object_name = "unit_plan"

    def get_object(self, **kwargs):
        """Retrieve object for the unit plan view.

        Returns:
            UnitPlan object, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            slug=self.kwargs.get("unit_plan_slug", None)
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the unit plan view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(UnitPlanDescriptionView, self).get_context_data(**kwargs)
        # Loading object under consistent context names for breadcrumbs
        context["topic"] = self.object.topic
        return context


class LessonView(generic.DetailView):
    """View for a specific lesson."""

    model = Lesson
    template_name = "topics/lesson.html"
    context_object_name = "lesson"

    def get_object(self, **kwargs):
        """Retrieve object for the lesson view.

        Returns:
            Lesson object, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            unit_plan__slug=self.kwargs.get("unit_plan_slug", None),
            slug=self.kwargs.get("lesson_slug", None),
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the lesson view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(LessonView, self).get_context_data(**kwargs)
        # Loading objects under consistent context names for breadcrumbs
        context["lesson_ages"] = []
        for age_group in self.object.age_group.order_by("ages"):
            number = LessonNumber.objects.get(lesson=self.object, age_group=age_group).number
            context["lesson_ages"].append(
                {
                    "lower": age_group.ages.lower,
                    "upper": age_group.ages.upper,
                    "number": number,
                }
            )
        context["topic"] = self.object.topic
        context["unit_plan"] = self.object.unit_plan
        # Add all the connected programming challenges
        context["programming_challenges"] = self.object.programming_challenges.exists()
        # Add all the connected learning outcomes
        context["learning_outcomes"] = self.object.learning_outcomes(manager="translated_objects").order_by("text")
        context["classroom_resources"] = self.object.classroom_resources(manager="translated_objects").order_by(
            "description"
        )
        # Add all the connected generated resources
        related_resources = self.object.generated_resources.order_by("name")
        generated_resources = []
        for related_resource in related_resources:
            generated_resource = dict()
            generated_resource["slug"] = related_resource.slug
            generated_resource["name"] = related_resource.name
            generated_resource["thumbnail"] = get_thumbnail_static_path_for_resource(related_resource)
            relationship = ResourceDescription.objects.get(resource=related_resource, lesson=self.object)
            generated_resource["description"] = relationship.description
            generated_resources.append(generated_resource)
        context["generated_resources"] = generated_resources

        return context


class ProgrammingChallengeList(generic.base.TemplateView):
    """View for listing all programming challenges for a lesson."""

    template_name = "topics/programming-challenge-lesson-list.html"

    def get_context_data(self, **kwargs):
        """Provide the context data for the programming challenge list view.

        Returns:
            Dictionary of context data.
        """
        context = super(ProgrammingChallengeList, self).get_context_data(**kwargs)
        lesson = get_object_or_404(
            Lesson.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            unit_plan__slug=self.kwargs.get("unit_plan_slug", None),
            slug=self.kwargs.get("lesson_slug", None),
        )
        context["lesson"] = lesson
        context["programming_challenges"] = lesson.retrieve_related_programming_challenges()
        context["unit_plan"] = lesson.unit_plan
        context["topic"] = lesson.topic
        return context


class ProgrammingChallengeView(generic.DetailView):
    """View for a specific programming challenge."""

    model = ProgrammingChallenge
    template_name = "topics/programming-challenge.html"
    context_object_name = "programming_challenge"

    def get_object(self, **kwargs):
        """Retrieve object for the programming challenge view.

        Returns:
            ProgrammingChallenge object, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            slug=self.kwargs.get("programming_challenge_slug", None)
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the programming challenge view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(ProgrammingChallengeView, self).get_context_data(**kwargs)
        context["lessons"] = self.object.lessons.all()
        for lesson in context["lessons"]:
            challenge_numbers = ProgrammingChallengeNumber.objects.get(
                lesson=lesson,
                programming_challenge=self.object
            )
            lesson.challenge_set_number = challenge_numbers.challenge_set_number
            lesson.challenge_number = challenge_numbers.challenge_number
        context["topic"] = self.object.topic
        # Add all the connected learning outcomes
        context["learning_outcomes"] = self.object.learning_outcomes(manager="translated_objects").order_by("text")
        context["implementations"] = self.object.ordered_implementations()
        return context


class ProgrammingChallengeLanguageSolutionView(generic.DetailView):
    """View for a language implementation for a programming challenge."""

    model = ProgrammingChallengeImplementation
    template_name = "topics/programming-challenge-language-solution.html"
    context_object_name = "implementation"

    def get_object(self, **kwargs):
        """Retrieve object for the language implementation view.

        Returns:
            ProgrammingChallengeImplementation object, or raises 404
            error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            challenge__slug=self.kwargs.get("programming_challenge_slug", None),
            language__slug=self.kwargs.get("programming_language_slug", None)
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the language implementation view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(ProgrammingChallengeLanguageSolutionView, self).get_context_data(**kwargs)
        # Loading object under consistent context names for breadcrumbs
        context["topic"] = self.object.topic
        context["programming_challenge"] = self.object.challenge
        return context


class AllCurriculumIntegrationList(generic.ListView):
    """View for listing all curriculum integrations."""

    model = CurriculumIntegration
    template_name = "topics/all-curriculum-integration-list.html"
    context_object_name = "curriculum_integrations"

    def get_queryset(self, **kwargs):
        """Retrieve all curriculum integrations.

        Returns:
            Queryset of CurriculumIntegration objects.
        """
        return CurriculumIntegration.objects.select_related().order_by("topic__name", "number")


class CurriculumIntegrationView(generic.DetailView):
    """View for a specific curriculum integration."""

    model = CurriculumIntegration
    queryset = CurriculumIntegration.objects.all()
    template_name = "topics/curriculum-integration.html"
    context_object_name = "integration"

    def get_object(self, **kwargs):
        """Retrieve object for the curriculum integration view.

        Returns:
            CurriculumIntegration object, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            slug=self.kwargs.get("integration_slug", None)
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the curriculum integration view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(CurriculumIntegrationView, self).get_context_data(**kwargs)
        # Loading objects under consistent context names for breadcrumbs
        context["topic"] = self.object.topic
        # Add in a QuerySet of all the connected curriculum areas
        context["integration_curriculum_areas"] = self.object.curriculum_areas.order_by("name")
        # Add in a QuerySet of all the prerequisite lessons
        context["prerequisite_lessons"] = self.object.prerequisite_lessons.select_related().order_by(
            "unit_plan__name",
            "lessonnumber",
        )
        return context


class OtherResourcesView(generic.DetailView):
    """View for detailing other resources for a specific topic."""

    model = Topic
    template_name = "topics/topic-other-resources.html"
    slug_url_kwarg = "topic_slug"


class GlossaryList(generic.ListView):
    """Provide glossary view of all terms."""

    template_name = "topics/glossary.html"
    context_object_name = "glossary_terms"

    def get_queryset(self):
        """Get queryset of all glossary terms.

        Returns:
            Queryset of GlossaryTerm objects ordered by term.
        """
        return GlossaryTerm.objects.order_by("term")

    def get_context_data(self):
        """Get context data for template rendering."""
        term_locale = "term_" + get_language().replace("-", "_")
        return {
            "glossary_terms": GlossaryTerm.objects.filter(
                Q(languages__contains=[get_language()])
            ).order_by(term_locale),
            "untranslated_glossary_terms": GlossaryTerm.objects.filter(
                ~Q(languages__contains=[get_language()])
            ).order_by("term_en")
        }


def glossary_json(request, **kwargs):
    """Provide JSON data for glossary term.

    Args:
        request: The HTTP request.

    Returns:
        JSON response is sent containing data for the requested term.

    Raises:
        404 error if term not found.
    """
    # If term parameter, then return JSON
    if "term" in request.GET:
        glossary_slug = request.GET.get("term")
        glossary_item = get_object_or_404(
            GlossaryTerm,
            slug=glossary_slug
        )
        data = {
            "slug": glossary_slug,
            "translated": glossary_item.translation_available,
            "term": glossary_item.term,
            "definition": render_html_with_static(glossary_item.definition)
        }
        return JsonResponse(data)
    else:
        raise Http404("Term parameter not specified.")
