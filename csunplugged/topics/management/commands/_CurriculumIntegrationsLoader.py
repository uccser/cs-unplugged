import os.path
from utils.BaseLoader import BaseLoader
from topics.models import CurriculumLink


class CurriculumIntegrationsLoader(BaseLoader):
    """Loader for curriculum integrations"""

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        """Initiates the loader for curriculum integrations

        Args:
            structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(BASE_PATH, load_log)
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])
        self.topic = topic

    def load(self):
        """Load the content for curriculum integrations"""
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

                # Add curriculum links
                curriculum_link_slugs = integration_data['curriculum-links']
                for curriculum_link_slug in curriculum_link_slugs:
                    curriculum_link = CurriculumLink.objects.get(
                        slug=curriculum_link_slug
                    )
                    integration.curriculum_links.add(curriculum_link)

                self.log('Added Curriculum Integration: {}'.format(integration.name), 1)
