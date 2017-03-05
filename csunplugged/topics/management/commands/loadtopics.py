from django.core.management.base import BaseCommand
from .BaseLoader import BaseLoader
from .LearningOutcomesLoader import LearningOutcomesLoader
from .TopicsLoader import TopicsLoader
from .ProgrammingExercisesDifficultiesLoader import ProgrammingExercisesDifficultiesLoader  # noqa: E501


class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        """The function called when the loadtopics command is given

        Loads content into database.
        """
        # Get structure and content files
        base_loader = BaseLoader()
        structure_file = base_loader.language_structure
        difficulty_file = structure_file['programming-exercises-difficulty']
        learning_outcomes_file = structure_file['learning-outcomes']

        # Load content into db
        LearningOutcomesLoader(learning_outcomes_file).load()
        ProgrammingExercisesDifficultiesLoader(difficulty_file).load()
        TopicsLoader(structure_file).load()
