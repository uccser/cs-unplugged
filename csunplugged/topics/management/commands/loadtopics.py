from django.core.management.base import BaseCommand
import yaml
import os # NTS maybe don't need this...
import os.path
import mdx_math
import abc
from kordac import Kordac
from topics.management.commands.BaseLoader import BaseLoader
from topics.management.commands.LearningOutcomesLoader import LearningOutcomesLoader
from topics.management.commands.TopicsLoader import TopicsLoader

class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        """The function called when the loadtopics command is given"""
        thing = BaseLoader()
        LearningOutcomesLoader(thing.language_structure['learning-outcomes']).load()
        TopicsLoader(thing.language_structure).load()

