from utils.BaseLoader import BaseLoader
from topics.models import CurriculumLink


class FollowUpActivitiesLoader(BaseLoader):
    """Loader for follow up activites"""

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        """Initiates the loader for follow up activites

        Args:
            structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(BASE_PATH, load_log)
        self.structure_file = structure_file
        self.topic = topic

    def load(self):
        """Load the content for follow up activities"""
        if self.structure_file:
            structure = self.load_yaml_file(self.BASE_PATH.format(self.structure_file))

            for activity_data in structure:
                md_file = activity_data['md-file']
                activity_content = self.convert_md_file(self.BASE_PATH.format(md_file))

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

                self.log('Added Activity: {}'.format(activity.name), 1)
