from django.core.management.base import BaseCommand
from topics.management.commands.BaseLoader import BaseLoader
from topics.management.commands.LearningOutcomesLoader import LearningOutcomesLoader
from topics.management.commands.TopicsLoader import TopicsLoader

class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        """The function called when the loadtopics command is given"""
        base_loader = BaseLoader()
        LearningOutcomesLoader(base_loader.language_structure['learning-outcomes']).load()
        TopicsLoader(base_loader.language_structure).load()

