"""Custom loader for loading curriculum integrations."""

import os.path
from utils.BaseLoader import BaseLoader
from topics.models import CurriculumArea, Lesson


class CurriculumIntegrationsLoader(BaseLoader):
    """Custom loader for loading curriculum integrations."""

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        """Create the loader for loading curriculum integrations.

        Args:
            load_log: List of log messages (list).
            structure_file: File path for structure YAML file (string).
            topic: Object of related topic model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH, load_log)
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])
        self.topic = topic

    def load(self):
        """Load the content for curriculum integrations."""
        if self.structure_file:
            structure = self.load_yaml_file(self.structure_file)

            for integration_slug, integration_data in structure.items():
                md_file = integration_data['md-file']
                integration_content = self.convert_md_file(os.path.join(self.BASE_PATH, md_file))

                integration = self.topic.curriculum_integrations.create(
                    slug=integration_slug,
                    number=integration_data['number'],
                    name=integration_content.title,
                    content=integration_content.html_string,
                )
                integration.save()

                # Add curriculum areas
                curriculum_area_slugs = integration_data['curriculum-areas']
                for curriculum_area_slug in curriculum_area_slugs:
                    curriculum_area = CurriculumArea.objects.get(
                        slug=curriculum_area_slug
                    )
                    integration.curriculum_areas.add(curriculum_area)

                # Add prerequisite lessons
                if 'prerequisite-lessons' in integration_data:
                    prerequisite_lessons_slugs = integration_data['prerequisite-lessons']
                    for prerequisite_lessons_slug in prerequisite_lessons_slugs:
                        (unit_plan_slug, lesson_slug) = prerequisite_lessons_slug.split('/')
                        lesson = Lesson.objects.get(
                            slug=lesson_slug,
                            unit_plan__slug=unit_plan_slug,
                            topic__slug=self.topic.slug
                        )
                        integration.prerequisite_lessons.add(lesson)

                self.log('Added Curriculum Integration: {}'.format(integration.name), 1)
