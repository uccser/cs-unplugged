from django.core.management.base import BaseCommand
from utils.BaseLoader import BaseLoader
from .LearningOutcomesLoader import LearningOutcomesLoader
from .TopicsLoader import TopicsLoader
from .ProgrammingExercisesStructureLoader import ProgrammingExercisesStructureLoader


class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        """The function called when the loadtopics command is given

        Loads content into database.
        """
        # Get structure and content files
        base_loader = BaseLoader()

        structure_file = base_loader.load_yaml_file(base_loader.BASE_PATH.format('structure.yaml'))
        difficulty_file = structure_file['programming-exercises-structure']
        learning_outcomes_file = structure_file['learning-outcomes']

        # Load content into db
        LearningOutcomesLoader(learning_outcomes_file).load()
        ProgrammingExercisesStructureLoader(difficulty_file).load()
        TopicsLoader(structure_file).load()
