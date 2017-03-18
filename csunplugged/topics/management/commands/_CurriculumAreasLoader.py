import os.path
from django.db import transaction
from utils.BaseLoader import BaseLoader
from topics.models import CurriculumArea


class CurriculumAreasLoader(BaseLoader):
    """Loader for curriculum area content"""

    def __init__(self, curriculum_areas_file, BASE_PATH):
        """Initiates the curriculum area loader

        Args:
            curriculum_areas_file: file path (string)
        """
        super().__init__(BASE_PATH)
        self.curriculum_areas_file = curriculum_areas_file
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(curriculum_areas_file)[0])

    @transaction.atomic
    def load(self):
        """load the content for curriculum areas"""
        curriculum_areas_structure = self.load_yaml_file(os.path.join(self.BASE_PATH, self.curriculum_areas_file))
        for (curriculum_area_slug, curriculum_area_data) in curriculum_areas_structure.items():
            # Create area objects and save to database
            area = CurriculumArea(
                slug=curriculum_area_slug,
                name=curriculum_area_data['name']
            )
            area.save()
            self.log('Added Curriculum Area: {}'.format(area.__str__()))

        # Print log output
        self.print_load_log()
