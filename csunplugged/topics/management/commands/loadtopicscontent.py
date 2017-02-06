from django.core.management.base import BaseCommand, CommandError
from topics.models import Topic, CurriculumLink
from django.utils.text import slugify
from django.db import transaction
import yaml
import os
import os.path
import sys
import markdown
import mdx_math
from kordac import Kordac

class Command(BaseCommand):
    help = 'Converts Markdown files listed in structure file and stores'

    def handle(self, *args, **options):
        """The function called when the loadtopicscontent command is given"""

        # This path should be calculated, hardcoded for prototype
        self.BASE_PATH = 'topics/content/en/'
        self.converter = Kordac()
        language_structure = self.read_language_structure()
        self.load_topics(language_structure)


    def read_language_structure(self):
        structure_file = open(os.path.join(self.BASE_PATH, 'structure.yml'), encoding='UTF-8')
        return yaml.load(structure_file.read())

    def print_load_log(self):
        for log in self.load_log:
            self.stdout.write(log)

    @transaction.atomic
    def load_topics(self, structure):
        self.load_log = []
        for topic_structure in structure['topics']:
            topic_data = self.convert_md_file(topic_structure['md-file'])

            other_resources_file = topic_structure['other-resources-md-file']
            if other_resources_file:
                other_resources_data = self.convert_md_file(other_resources_file)
                other_resources_html = other_resources_data.html
            else:
                other_resources_html = ''

            topic = Topic(
                slug=topic_structure['slug'],
                name=topic_data.heading,
                content=topic_data.html,
                other_resources=other_resources_html,
                icon=topic_structure['icon']
            )
            topic.save()
            self.load_log.append('Added Topic: {}'.format(topic.name))

            self.stdout.write(topic_structure['follow-up-activities'])
            if topic_structure['follow-up-activities']:
                self.load_follow_up_activities(topic_structure['follow-up-activities'], topic)
        self.print_load_log()

    def convert_md_file(self, file_path):
        """Returns the Kordac object for a given Markdown file"""
        content = open(os.path.join(self.BASE_PATH, file_path), encoding='UTF-8').read()
        return self.converter.run(content)


    def load_follow_up_activities(self, follow_up_activities_structure, topic):
        if follow_up_activities_structure:
            structure = yaml.load(open(os.path.join(self.BASE_PATH, follow_up_activities_structure), encoding='UTF-8').read())

            for activity_data in structure:
                activity_file = open(os.path.join(self.BASE_PATH, activity_data['md-file']), encoding='UTF-8')
                raw_content = activity_file.read()
                activity_content = self.converter.run(raw_content)
                activity = topic.topic_follow_up_activities.create(
                    slug=activity_data['slug'],
                    name=activity_content.heading,
                    content=activity_content.html,
                )
                activity.save()
                for link in activity_data['curriculum-links']:
                     (object, created) = CurriculumLink.objects.get_or_create(
                        name=link
                     )
                     activity.curriculum_links.add(object)
                self.load_log.append('Added Activity: {}'.format(activity.name))
