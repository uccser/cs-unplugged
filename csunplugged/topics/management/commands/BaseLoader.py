from django.core.management.base import BaseCommand
import yaml
import os # NTS maybe don't need this...
import os.path
import mdx_math
import abc
from kordac import Kordac


# TODO: Should create generic functions for loading YAML and reading file
class BaseLoader(BaseCommand):

    def __init__(self):
        self.BASE_PATH = 'topics/content/en/' # TODO: Hardcoded for prototype
        self.language_structure = self.read_language_structure()
        self.setup_converter()
        self.load_log = []

    def setup_converter(self):
        """Create Kordac converter with custom processors, html templates,
        and extensions.
        """
        templates = dict()
        extensions = [
            'markdown.extensions.fenced_code',
            'markdown.extensions.codehilite',
            'markdown.extensions.sane_lists',
            mdx_math.MathExtension(enable_dollar_delimiter=True)
        ]
        self.converter = Kordac(html_templates=templates, extensions=extensions)
        custom_processors = self.converter.processor_defaults()
        custom_processors.add('remove-title')
        self.converter.update_processors(custom_processors)

    def read_language_structure(self):
        structure_file = open(os.path.join(self.BASE_PATH, 'structure.yaml'), encoding='UTF-8')
        return yaml.load(structure_file.read())

    def print_load_log(self):
        for (log, indent) in self.load_log:
            self.stdout.write('{indent}{text}'.format(indent='  '*indent,text=log))
        self.stdout.write('\n')
        self.load_log = []

    def convert_md_file(self, file_path):
        """Returns the Kordac object for a given Markdown file"""
        content = open(os.path.join(self.BASE_PATH, file_path), encoding='UTF-8').read()
        return self.converter.convert(content)

    @abc.abstractmethod
    def load(self):
        pass
        # raise <something>


