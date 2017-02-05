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
        for topic_data in structure['topics']:
            topic_file = open(os.path.join(self.BASE_PATH, topic_data['md-file']), encoding='UTF-8')
            raw_content = topic_file.read()
            topic_content = self.converter.run(raw_content)
            topic = Topic(
                slug=topic_data['slug'],
                # TODO: Set name from coverted content
                name=topic_content.heading,
                content=topic_content.html_string,
                icon=topic_data['icon']
            )
            topic.save()
            self.load_log.append('Added Topic: {}'.format(topic.name))
            self.load_follow_up_activities(topic_data['follow-up-activities'], topic)
        self.print_load_log()

    def load_follow_up_activities(self, follow_up_activities_structure, topic):
        if follow_up_activities_structure:
            structure = yaml.load(open(os.path.join(self.BASE_PATH, follow_up_activities_structure), encoding='UTF-8').read())

            for activity_data in structure:
                activity_file = open(os.path.join(self.BASE_PATH, activity_data['md-file']), encoding='UTF-8')
                raw_content = activity_file.read()
                activity_content = self.converter.run(raw_content)
                activity = topic.topic_follow_up_activities.create(
                    slug=activity_data['slug'],
                    # TODO: Set name from coverted content
                    name=activity_content.heading,
                    content=activity_content.html_string,
                )
                activity.save()
                for link in activity_data['curriculum-links']:
                     (object, created) = CurriculumLink.objects.get_or_create(
                        name=link
                     )
                     activity.curriculum_links.add(object)
                self.load_log.append('Added Activity: {}'.format(activity.name))
