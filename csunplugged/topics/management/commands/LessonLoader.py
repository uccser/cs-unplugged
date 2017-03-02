from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.models import Age, LearningOutcome, CurriculumLink, ClassroomResource, Resource, ConnectedGeneratedResource

class LessonLoader(BaseLoader):

    def __init__(self, lesson_structure, topic, unit_plan):
        super().__init__()
        self.lesson_structure = lesson_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
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
