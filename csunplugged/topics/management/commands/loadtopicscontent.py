from django.core.management.base import BaseCommand, CommandError
from topics.models import Topic, CurriculumLink
from django.utils.text import slugify
import yaml
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

        # Would import Kordac as required package,
        # rather than submodule in final release.
        # Current functions have to switch to Kordac path
        # every time they need to run Kordac.
        self.django_wd = os.getcwd()
        os.chdir(os.path.join(self.BASE_PATH, '../kordac/'))
        sys.path.insert(0, os.getcwd())
        import Kordac
        self.kordac = Kordac.Kordac()
        os.chdir(self.django_wd)

        language_structure = self.read_language_structure()
        self.load_topics(language_structure)


    def read_language_structure(self):
        structure_file = open(os.path.join(self.BASE_PATH, 'structure.yml'), encoding='UTF-8')
        return yaml.load(structure_file.read())

    def load_topics(self, structure):
        for topic_data in structure['topics']:
            topic_file = open(os.path.join(self.BASE_PATH, topic_data['md-file']), encoding='UTF-8')
            raw_content = topic_file.read()
            os.chdir(os.path.join(self.BASE_PATH, '../kordac/'))
            topic_content = self.kordac.run(raw_content)
            os.chdir(self.django_wd)
            topic = Topic(
                slug=topic_data['slug'],
                # TODO: Set name from coverted content
                name=topic_data['slug'],
                content=topic_content.html_string,
                icon=topic_data['icon']
            )
            topic.save()
            self.stdout.write('Added Topic: {}'.format(topic.name))
            self.load_follow_up_activities(topic_data['follow-up-activities'], topic)

    def load_follow_up_activities(self, follow_up_activities_structure, topic):
        if follow_up_activities_structure:
            structure = yaml.load(open(os.path.join(self.BASE_PATH, follow_up_activities_structure), encoding='UTF-8').read())

            for activity_data in structure:
                activity_file = open(os.path.join(self.BASE_PATH, activity_data['md-file']), encoding='UTF-8')
                raw_content = activity_file.read()
                os.chdir(os.path.join(self.BASE_PATH, '../kordac/'))
                activity_content = self.kordac.run(raw_content)
                os.chdir(self.django_wd)
                activity = topic.topic_follow_up_activities.create(
                    slug=activity_data['slug'],
                    # TODO: Set name from coverted content
                    name=activity_data['slug'],
                    content=activity_content.html_string,
                )
                activity.save()
                for link in activity_data['curriculum-links']:
                     (object, created) = CurriculumLink.objects.get_or_create(
                        name=link
                     )
                     activity.curriculum_links.add(object)
                self.stdout.write('Added Activity: {}'.format(activity.name))
