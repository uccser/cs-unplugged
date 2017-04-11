import os.path

from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import CurriculumArea


class CurriculumAreasLoader(BaseLoader):
    '''Loader for curriculum area content'''

    def __init__(self, curriculum_areas_file, BASE_PATH):
        '''Initiates the curriculum area loader

        Args:
            curriculum_areas_file: file path (string)
        '''
        super().__init__(BASE_PATH)
        self.curriculum_areas_file = curriculum_areas_file
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(curriculum_areas_file)[0])

    @transaction.atomic
    def load(self):
        '''Load the content for curriculum areas
        
        Raises:
            MissingRequiredFieldError:
        '''
        curriculum_areas_structure = self.load_yaml_file(
            os.path.join(
                self.BASE_PATH,
                self.curriculum_areas_file
            )
        )

        for (curriculum_area_slug, curriculum_area_data) in curriculum_areas_structure.items():

            try:
                curriculum_area_name = curriculum_area_data['name']
            except:
                raise MissingRequiredFieldError()

            if curriculum_area_name is None:
                raise MissingRequiredFieldError()

            # Create area objects and save to database
            new_area = CurriculumArea(
                slug=curriculum_area_slug,
                name=curriculum_area_name,
            )
            new_area.save()

            self.log('Added Curriculum Area: {}'.format(new_area.__str__()))

            # Create children curriculum areas with reference to parent
            if 'children' in curriculum_area_data:
                for (child_slug, child_data) in curriculum_area_data['children'].items():
                    try:
                        child_name = child_data['name']
                    except:
                        raise MissingRequiredFieldError()

                    if child_name is None:
                        raise MissingRequiredFieldError()

                    new_child = CurriculumArea(
                        slug=child_slug,
                        name=child_name,
                        parent=new_area
                    )
                    new_child.save()

                    self.log('Added Child Curriculum Area: {}'.format(new_child.__str__()), 1)

            

        # Print log output
        self.print_load_log()
