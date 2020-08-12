"""Models for the topics application."""

from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField, IntegerRangeField
from resources.models import Resource
from utils.TranslatableModel import TranslatableModel


class GlossaryTerm(TranslatableModel):
    """Model for glossary term in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    term = models.CharField(max_length=200, unique=True)
    definition = models.TextField()

    def __str__(self):
        """Text representation of GlossaryTerm object.

        Returns:
            Term attribute of GlossaryTerm (str).
        """
        return self.term


class CurriculumArea(TranslatableModel):
    """Model for curriculum area in database."""

    MODEL_NAME = _("Curriculum Area")

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, default="")
    number = models.PositiveSmallIntegerField()
    colour = models.CharField(max_length=15)
    parent = models.ForeignKey(
        "self",
        null=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Text representation of CurriculumArea object.

        Returns:
            Name of curriculum area (str).
        """
        if self.parent:
            return "{}: {}".format(self.parent.name, self.name)
        else:
            return self.name

    class Meta:
        """Set consistent ordering of curriculum areas."""

        ordering = ["number", "name"]


class LearningOutcome(TranslatableModel):
    """Model for learning outcome in database."""

    MODEL_NAME = _("Learning Outcome")

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(max_length=80, unique=True)
    text = models.CharField(max_length=500, default="")
    curriculum_areas = models.ManyToManyField(
        CurriculumArea,
        related_name="learning_outcomes",
    )

    def __str__(self):
        """Text representation of LearningOutcome object.

        Returns:
            Text of learning outcome (str).
        """
        return self.text

    class Meta:
        """Set consistent ordering of learning outcomes."""

        ordering = ["curriculum_areas__number", "curriculum_areas__name", "text"]


class ClassroomResource(TranslatableModel):
    """Model for classroom resource."""

    MODEL_NAME = _("Classroom Resource")

    slug = models.SlugField(max_length=80, unique=True)
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        """Text representation of ClassroomResource object.

        Returns:
            Description of classroom resource (str).
        """
        return self.description


class Topic(TranslatableModel):
    """Model for topic in database."""

    MODEL_NAME = _("Topic")

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, default="")
    content = models.TextField(default="")
    other_resources = models.TextField(default="")
    icon = models.CharField(max_length=100, null=True)

    def get_absolute_url(self):
        """Return the canonical URL for a topic.

        Returns:
            URL as string.
        """
        kwargs = {
            "topic_slug": self.slug
        }
        return reverse("topics:topic", kwargs=kwargs)

    def __str__(self):
        """Text representation of Topic object.

        Returns:
            Name of topic (str).
        """
        return self.name


class UnitPlan(TranslatableModel):
    """Model for unit plan in database."""

    MODEL_NAME = _("Unit Plan")
    RETURN_TO_PARENT = _("Return to topic")

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="unit_plans"
    )
    slug = models.SlugField()
    name = models.CharField(max_length=100, default="")
    content = models.TextField(default="")
    computational_thinking_links = models.TextField(default="")
    heading_tree = JSONField(default=dict)

    def get_absolute_url(self):
        """Return the canonical URL for a unit plan.

        Returns:
            URL as string.
        """
        kwargs = {
            "topic_slug": self.topic.slug,
            "unit_plan_slug": self.slug
        }
        return reverse("topics:unit_plan", kwargs=kwargs)

    def __str__(self):
        """Text representation of UnitPlan object.

        Returns:
            Name of unit plan (str).
        """
        return self.name


