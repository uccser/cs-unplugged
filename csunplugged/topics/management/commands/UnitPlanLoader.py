from utils.BaseLoader import BaseLoader
from .LessonsLoader import LessonsLoader


class UnitPlanLoader(BaseLoader):
    """Loader for unit plans"""

    def __init__(self, load_log, structure_file, topic):
        """Initiates the loader for unit plans

        Args:
            structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(load_log)
        self.structure_file = structure_file
        self.topic = topic

    def load(self):
        """load the content for unit plans"""
        unit_plan_structure = self.load_yaml_file(self.BASE_PATH.format(self.structure_file))
        md_file = unit_plan_structure['md-file']
        unit_plan_content = self.convert_md_file(self.BASE_PATH.format(md_file))

        unit_plan = self.topic.topic_unit_plans.create(
            slug=unit_plan_structure['slug'],
            name=unit_plan_content.title,
            content=unit_plan_content.html_string,
        )
        unit_plan.save()

        self.log('Added Unit Plan: {}'.format(unit_plan.name), 1)

        lessons_structure = unit_plan_structure['lessons']
        LessonsLoader(self.load_log, lessons_structure, self.topic,
                      unit_plan).load()
