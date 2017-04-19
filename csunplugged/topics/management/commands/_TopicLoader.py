import os.path
from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.check_required_files import find_image_files

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from ._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader
from ._ProgrammingExercisesLoader import ProgrammingExercisesLoader
from ._UnitPlanLoader import UnitPlanLoader

from topics.models import Topic


class TopicLoader(BaseLoader):
    '''Loader for the topics content'''

    def __init__(self, structure_file_path, BASE_PATH):
        '''Initiates the topic loader

        Args:
            structure_file_path: file path (string)
            a dictionary of attributes.
        '''
        super().__init__(BASE_PATH)
        self.topic_slug = os.path.split(structure_file_path)[0]
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, self.topic_slug)

    @transaction.atomic
    def load(self):
        '''Load the content for a topic

        Raises:
            TopicHasNoUnitPlansError:
        '''
        
        topic_structure = self.load_yaml_file(self.structure_file_path)
        
        unit_plans = topic_structure.get('unit-plans', None)
        if unit_plans is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ['unit-plans'],
                'Topic'
            )

        # Convert the content to HTML
        topic_content = self.convert_md_file(
            os.path.join(
                self.BASE_PATH,
                '{}.md'.format(self.topic_slug)
            ),
            self.structure_file_path
        )

        # If other resources are given, convert to HTML
        if 'other-resources' in topic_structure:
            topic_other_resources_file = topic_structure['other-resources']
            other_resources_content = self.convert_md_file(
                os.path.join(
                    self.BASE_PATH,
                    topic_other_resources_file
                ),
                self.structure_file_path
            )
            topic_other_resources_html = other_resources_content.html_string
        else:
            topic_other_resources_html = None

        # Check if icon is given
        if 'icon' in topic_structure:
            topic_icon = topic_structure['icon']
            find_image_files([topic_icon], self.structure_file_path)
        else:
            topic_icon = None

        # Create topic objects and save to the db
        topic = Topic(
            # slug=self.topic_slug,
            name=topic_content.title,
            content=topic_content.html_string,
            other_resources=topic_other_resources_html,
            icon=topic_icon
        )
        topic.save()

        self.log('Added Topic: {}'.format(topic.name))

        FILE_PATH_TEMPLATE = '{0}/{0}.yaml'
        
        if 'misc-structure-files' in topic_structure:
            misc_structure_file_paths = topic_structure['misc-structure-files']
         
        # Load programming exercises   
        if 'programming-exercises' in misc_structure_file_paths:
            ProgrammingExercisesLoader(
                self.load_log,
                FILE_PATH_TEMPLATE.format('programming-exercises'),
                topic,
                self.BASE_PATH
            ).load()

        # Load unit plans
        for unit_plan in unit_plans:
            UnitPlanLoader(
                self.load_log,
                FILE_PATH_TEMPLATE.format(unit_plan),
                topic,
                self.BASE_PATH
            ).load()

        # Load curriculum integrations
        if 'curriculum-integrations' in misc_structure_file_paths:
            CurriculumIntegrationsLoader(
                self.load_log,
                FILE_PATH_TEMPLATE.format('curriculum-integrations'),
                topic,
                self.BASE_PATH
            ).load()

        # Print log output
        self.print_load_log()
