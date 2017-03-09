import yaml
import os.path
import mdx_math
import abc
import sys
from kordac import Kordac


class BaseLoader():
    """Base loader class for individual loaders"""

    def __init__(self, load_log=[]):
        if load_log:
            self.load_log = load_log
        else:
            self.load_log = list(load_log)
        self.BASE_PATH = 'topics/content/en/'  # TODO: Hardcoded for prototype
        self.language_structure = self.load_yaml_file('structure.yaml')
        self.setup_md_to_html_converter()

    def setup_md_to_html_converter(self):
        """Create Kordac converter with custom processors, html templates,
        and extensions.
        """
        templates = dict()
        templates['scratch'] = '<div><object data="{% autoescape false -%}{{ "{% get_static_prefix %}" }}img/scratch-blocks-{{ hash }}.svg{%- endautoescape %}" type="image/svg+xml" /></div>'  # noqa: E501 Fixed in #77
        templates['iframe'] = '<iframe allowtransparency="true" width="485" height="402" src="{{ link }}" frameborder="0" allowfullscreen="true"></iframe>'  # noqa: E501 Fixed in #77
        templates['heading'] = '<{{ heading_type }} id="{{ title_slug }}">{{ title }}</{{ heading_type }}>'  # noqa: E501 Fixed in #77
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

    def convert_md_file(self, file_path):
        """Returns the Kordac object for a given Markdown file

        Args:
            file_path: location of md file to convert

        Returns:
            Kordac result object
        """
        md_file_path = os.path.join(self.BASE_PATH, file_path)
        content = open(md_file_path, encoding='UTF-8').read()
        result = self.converter.convert(content)
        # Write Scratch data for image rendering by Gulp script
        if 'scratch_images' in result.required_files:
            FILEPATH_TEMPLATE = 'temp/scratch-blocks-{hash}.txt'
            if not os.path.exists('temp'):
                os.makedirs('temp')
            for scratch_image in result.required_files['scratch_images']:
                filepath = FILEPATH_TEMPLATE.format(hash=scratch_image.hash)
                if not os.path.isfile(filepath):
                    with open(filepath, 'w') as scratch_temp_file:
                        scratch_temp_file.write(scratch_image.text)
        return result

    def log(self, log_message, indent_amount=0):
        """Adds the log message to the load log with the specified indent"""
        self.load_log.append((log_message, indent_amount))

    def print_load_log(self):
        """Output log messages from loader to console"""
        for (log, indent_amount) in self.load_log:
            indent = '  ' * indent_amount
            sys.stdout.write('{indent}{text}\n'.format(indent=indent, text=log))
        sys.stdout.write('\n')
        self.load_log = []

    def load_yaml_file(self, file_path):
        """Loads and reads yaml file

        Args:
            file_path: location of yaml file to read

        Returns:
             Either list or string, depending on structure of given yaml file
        """
        yaml_file_path = os.path.join(self.BASE_PATH, file_path)
        yaml_file = open(yaml_file_path, encoding='UTF-8').read()
        return yaml.load(yaml_file)

    @abc.abstractmethod
    def load(self):
        raise NotImplementedError('subclass does not implement this method')
