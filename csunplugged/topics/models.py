"""Models for the topics application."""

from collections import OrderedDict

from django.db import models
from resources.models import Resource


class GlossaryTerm(models.Model):
    """Model for glossary term in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    term = models.CharField(max_length=200, unique=True)
    definition = models.TextField()

    def __str__(self):
        """Text representation of GlossaryTerm object.

        Returns:
            Term attribute of GlossaryTerm (string).
        """
        return self.term


class LearningOutcome(models.Model):
    """Model for learning outcome in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    text = models.CharField(max_length=200, unique=True)

    def __str__(self):
        """Text representation of LearningOutcome object.

        Returns:
            Text of learning outcome (string).
        """
        return self.slug


class CurriculumArea(models.Model):
    """Model for curriculum area in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        related_name='parent_curriculum_area'
    )

    def __str__(self):
        """Text representation of CurriculumArea object.

        Returns:
            Name of curriculum area (string).
        """
        return self.name


class Topic(models.Model):
    """Model for topic in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    other_resources = models.TextField(null=True)
    icon = models.CharField(max_length=100, null=True)

    def __str__(self):
        """Text representation of Topic object.

        Returns:
            Name of topic (string).
        """
        return self.name


class UnitPlan(models.Model):
    """Model for unit plan in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='topic_unit_plans'
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
        lessons = self.unit_plan_lessons.order_by('min_age', 'max_age', 'number')
        for lesson in lessons:
            if (lesson.min_age, lesson.max_age) in grouped_lessons:
                grouped_lessons[(lesson.min_age, lesson.max_age)].append(lesson)
            else:
                grouped_lessons[(lesson.min_age, lesson.max_age)] = [lesson]
        return grouped_lessons

    def __str__(self):
        """Text representation of UnitPlan object.

        Returns:
            Name of unit plan (string).
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
            Name of difficulty level (string).
        """
        return self.name


class ProgrammingExercise(models.Model):
    """Model for programming exercise in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='topic_programming_exercises'
    )
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    exercise_set_number = models.PositiveSmallIntegerField()
    exercise_number = models.PositiveSmallIntegerField()
    content = models.TextField()
    learning_outcomes = models.ManyToManyField(
        LearningOutcome,
        related_name='programming_exercise_learning_outcomes'
    )
    difficulty = models.ForeignKey(
        ProgrammingExerciseDifficulty,
        on_delete=models.CASCADE,
        related_name='difficulty_programming_exercises'
    )

    def __str__(self):
        """Text representation of ProgrammingExercise object.

        Returns:
            Name of programming exercise (string).
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
            Name of programming language (string).
        """
        return self.name


class ProgrammingExerciseLanguageImplementation(models.Model):
    """Model for programming exercise language implementation in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='implementations'
    )
    language = models.ForeignKey(
        ProgrammingExerciseLanguage,
        on_delete=models.CASCADE,
        related_name='implementations'
    )
    exercise = models.ForeignKey(
        ProgrammingExercise,
        on_delete=models.CASCADE,
        related_name='implementations'
    )
    expected_result = models.TextField()
    hints = models.TextField(null=True)
    solution = models.TextField()

    def __str__(self):
        """Text representation of ProgrammingExerciseLanguageImplementation.

        Returns:
            Description of implementation and related exercise (string).
        """
        return '{} for exercise {}.{}, {}'.format(
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
        related_name='topic_lessons'
    )
    unit_plan = models.ForeignKey(
        UnitPlan,
        on_delete=models.CASCADE,
        related_name='unit_plan_lessons'
    )
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    duration = models.PositiveSmallIntegerField(null=True)
    content = models.TextField()
    min_age = models.PositiveSmallIntegerField()
    max_age = models.PositiveSmallIntegerField()
    programming_exercises = models.ManyToManyField(
        ProgrammingExercise,
        related_name='lessons'
    )
    learning_outcomes = models.ManyToManyField(
        LearningOutcome,
        related_name='lesson_learning_outcomes'
    )
    curriculum_areas = models.ManyToManyField(
        CurriculumArea,
        related_name='lesson_curriculum_areas',
    )
    generated_resources = models.ManyToManyField(
        Resource,
        through='ConnectedGeneratedResource',
        related_name='lesson_generated_resources'
    )

    def has_programming_exercises(self):
        """Return boolean of lesson having any programming exercises.

        Returns:
            True if the lesson has connected programming exercises.
            Otherwise False.
        """
        return bool(self.programming_exercises.all())

    def __str__(self):
        """Text representation of Lesson object.

        Returns:
            Name of lesson (string).
        """
        return self.name


class CurriculumIntegration(models.Model):
    """Model for curriculum integration in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='curriculum_integrations'
    )
    slug = models.SlugField()
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=200)
    content = models.TextField()
    curriculum_areas = models.ManyToManyField(
        CurriculumArea,
        related_name='curriculum_integrations',
    )
    prerequisite_lessons = models.ManyToManyField(
        Lesson,
        related_name='curriculum_integrations'
    )

    def has_prerequisite_lessons(self):
        """Return boolean of integration having any prerequisite lessons.

        Returns:
            True if the curriculum integration has at
            least one prerequisite lesson, otherwise False.
        """
        return bool(self.prerequisite_lessons.all())

    def __str__(self):
        """Text representation of CurriculumIntegration object.

        Returns:
            Name of curriculum integration (string).
        """
        return self.name


class ConnectedGeneratedResource(models.Model):
    """Model for relationship between resource and lesson in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
