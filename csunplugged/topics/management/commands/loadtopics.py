import os.path
from django.core.management.base import BaseCommand
from utils.BaseLoader import BaseLoader
from ._LearningOutcomesLoader import LearningOutcomesLoader
from ._CurriculumAreasLoader import CurriculumAreasLoader
from ._TopicLoader import TopicLoader
from ._ProgrammingExercisesStructureLoader import ProgrammingExercisesStructureLoader


class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        '''The function called when the loadtopics command is given

        Loads content into database.
        '''
        # Get structure and content files
        base_loader = BaseLoader()
        BASE_PATH = 'topics/content/en/'

        structure_file = base_loader.load_yaml_file(
            os.path.join(
                BASE_PATH,
                'structure.yaml'
            )
        )

        # Load content from misc structure files into db
        if 'misc-structure-files' in structure_file:
            misc_structure_files = structure_file['misc-structure-files']
            for item in misc_structure_files:
                file = '{}.yaml'.format(item)

                if item == 'learning-outcomes':
                    LearningOutcomesLoader(
                        file,
                        BASE_PATH
                    ).load()

                if item == 'curriculum-areas':
                    CurriculumAreasLoader(
                        file,
                        BASE_PATH
                    ).load()
        
                if item == 'programming-exercises-structure':
                    ProgrammingExercisesStructureLoader(
                        file,
                        BASE_PATH
                    ).load()
        
        for topic in structure_file['topics']:
            topic_structure_file = '{0}/{0}.yaml'.format(topic)
            TopicLoader(
                topic_structure_file,
                BASE_PATH
            ).load()
