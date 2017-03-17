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
        """The function called when the loadtopics command is given

        Loads content into database.
        """
        # Get structure and content files
        base_loader = BaseLoader()
        BASE_PATH = 'topics/content/en/'

        structure_file = base_loader.load_yaml_file(os.path.join(BASE_PATH, 'structure.yaml'))
        difficulty_file = structure_file['programming-exercises-structure']
        learning_outcomes_file = structure_file['learning-outcomes']
        curriculum_areas_file = structure_file['curriculum-areas']

        # Load content into db
        LearningOutcomesLoader(
            learning_outcomes_file,
            BASE_PATH
        ).load()

        CurriculumAreasLoader(
            curriculum_areas_file,
            BASE_PATH
        ).load()

        ProgrammingExercisesStructureLoader(
            difficulty_file,
            BASE_PATH
        ).load()

        for topic_structure_file in structure_file['topic-structure-files']:
            TopicLoader(
                topic_structure_file,
                BASE_PATH
            ).load()