class ProgrammingChallengeDifficulty(TranslatableModel):
    """Model for programming challenge difficulty in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    level = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        """Text representation of ProgrammingChallengeDifficulty object.

        Returns:
            Name of difficulty level (str).
        """
        return self.name


class ProgrammingChallenge(TranslatableModel):
    """Model for programming challenge in database."""

    MODEL_NAME = _("Programming Challenge")
    RETURN_TO_PARENT = _("Return to topic")

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="programming_challenges"
    )
    slug = models.SlugField()
    name = models.CharField(max_length=200, default="")
    challenge_set_number = models.PositiveSmallIntegerField()
    challenge_number = models.PositiveSmallIntegerField()
    content = models.TextField(default="")
    extra_challenge = models.TextField(default="")
    learning_outcomes = models.ManyToManyField(
        LearningOutcome,
        related_name="programming_challenges"
    )
    difficulty = models.ForeignKey(
        ProgrammingChallengeDifficulty,
        on_delete=models.CASCADE,
        related_name="programming_challenges"
    )

    def get_absolute_url(self):
        """Return the canonical URL for a programming challenge.

        Returns:
            URL as string.
        """
        kwargs = {
            "topic_slug": self.topic.slug,
            "programming_challenge_slug": self.slug
        }
        return reverse("topics:programming_challenge", kwargs=kwargs)

    def get_learning_outcomes(self):
        """Return an ordered QuerySet of translated learning outcomes.

        Returns:
            Ordered QuerySet.
        """
        return self.learning_outcomes(manager="translated_objects").order_by("text")

    def ordered_implementations(self):
        """Return an ordered QuerySet of implementations.

        Returns:
            Ordered QuerySet.
        """
        return self.implementations.all().order_by("language__number").select_related()

    def related_test_cases(self):
        """Return a QuerySet of test cases.

        Returns:
            QuerySet.
        """
        return self.test_cases.all().select_related()

    def __str__(self):
        """Text representation of ProgrammingChallenge object.

        Returns:
            Name of programming challenge (str).
        """
        return self.name


class ProgrammingChallengeLanguage(TranslatableModel):
    """Model for programming language in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    number = models.PositiveSmallIntegerField()
    icon = models.CharField(max_length=100, null=True)

    def __str__(self):
        """Text representation of ProgrammingChallengeLanguage object.

        Returns:
            Name of programming language (str).
        """
        return self.name


class ProgrammingChallengeImplementation(TranslatableModel):
    """Model for programming challenge language implementation in database."""

    RETURN_TO_PARENT = _("Return to programming challenge")

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="implementations"
    )
    language = models.ForeignKey(
        ProgrammingChallengeLanguage,
        on_delete=models.CASCADE,
        related_name="implementations"
    )
    challenge = models.ForeignKey(
        ProgrammingChallenge,
        on_delete=models.CASCADE,
        related_name="implementations"
    )
    expected_result = models.TextField(default="")
    hints = models.TextField(default="")
    solution = models.TextField(default="")

    def __str__(self):
        """Text representation of ProgrammingChallengeImplementation.

        Returns:
            Description of implementation and related challenge (str).
        """
        return "{} for challenge {}.{}, {}".format(
            self.language.name,
            self.challenge.challenge_set_number,
            self.challenge.challenge_number,
            self.challenge.name
        )


