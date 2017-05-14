"""Models for the topics application."""

from collections import OrderedDict
from django.urls import reverse
from django.db import models
from django.contrib.postgres.fields import JSONField
from resources.models import Resource


class GlossaryTerm(models.Model):
    """Model for glossary term in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    term = models.CharField(max_length=200, unique=True, null=True)
    definition = models.TextField()

    def __str__(self):
        """Text representation of GlossaryTerm object.

        Returns:
            Term attribute of GlossaryTerm (str).
        """
        return self.term


class CurriculumArea(models.Model):
    """Model for curriculum area in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    colour = models.CharField(max_length=15, null=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        related_name="parent_curriculum_area"
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


class LearningOutcome(models.Model):
    """Model for learning outcome in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    text = models.CharField(max_length=200, unique=True)
    curriculum_areas = models.ManyToManyField(
        CurriculumArea,
        related_name='learning_outcomes',
    )

    def __str__(self):
        """Text representation of LearningOutcome object.

        Returns:
            Text of learning outcome (string).
        """
        return self.text


class Topic(models.Model):
    """Model for topic in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    other_resources = models.TextField(null=True)
    icon = models.CharField(max_length=100, null=True)

    def get_absolute_url(self):
        """Return the canonical URL for a programming exercise.

        Returns:
            URL as string.
        """
        kwargs = {
            "topic_slug": self.slug
        }
        return reverse("topics:topic", kwargs=kwargs)

    def model_type(self):
        """Text name of model type.

        Returns:
            Name of the model (str).
        """
        return "Topic"

    def __str__(self):
        """Text representation of Topic object.

        Returns:
            Name of topic (str).
        """
        return self.name


class UnitPlan(models.Model):
    """Model for unit plan in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="topic_unit_plans"
    )
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    content = models.TextField()

    def lessons_by_age_group(self):
        """Return ordered groups of lessons.

        Lessons are grouped by the lesson minimum age and maximum ages,
        and then order by number.

        Returns:
            A ordered dictionary of grouped lessons.
            The key is a tuple of the minimum age and maximum ages for
            the lessons.
            The value for a key is a sorted list of lessons.
            The dictionary is ordered by minimum age, then maximum age.
        """
        grouped_lessons = OrderedDict()
        lessons = self.unit_plan_lessons.order_by("min_age", "max_age", "number")
        for lesson in lessons:
            if (lesson.min_age, lesson.max_age) in grouped_lessons:
                grouped_lessons[(lesson.min_age, lesson.max_age)].append(lesson)
            else:
                grouped_lessons[(lesson.min_age, lesson.max_age)] = [lesson]
        return grouped_lessons

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

    def model_type(self):
        """Text name of model type.

        Returns:
            Name of the model (str).
        """
        return "Unit Plan"

    def __str__(self):
        """Text representation of UnitPlan object.

        Returns:
            Name of unit plan (str).
        """
        return self.name


class ProgrammingExerciseDifficulty(models.Model):
    """Model for programming exercise difficulty in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    level = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Text representation of ProgrammingExerciseDifficulty object.

        Returns:
            Name of difficulty level (str).
        """
        return self.name


class ProgrammingExercise(models.Model):
    """Model for programming exercise in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="topic_programming_exercises"
    )
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    exercise_set_number = models.PositiveSmallIntegerField()
    exercise_number = models.PositiveSmallIntegerField()
    content = models.TextField()
    extra_challenge = models.TextField(null=True)
    learning_outcomes = models.ManyToManyField(
        LearningOutcome,
        related_name="programming_exercise_learning_outcomes"
    )
    difficulty = models.ForeignKey(
        ProgrammingExerciseDifficulty,
        on_delete=models.CASCADE,
        related_name="difficulty_programming_exercises"
    )

    def get_absolute_url(self):
        """Return the canonical URL for a programming exercise.

        Returns:
            URL as string.
        """
        kwargs = {
            "topic_slug": self.topic.slug,
            "programming_exercise_slug": self.slug
        }
        return reverse("topics:programming_exercise", kwargs=kwargs)

    def model_type(self):
        """Text name of model type.

        Returns:
            Name of the model (str).
        """
        return "Programming Challenge"

    def __str__(self):
        """Text representation of ProgrammingExercise object.

        Returns:
            Name of programming exercise (str).
        """
        return self.name


class ProgrammingExerciseLanguage(models.Model):
    """Model for programming language in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, null=True)

    def __str__(self):
        """Text representation of ProgrammingExerciseLanguage object.

        Returns:
            Name of programming language (str).
        """
        return self.name


class ProgrammingExerciseLanguageImplementation(models.Model):
    """Model for programming exercise language implementation in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="implementations"
    )
    language = models.ForeignKey(
        ProgrammingExerciseLanguage,
        on_delete=models.CASCADE,
        related_name="implementations"
    )
    exercise = models.ForeignKey(
        ProgrammingExercise,
        on_delete=models.CASCADE,
        related_name="implementations"
    )
    expected_result = models.TextField()
    hints = models.TextField(null=True)
    solution = models.TextField()

    def __str__(self):
        """Text representation of ProgrammingExerciseLanguageImplementation.

        Returns:
            Description of implementation and related exercise (str).
        """
        return "{} for exercise {}.{}, {}".format(
            self.language.name,
            self.exercise.exercise_set_number,
            self.exercise.exercise_number,
            self.exercise.name
        )


class Lesson(models.Model):
    """Model for lesson in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="topic_lessons"
    )
    unit_plan = models.ForeignKey(
        UnitPlan,
        on_delete=models.CASCADE,
        related_name="unit_plan_lessons"
    )
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    duration = models.PositiveSmallIntegerField(null=True)
    content = models.TextField()
    min_age = models.PositiveSmallIntegerField()
    max_age = models.PositiveSmallIntegerField()
    heading_tree = JSONField(null=True)
    programming_exercises = models.ManyToManyField(
        ProgrammingExercise,
        related_name="lessons"
    )
    learning_outcomes = models.ManyToManyField(
        LearningOutcome,
        related_name="lesson_learning_outcomes"
    )
    generated_resources = models.ManyToManyField(
        Resource,
        through="ConnectedGeneratedResource",
        related_name="lesson_generated_resources"
    )

    def has_programming_exercises(self):
        """Return boolean of lesson having any programming exercises.

        Returns:
            True if the lesson has connected programming exercises.
            Otherwise False.
        """
        return bool(self.programming_exercises.all())

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

    def model_type(self):
        """Text name of model type.

        Returns:
            Name of the model (str).
        """
        return "Lesson"

    def __str__(self):
        """Text representation of Lesson object.

        Returns:
            Name of lesson (str).
        """
        return self.name


class CurriculumIntegration(models.Model):
    """Model for curriculum integration in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="curriculum_integrations"
    )
    slug = models.SlugField()
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=200)
    content = models.TextField()
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

    def model_type(self):
        """Text name of model type.

        Returns:
            Name of the model (str).
        """
        return "Curriculum Integration"

    def __str__(self):
        """Text representation of CurriculumIntegration object.

        Returns:
            Name of curriculum integration (str).
        """
        return self.name


class ConnectedGeneratedResource(models.Model):
    """Model for relationship between resource and lesson in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
