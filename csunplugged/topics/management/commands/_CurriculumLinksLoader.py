import os.path
from django.db import transaction
from utils.BaseLoader import BaseLoader
from topics.models import CurriculumLink


class CurriculumLinksLoader(BaseLoader):
    """Loader for curriculum link content"""

    def __init__(self, curriculum_links_file, BASE_PATH):
        """Initiates the curriculum links loader

        Args:
            curriculum_links_file: file path (string)
        """
        super().__init__(BASE_PATH)
        self.curriculum_links_file = curriculum_links_file
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(curriculum_links_file)[0])

    @transaction.atomic
    def load(self):
        """load the content for curriculum links"""
        curriculum_links_structure = self.load_yaml_file(os.path.join(self.BASE_PATH, self.curriculum_links_file))
        for (curriculum_link_slug, curriculum_link_data) in curriculum_links_structure.items():
            # Create link objects and save to database
            link = CurriculumLink(
                slug=curriculum_link_slug,
                name=curriculum_link_data['name']
            )
            link.save()
            self.log('Added Curriculum Link: {}'.format(link.__str__()))

        # Print log output
        self.print_load_log()
