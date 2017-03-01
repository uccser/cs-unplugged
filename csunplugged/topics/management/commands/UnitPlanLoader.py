import yaml
import os
from topics.management.commands.BaseLoader import BaseLoader
from topics.management.commands.LessonLoader import LessonLoader

class UnitPlanLoader(BaseLoader):

    def __init__(self, unit_plan_structure_file, topic):
        super().__init__()
        self.unit_plan_structure_file = unit_plan_structure_file
        self.topic = topic

    def load(self):
        unit_plan_structure = yaml.load(open(os.path.join(self.BASE_PATH, self.unit_plan_structure_file), encoding='UTF-8').read())
        unit_plan_content = BaseLoader.convert_md_file(unit_plan_structure['md-file'])

        unit_plan = self.topic.topic_unit_plans.create(
            slug=unit_plan_structure['slug'],
            name=unit_plan_content.title,
            content=unit_plan_content.html_string,
        )
        unit_plan.save()
        BaseLoader.load_log.append(('Added Unit Plan: {}'.format(unit_plan.name), 1))

        lessons_structure = unit_plan_structure['lessons']
        LessonLoader.load(lessons_structure, self.topic, unit_plan)
