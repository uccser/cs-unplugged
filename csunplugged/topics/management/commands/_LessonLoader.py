import os.path
from utils.BaseLoader import BaseLoader
from topics.models import (
    LearningOutcome,
    CurriculumLink,
    ClassroomResource,
    Resource,
    ConnectedGeneratedResource,
)


class LessonLoader(BaseLoader):
    """Loader for a single lesson"""

    def __init__(self, load_log, lesson_slug, lesson_structure, topic, unit_plan, BASE_PATH):
        """Initiates the loader for a single lesson

        Args:
            lesson_slug: string of the URL slug for a lesson
            lesson_structure: dictionary containing attributes for a lesson
            topic: Topic model object
            unit_plan: UnitPlan model object
        """
        super().__init__(BASE_PATH, load_log)
        self.lesson_slug = lesson_slug
        self.lesson_structure = lesson_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """load the content for a single lesson"""
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

        # Add learning outcomes
        learning_outcome_slugs = self.lesson_structure['learning-outcomes']
        for learning_outcome_slug in learning_outcome_slugs:
            learning_outcome = LearningOutcome.objects.get(
                slug=learning_outcome_slug
            )
            lesson.learning_outcomes.add(learning_outcome)

        # Add curriculum links
        curriculum_link_slugs = self.lesson_structure['curriculum-links']
        for curriculum_link_slug in curriculum_link_slugs:
            curriculum_link = CurriculumLink.objects.get(
                slug=curriculum_link_slug
            )
            lesson.curriculum_links.add(curriculum_link)

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