class AgeGroup(TranslatableModel):
    """Model for age group in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField()
    ages = IntegerRangeField()
    description = models.CharField(max_length=500, default="")

    def __str__(self):
        """Text representation of AgeGroup object.

        Returns:
            Integer group (str).
        """
        return repr(self.ages)

    class Meta:
        """Set consistent ordering of age groups."""

        ordering = ["ages"]


class Lesson(TranslatableModel):
    """Model for lesson in database."""

    MODEL_NAME = _("Lesson")
    RETURN_TO_PARENT = _("Return to unit plan")

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    unit_plan = models.ForeignKey(
        UnitPlan,
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100, default="")
    duration = models.PositiveSmallIntegerField(null=True)
    content = models.TextField(default="")
    computational_thinking_links = models.TextField(default="")
    heading_tree = JSONField(default=list)
    age_group = models.ManyToManyField(
        AgeGroup,
        through="LessonNumber",
        related_name="lessons"
    )
    programming_challenges = models.ManyToManyField(
        ProgrammingChallenge,
        through="ProgrammingChallengeNumber",
        related_name="lessons"
    )
    programming_challenges_description = models.TextField(default="")
    learning_outcomes = models.ManyToManyField(
        LearningOutcome,
        related_name="lessons"
    )
    generated_resources = models.ManyToManyField(
        Resource,
        through="ResourceDescription",
        related_name="lessons"
    )
    classroom_resources = models.ManyToManyField(
        ClassroomResource,
    )

    def has_programming_challenges(self):
        """Return boolean of lesson having any programming challenges.

        Returns:
            True if the lesson has connected programming challenges.
            Otherwise False.
        """
        return bool(self.programming_challenges.all())

    def retrieve_related_programming_challenges(self, language_filter="all"):
        """Retrieve the lesson's programming challenges and update numbers.

        Returns:
            QuerySet of programming challenges with updated numbers.
        """
        programming_challenges = self.programming_challenges.order_by(
            "challenge_set_number",
            "challenge_number",
            "name",
        )

        if language_filter != "all":
            programming_challenges = programming_challenges.filter(implementations__language__name=language_filter)

        for programming_challenge in programming_challenges:
            challenge_numbers = ProgrammingChallengeNumber.objects.get(
                lesson=self,
                programming_challenge=programming_challenge
            )
            programming_challenge.challenge_set_number = challenge_numbers.challenge_set_number
            programming_challenge.challenge_number = challenge_numbers.challenge_number
        return programming_challenges

    def challenge_languages(self):
        """Retrieve the lesson's programming challenge languages.

        Returns:
            QuerySet of languages for this lesson.
        """
        return ProgrammingChallengeLanguage.objects \
            .filter(implementations__challenge__lessons=self) \
            .distinct() \
            .order_by('name') \


    def get_absolute_url(self):
        """Return the canonical URL for a lesson.

        Returns:
            URL as string.
        """
        kwargs = {
            "topic_slug": self.topic.slug,
            "unit_plan_slug": self.unit_plan.slug,
            "lesson_slug": self.slug
        }
        return reverse("topics:lesson", kwargs=kwargs)

    def __str__(self):
        """Text representation of Lesson object.

        Returns:
            Name of lesson (str).
        """
        return self.name


class LessonNumber(models.Model):
    """Model for relationship between age group and lesson in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()

    class Meta:
        """Set consistent ordering of age groups."""

        ordering = ["number"]


class ProgrammingChallengeNumber(models.Model):
    """Model for relationship between programming challenge and lesson in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    programming_challenge = models.ForeignKey(ProgrammingChallenge, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    challenge_set_number = models.PositiveSmallIntegerField()
    challenge_number = models.PositiveSmallIntegerField()


class CurriculumIntegration(TranslatableModel):
    """Model for curriculum integration in database."""

    MODEL_NAME = _("Curriculum Integration")
    RETURN_TO_PARENT = _("Return to topic")

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="curriculum_integrations"
    )
    slug = models.SlugField()
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=200, default="")
    content = models.TextField(default="")
    curriculum_areas = models.ManyToManyField(
        CurriculumArea,
        related_name="curriculum_integrations",
    )
    prerequisite_lessons = models.ManyToManyField(
        Lesson,
        related_name="curriculum_integrations"
    )

    def has_prerequisite_lessons(self):
        """Return boolean of integration having any prerequisite lessons.

        Returns:
            True if the curriculum integration has at
            least one prerequisite lesson, otherwise False.
        """
        return bool(self.prerequisite_lessons.all())

    def get_absolute_url(self):
        """Return the canonical URL for a curriculum integration.

        Returns:
            URL as string.
        """
        kwargs = {
            "topic_slug": self.topic.slug,
            "integration_slug": self.slug
        }
        return reverse("topics:integration", kwargs=kwargs)

    def __str__(self):
        """Text representation of CurriculumIntegration object.

        Returns:
            Name of curriculum integration (str).
        """
        return self.name


class ResourceDescription(TranslatableModel):
    """Model for relationship between resource and lesson in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, default="")
