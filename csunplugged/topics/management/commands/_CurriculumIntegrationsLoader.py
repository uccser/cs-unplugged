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

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        '''Initiates the loader for curriculum integrations

        Args:
            structure_file: file path (string)
            topic: Topic model object
        '''
        super().__init__(BASE_PATH, load_log)
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])
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
        if self.structure_file:
            structure = self.load_yaml_file(self.structure_file)

            for integration_slug, integration_data in structure.items():
                try:
                    integration_content = self.convert_md_file(
                        os.path.join(
                            self.BASE_PATH,
                            '{}.md'.format(integration_slug)
                        )
                    )
                except:
                    raise CouldNotFindMarkdownFileError()

                # Check that content is not empty and that a title was extracted
                if integration_content.title is None:
                    raise MarkdownFileMissingTitleError()
                
                if len(integration_content.html_string) == 0:
                    raise EmptyMarkdownFileError()

                try:
                    integration_number = integration_data['number']
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
                if 'curriculum-areas' in integration_data:
                    curriculum_area_slugs = integration_data['curriculum-areas']
                    for curriculum_area_slug in curriculum_area_slugs:
                        try:
                            curriculum_area = CurriculumArea.objects.get(
                                slug=curriculum_area_slug
                            )
                            integration.curriculum_areas.add(curriculum_area)
                        except:
                            raise KeyNotFoundError()

                # Add prerequisite lessons
                if 'prerequisite-lessons' in integration_data:
                    prerequisite_lessons_slugs = integration_data['prerequisite-lessons']
                    for lesson_slug in prerequisite_lessons_slugs:
                        try:
                            lesson = Lesson.objects.get(
                                slug=lesson_slug,
                                topic__slug=self.topic.slug
                            )
                            integration.prerequisite_lessons.add(lesson)
                        except:
                            raise KeyNotFoundError()

                self.log('Added Curriculum Integration: {}'.format(integration.name), 1)
