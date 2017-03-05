from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.management.commands.FollowUpActivitiesLoader import FollowUpActivitiesLoader
from topics.management.commands.ProgrammingExercisesLoader import ProgrammingExercisesLoader
from topics.management.commands.UnitPlanLoader import UnitPlanLoader
from topics.models import Topic


class TopicsLoader(BaseLoader):
    """Loader for the topics content"""

    def __init__(self, structure):
        """Initiates the learning outcomes loader

        Args:
            structure: dictionary containing list of topics, each with a dictionary of attributes
        """
        super().__init__()
        self.structure = structure

    @transaction.atomic
    def load(self):
        """load the content for topics"""
        for topic_structure in self.structure['topics']:
            topic_data = self.convert_md_file(topic_structure['md-file'])

            # If other resources are given, convert to html
            other_resources_file = topic_structure['other-resources-md-file']
            if other_resources_file:
                other_resources_data = self.convert_md_file(other_resources_file)
                other_resources_html = other_resources_data.html_string
            else:
                other_resources_html = ''

            # Create topic objects and save to the db
            topic = Topic(
                slug=topic_structure['slug'],
                name=topic_data.title,
                content=topic_data.html_string,
                other_resources=other_resources_html,
                icon=topic_structure['icon']
            )
            topic.save()
            self.load_log.append(('\nAdded Topic: {}'.format(topic.name), 0))

            # Load unit plans
            for unit_plan_structure_file in topic_structure['unit-plans']:
                UnitPlanLoader(self.load_log, unit_plan_structure_file, topic).load()

            # Load programming exercises (if there are any)
            if topic_structure['programming-exercises']:
                ProgrammingExercisesLoader(self.load_log, topic_structure['programming-exercises'], topic).load()

            # Load follow up activities (if there are any)
            if topic_structure['follow-up-activities']:
                FollowUpActivitiesLoader(self.load_log, topic_structure['follow-up-activities'], topic).load()

        # Print log output
        self.print_load_log()
