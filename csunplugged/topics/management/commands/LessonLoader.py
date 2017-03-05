from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.models import Age, LearningOutcome, CurriculumLink, ClassroomResource, Resource, ConnectedGeneratedResource

class LessonLoader(BaseLoader):
    """Loader for a single lesson"""

    def __init__(self, load_log, lesson_structure, topic, unit_plan):
        """Initiates the loader for a single lesson

        Args:
            lesson_structure: dictionary containing attributes for a lesson
            topic: Topic model object
            unit_plan: UnitPlan model object
        """
        super().__init__(load_log)
        self.lesson_structure = lesson_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """load the content for a single lesson"""
        lesson_content = self.convert_md_file(self.lesson_structure['md-file'])
        lesson = self.topic.topic_lessons.create(
            unit_plan=self.unit_plan,
            slug=self.lesson_structure['slug'],
            name=lesson_content.title,
            number=self.lesson_structure['lesson-number'],
            content=lesson_content.html_string,
        )
        lesson.save()

        # Add ages
        ages = self.lesson_structure['ages'].split(',')
        for age in ages:
            (object, created) = Age.objects.get_or_create(
                age=age
            )
            lesson.ages.add(object)

        # Add learning outcomes
        for learning_outcome_slug in self.lesson_structure['learning-outcomes']:
            learning_outcome = LearningOutcome.objects.get(
                slug=learning_outcome_slug
            )
            lesson.learning_outcomes.add(learning_outcome)

        # Add curriculum links
        for link in self.lesson_structure['curriculum-links']:
            (object, created) = CurriculumLink.objects.get_or_create(
                name=link
            )
            lesson.curriculum_links.add(object)

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
                resource = Resource.objects.get(slug=resource_data['resource-slug'])
                relationship = ConnectedGeneratedResource(
                    resource=resource,
                    lesson=lesson,
                    description=resource_data['description']
                )
                relationship.save()

        self.load_log.append(('Added Lesson: {}'.format(lesson.__str__()), 2))
