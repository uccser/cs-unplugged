import os.path
from django.db import transaction
from utils.BaseLoader import BaseLoader

from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.MarkdownFileMissingTitleError import MarkdownFileMissingTitleError
from utils.errors.TopicHasNoUnitPlansError import TopicHasNoUnitPlansError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from ._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader
from ._ProgrammingExercisesLoader import ProgrammingExercisesLoader
from ._UnitPlanLoader import UnitPlanLoader

from topics.models import Topic


class TopicLoader(BaseLoader):
    """Loader for the topics content"""

    def __init__(self, structure_file, BASE_PATH):
        """Initiates the topic loader

        Args:
            structure_file: file path (string)
            a dictionary of attributes.
        """
        super().__init__(BASE_PATH)
        self.topic_slug = os.path.split(structure_file)[0]
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, self.topic_slug)

    @transaction.atomic
    def load(self):
        """Load the content for a topic

        Raises:
            CouldNotFindMarkdownFileError:
            MarkdownFileMissingTitleError:
            EmptyMarkdownFileError:
            TopicHasNoUnitPlansError:
        """

        # Convert the content to HTML
        try:
            topic_content = self.convert_md_file(
                os.path.join(
                    self.BASE_PATH,
                    '{}.md'.format(self.topic_slug)
                )
            )
        except:
            raise CouldNotFindMarkdownFileError()

        # Check that content is not empty and that a title was extracted
        if topic_content.title is None:
            raise MarkdownFileMissingTitleError()
        
        if len(topic_content.html_string) == 0:
            raise EmptyMarkdownFileError()

        topic_structure = self.load_yaml_file(self.structure_file)

        # topic structure has at least one field that is required
        if topic_structure is None:
            raise MissingRequiredFieldError()

        # If other resources are given, convert to HTML
        if 'other_resources' in topic_structure:
            topic_other_resources_file = topic_structure['other-resources']
            if topic_other_resources_file:
                other_resources_content = self.convert_md_file(
                    os.path.join(
                        self.BASE_PATH,
                        topic_other_resources_file
                    )
                )
                topic_other_resources_html = other_resources_content.html_string
        else:
            topic_other_resources_html = None

        # Check if icon is given
        if 'icon' in topic_structure:
            topic_icon = topic_structure['icon']
        else:
            topic_icon = None

        # Create topic objects and save to the db
        topic = Topic(
            slug=self.topic_slug,
            name=topic_content.title,
            content=topic_content.html_string,
            other_resources=topic_other_resources_html,
            icon=topic_icon
        )
        topic.save()

        self.log('Added Topic: {}'.format(topic.name))

        # Load unit plans
        if 'unit-plans' in topic_structure:
            if len(topic_structure['unit-plans']) == 0:
                raise TopicHasNoUnitPlansError()
            for unit_plan_structure_file in topic_structure['unit-plans']:
                UnitPlanLoader(
                    self.load_log,
                    unit_plan_structure_file,
                    topic,
                    self.BASE_PATH
                ).load()
        else:
            raise TopicHasNoUnitPlansError()

        # Load programming exercises (if there are any)
        if 'programming-exercises' in topic_structure:
            ProgrammingExercisesLoader(
                self.load_log,
                topic_structure['programming-exercises'],
                topic,
                self.BASE_PATH
            ).load()

        # Load curriculum integrations (if there are any)
        if 'curriculum-integrations' in topic_structure:
            CurriculumIntegrationsLoader(
                self.load_log,
                topic_structure['curriculum-integrations'],
                topic,
                self.BASE_PATH
            ).load()

        # Print log output
        self.print_load_log()
