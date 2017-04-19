import os.path

from utils.BaseLoader import BaseLoader

from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.MarkdownFileMissingTitleError import MarkdownFileMissingTitleError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import CurriculumArea, Lesson


class CurriculumIntegrationsLoader(BaseLoader):
    '''Loader for curriculum integrations'''

    def __init__(self, load_log, structure_file_path, topic, BASE_PATH):
        '''Initiates the loader for curriculum integrations

        Args:
            structure_file_path_path: file path (string)
            topic: Topic model object
        '''
        super().__init__(BASE_PATH, load_log)
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])
        self.topic = topic

    def load(self):
        '''Load the content for curriculum integrations

        Raises:
            CouldNotFindMarkdownFileError:
            MarkdownFileMissingTitleError:
            EmptyMarkdownFileError:
            KeyNotFoundError:
            MissingRequiredFieldError:
        '''
        structure = self.load_yaml_file(self.structure_file_path)

        for (integration_slug, integration_data) in structure.items():

            integration_content = self.convert_md_file(
                os.path.join(
                    self.BASE_PATH,
                    '{}.md'.format(integration_slug)
                ),
                self.structure_file_path
            )

            try:
                integration_number = integration_data['number']
                integration_curriculum_areas = integration_data['curriculum-areas']
            except:
                raise MissingRequiredFieldError()

            integration = self.topic.curriculum_integrations.create(
                slug=integration_slug,
                number=integration_data['number'],
                name=integration_content.title,
                content=integration_content.html_string,
            )
            integration.save()

            # Add curriculum areas
            for curriculum_area_slug in integration_curriculum_areas:
                try:
                    curriculum_area = CurriculumArea.objects.get(
                        slug=curriculum_area_slug
                    )
                    integration.curriculum_areas.add(curriculum_area)
                except:
                    raise KeyNotFoundError()

            # Add prerequisite lessons
            if 'prerequisite-lessons' in integration_data:
                prerequisite_lessons = integration_data['prerequisite-lessons']
                for (unit_plan_slug, lessons) in prerequisite_lessons.items():
                    for lesson_slug in lessons:
                        try:
                            lesson = Lesson.objects.get(
                                slug=lesson_slug,
                                unit_plan__slug=unit_plan_slug,
                                topic__slug=self.topic.slug
                            )
                            integration.prerequisite_lessons.add(lesson)
                        except:
                            raise KeyNotFoundError()

            self.log('Added Curriculum Integration: {}'.format(integration.name), 1)
