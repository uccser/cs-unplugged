from django.db import models
from resources.models import Resource

class LearningOutcome(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    text = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.text


class CurriculumLink(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ClassroomResource(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    text = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.text


class Age(models.Model):
#  Auto-incrementing 'id' field is automatically set by Django
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.age


class Topic(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    other_resources = models.TextField()
    icon = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class UnitPlan(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='topic_unit_plans'
    )
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
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
    content = models.TextField()
    ages = models.ManyToManyField(
        Age,
        related_name='lesson_ages'
    )
    learning_outcomes = models.ManyToManyField(
        LearningOutcome,
        related_name='lesson_learning_outcomes'
    )
    curriculum_links = models.ManyToManyField(
        CurriculumLink,
        related_name='lesson_curriculum_links'
    )
    classroom_resources = models.ManyToManyField(
        ClassroomResource,
        related_name='lesson_classroom_resources'
    )
    generated_resources = models.ManyToManyField(
        Resource,
        through='ConnectedGeneratedResource',
        related_name='lesson_generated_resources'
    )

    def __str__(self):
        return self.name


class FollowUpActivity(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='topic_follow_up_activities'
    )
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    content = models.TextField()
    curriculum_links = models.ManyToManyField(
        CurriculumLink,
        related_name='follow_up_activity_curriculum_links'
    )

    def __str__(self):
        return self.name


class ProgrammingExerciseDifficulty(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    level = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProgrammingExercise(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='topic_programming_exercises'
    )
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    exercise_number = models.IntegerField()
    content = models.TextField()
    scratch_hints = models.TextField()
    scratch_solution = models.TextField()
    python_hints = models.TextField()
    python_solution = models.TextField()
    learning_outcomes = models.ManyToManyField(
        LearningOutcome,
        related_name='programming_exercise_learning_outcomes'
    )

    def __str__(self):
        return self.name


class ConnectedGeneratedResource(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
