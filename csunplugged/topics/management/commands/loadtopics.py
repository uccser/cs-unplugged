from django.core.management.base import BaseCommand
from utils.BaseLoader import BaseLoader
from ._LearningOutcomesLoader import LearningOutcomesLoader
from ._TopicsLoader import TopicsLoader
from ._ProgrammingExercisesStructureLoader import ProgrammingExercisesStructureLoader


class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        """The function called when the loadtopics command is given

        Loads content into database.
        """
        # Get structure and content files
        base_loader = BaseLoader()
        BASE_PATH = 'topics/content/en/{}'

        structure_file = base_loader.load_yaml_file(BASE_PATH.format('structure.yaml'))
        difficulty_file = structure_file['programming-exercises-structure']
        learning_outcomes_file = structure_file['learning-outcomes']

        # Load content into db
        LearningOutcomesLoader(
            learning_outcomes_file,
            BASE_PATH
        ).load()

        ProgrammingExercisesStructureLoader(
            difficulty_file,
            BASE_PATH
        ).load()

        TopicsLoader(
            structure_file,
            BASE_PATH
        ).load()
