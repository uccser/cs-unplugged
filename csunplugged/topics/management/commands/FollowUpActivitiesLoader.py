from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.models import CurriculumLink

class FollowUpActivitiesLoader(BaseLoader):

    def __init__(self, follow_up_activities_structure, topic):
        super().__init__()
        self.follow_up_activities_structure = follow_up_activities_structure
        self.topic = topic

    def load(self):
        if self.follow_up_activities_structure:
            structure = self.load_yaml_file(self.follow_up_activities_structure)

            for activity_data in structure:
                activity_content = self.convert_md_file(activity_data['md-file'])
                activity = self.topic.topic_follow_up_activities.create(
                    slug=activity_data['slug'],
                    name=activity_content.title,
                    content=activity_content.html_string,
                )
                activity.save()
                for link in activity_data['curriculum-links']:
                    (object, created) = CurriculumLink.objects.get_or_create(
                        name=link
                    )
                    activity.curriculum_links.add(object)
                self.load_log.append(('Added Activity: {}'.format(activity.name), 1))
