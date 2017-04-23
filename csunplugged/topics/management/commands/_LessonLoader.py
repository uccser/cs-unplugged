"""Custom loader for loading a lesson."""

import os.path
from utils.BaseLoader import BaseLoader
from topics.models import (
    ProgrammingExercise,
    LearningOutcome,
    CurriculumArea,
    ClassroomResource,
    Resource,
    ConnectedGeneratedResource,
)


class LessonLoader(BaseLoader):
    """Custom loader for loading a lesson."""

    def __init__(self, load_log, lesson_slug, lesson_structure, topic, unit_plan, BASE_PATH):
        """Create the loader for loading a lesson.

        Args:
            load_log: List of log messages (list).
            lesson_slug: Slug of lesson (string).
            lesson_structure: Data for lesson (dict).
            topic: Object of Topic model.
            unit_plan: Object of UnitPlan model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH, load_log)
        self.lesson_slug = lesson_slug
        self.lesson_structure = lesson_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """Load the content for a lesson."""
        lesson_content = self.convert_md_file(os.path.join(self.BASE_PATH, self.lesson_structure['md-file']))
        lesson = self.topic.topic_lessons.create(
            unit_plan=self.unit_plan,
            slug=self.lesson_slug,
            name=lesson_content.title,
            number=self.lesson_structure['number'],
            content=lesson_content.html_string,
            min_age=self.lesson_structure['minimum-age'],
            max_age=self.lesson_structure['maximum-age']
        )
        lesson.save()

        # Add programming exercises
        if 'programming-exercises' in self.lesson_structure:
            programming_exercise_slugs = self.lesson_structure['programming-exercises']
            for programming_exercise_slug in programming_exercise_slugs:
                programming_exercise = ProgrammingExercise.objects.get(
                    slug=programming_exercise_slug
                )
                lesson.programming_exercises.add(programming_exercise)

        # Add learning outcomes
        learning_outcome_slugs = self.lesson_structure['learning-outcomes']
        for learning_outcome_slug in learning_outcome_slugs:
            learning_outcome = LearningOutcome.objects.get(
                slug=learning_outcome_slug
            )
            lesson.learning_outcomes.add(learning_outcome)

        # Add curriculum areas
        curriculum_area_slugs = self.lesson_structure['curriculum-areas']
        for curriculum_area_slug in curriculum_area_slugs:
            curriculum_area = CurriculumArea.objects.get(
                slug=curriculum_area_slug
            )
            lesson.curriculum_areas.add(curriculum_area)

        # Add classroom resources
        if 'resources-classroom' in self.lesson_structure:
            for resource in self.lesson_structure['resources-classroom']:
                (object, created) = ClassroomResource.objects.get_or_create(
                    text=resource
                )
                lesson.classroom_resources.add(object)

        # Add generated resources
        if 'resources-generated' in self.lesson_structure:
            for resource_data in self.lesson_structure['resources-generated']:
                slug = resource_data['slug']
                resource = Resource.objects.get(slug=slug)
                relationship = ConnectedGeneratedResource(
                    resource=resource,
                    lesson=lesson,
                    description=resource_data['description']
                )
                relationship.save()

        self.log('Added Lesson: {}'.format(lesson.__str__()), 2)
