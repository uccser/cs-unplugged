import os.path
from utils.BaseLoader import BaseLoader

from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.MarkdownFileMissingTitleError import MarkdownFileMissingTitleError
from utils.errors.UnitPlanHasNoLessonsError import UnitPlanHasNoLessonsError

from ._LessonsLoader import LessonsLoader


class UnitPlanLoader(BaseLoader):
    """Loader for unit plans"""

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        """Initiates the loader for unit plans

        Args:
            structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(BASE_PATH, load_log)
        self.unit_plan_name = os.path.split(structure_file)[0]
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, self.unit_plan_name)
        self.topic = topic

    def load(self):
        """Load the content for unit plans

        Raises:
            CouldNotFindMarkdownFileError:
            MarkdownFileMissingTitleError:
            EmptyMarkdownFileError:
            UnitPlanHasNoLessonsError:
        """

        # Convert the content to HTML
        try:
            unit_plan_content = self.convert_md_file(
                os.path.join(
                    self.BASE_PATH,
                    '{}.md'.format(self.unit_plan_name)
                )
            )
        except:
            raise CouldNotFindMarkdownFileError()

        # Check that content is not empty and that a title was extracted
        if unit_plan_content.title is None:
            raise MarkdownFileMissingTitleError()
        
        if len(unit_plan_content.html_string) == 0:
            raise EmptyMarkdownFileError()
        
        unit_plan_structure = self.load_yaml_file(self.structure_file)

        unit_plan = self.topic.topic_unit_plans.create(
            slug=self.unit_plan_name,
            name=unit_plan_content.title,
            content=unit_plan_content.html_string,
        )
        unit_plan.save() # TODO shouldn't have to save? create does this?

        self.log('Added Unit Plan: {}'.format(unit_plan.name), 1)

        # Load the lessons for the unit plan

        # If there is nothing in the structure dictionary there
        # are obvsiously no lessons! Error!
        if unit_plan_structure is None:
            raise UnitPlanHasNoLessonsError()

        if 'lessons' in unit_plan_structure:
            # Check there is at least one lesson
            if len(unit_plan_structure['lessons'].keys()) == 0:
                raise UnitPlanHasNoLessonsError()
            # Call the loader to save the lessons into the db
            lessons_structure = unit_plan_structure['lessons']
            LessonsLoader(
                self.load_log,
                lessons_structure,
                self.topic,
                unit_plan,
                self.BASE_PATH
            ).load()
        else:
            raise UnitPlanHasNoLessonsError()
