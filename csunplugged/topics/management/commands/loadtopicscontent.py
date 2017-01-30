from django.core.management.base import BaseCommand, CommandError
from topics.models import Topic
from django.utils.text import slugify
import json
import os
import os.path
import sys
import markdown
import mdx_math

class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        """The function called when the loadtopicscontent command is given"""

        # This path should be calculated, hardcoded for prototype
        self.BASE_PATH = 'topics/content/en/'

        structure = self.read_structure()
        self.process_topics(structure)


    def read_structure(self):
        structure_file = open(os.path.join(self.BASE_PATH, 'structure.json'), encoding='UTF-8')
        structure_file_contents = structure_file.read()
        return json.loads(structure_file_contents)

    def process_topics(self, structure):
        # Would import Kordac as required package, rather than submodule in final release
        django_wd = os.getcwd()
        os.chdir(os.path.join(self.BASE_PATH, '../kordac/'))
        sys.path.insert(0, os.getcwd())
        import Kordac
        kordac_ext = Kordac.Kordac()
        converter = markdown.Markdown(extensions=[
            'markdown.extensions.fenced_code',
            'markdown.extensions.codehilite',
            'markdown.extensions.sane_lists',
            mdx_math.MathExtension(enable_dollar_delimiter=True),
            kordac_ext])
        os.chdir(django_wd)

        for topic in structure['topics']:
            topic_file = open(os.path.join(self.BASE_PATH, topic['file']), encoding='UTF-8')
            raw_content = topic_file.read()
            html = converter.convert(raw_content)
            self.save_topic(topic, html)

    def save_topic(self, topic, html):
        topic = Topic(name=topic['name'],
            description=html,
            slug=slugify(topic['name']))
        topic.save()
