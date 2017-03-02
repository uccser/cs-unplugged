import yaml
import os.path
import mdx_math
import abc
import sys
from kordac import Kordac


class BaseLoader():
    """Base loader class for individual loaders"""
    load_log = []

    def __init__(self):
        self.BASE_PATH = 'topics/content/en/' # TODO: Hardcoded for prototype
        self.language_structure = self.load_yaml_file('structure.yaml')
        self.setup_md_to_html_converter()

    def setup_md_to_html_converter(self):
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

    def print_load_log(self):
        """Output log messages from loader to console"""
        for (log, indent) in self.load_log:
            sys.stdout.write('{indent}{text}\n'.format(indent='  '*indent,text=log))
        self.load_log = []

    def convert_md_file(self, file_path):
        """Returns the Kordac object for a given Markdown file

        Args:
            file_path: location of md file to convert

        Returns:
            Kordac result object
        """
        content = open(os.path.join(self.BASE_PATH, file_path), encoding='UTF-8').read()
        return self.converter.convert(content)

    def load_yaml_file(self, file_path):
        """Loads and reads yaml file

        Args:
            file_path: location of yaml file to read

        Returns:
             Either list or string, depending on structure of given yaml file
        """
        return yaml.load(open(os.path.join(self.BASE_PATH, file_path), encoding='UTF-8').read())


    @abc.abstractmethod
    def load(self):
        raise NotImplementedError('subclass does not implement this method')


