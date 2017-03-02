from django.core.management.base import BaseCommand
from topics.management.commands.BaseLoader import BaseLoader
from topics.management.commands.LearningOutcomesLoader import LearningOutcomesLoader
from topics.management.commands.TopicsLoader import TopicsLoader

class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        """The function called when the loadtopics command is given

        Loads content into database.
        """
        # Get structure and content files
        base_loader = BaseLoader()
        structure_file = base_loader.language_structure
        learning_outcomes_file = structure_file['learning-outcomes']

        # Load content into db
        LearningOutcomesLoader(learning_outcomes_file).load()
        TopicsLoader(structure_file).load()

