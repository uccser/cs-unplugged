import yaml
import os
from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.management.commands.FollowUpActivitiesLoader import FollowUpActivitiesLoader
from topics.management.commands.ProgrammingExercisesLoader import ProgrammingExercisesLoader
from topics.management.commands.UnitPlanLoader import UnitPlanLoader


class TopicsLoader(BaseLoader):

    def __init__(self, structure):
        super().__init__()
        self.structure = structure

    @transaction.atomic
    def load(self):
        for topic_structure in self.structure['topics']:
            topic_data = BaseLoader.convert_md_file(topic_structure['md-file'])

            other_resources_file = topic_structure['other-resources-md-file']
            if other_resources_file:
                other_resources_data = BaseLoader.convert_md_file(other_resources_file)
                other_resources_html = other_resources_data.html_string
            else:
                other_resources_html = ''

            topic = Topic(
                slug=topic_structure['slug'],
                name=topic_data.title,
                content=topic_data.html_string,
                other_resources=other_resources_html,
                icon=topic_structure['icon']
            )
            topic.save()
            BaseLoader.load_log.append(('\nAdded Topic: {}'.format(topic.name), 0))

            # Load unit plans
            for unit_plan_structure_file in topic_structure['unit-plans']:
                UnitPlanLoader.load(unit_plan_structure_file, topic)

            # Load programming exercises
            if topic_structure['programming-exercises']:
                ProgrammingExercisesLoader.load(topic_structure['programming-exercises'], topic)

            # Load follow up activities
            if topic_structure['follow-up-activities']:
                FollowUpActivitiesLoader.load(topic_structure['follow-up-activities'], topic)

        # Print log output
        self.print_load_log()
