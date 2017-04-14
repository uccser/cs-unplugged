import os.path
from utils.BaseLoader import BaseLoader

from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.MarkdownFileMissingTitleError import MarkdownFileMissingTitleError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError

from topics.models import (
    ProgrammingExercise,
    LearningOutcome,
    CurriculumArea,
    ClassroomResource,
    Resource,
    ConnectedGeneratedResource,
)


class LessonLoader(BaseLoader):
    '''Loader for a single lesson'''

    def __init__(self, load_log, lesson_slug, lesson_structure, topic, unit_plan, BASE_PATH):
        '''Initiates the loader for a single lesson

        Args:
            lesson_slug: string of the URL slug for a lesson
            lesson_structure: dictionary containing attributes for a lesson
            topic: Topic model object
            unit_plan: UnitPlan model object
        '''
        super().__init__(BASE_PATH, load_log)
        self.lesson_slug = lesson_slug
        self.lesson_structure = lesson_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        '''Load the content for a single lesson

        Raises:
            CouldNotFindMarkdownFileError:
            EmptyMarkdownFileError:
            MarkdownFileMissingTitleError:
            MissingRequiredFieldError:
            KeyNotFoundError:
        '''
        # Retrieve required variables from structure dictionary
        try:
            lesson_min_age = self.lesson_structure['min-age']
            lesson_max_age = self.lesson_structure['max-age']
            lesson_number = self.lesson_structure['number']
        except:
            raise MissingRequiredFieldError()

        # Build the file path to the lesson's md file
        file_path = os.path.join(
            self.BASE_PATH,
            'lessons',
            '{}-{}'.format(lesson_min_age, lesson_max_age),
            '{}.md'.format(self.lesson_slug)
        )

        # Throw and error if the md file cannot be found
        try:
            lesson_content = self.convert_md_file(file_path)
        except:
            raise CouldNotFindMarkdownFileError()

        # Check that content is not empty and that a title was extracted
        if lesson_content.title is None:
            raise MarkdownFileMissingTitleError()

        if len(lesson_content.html_string) == 0:
            raise EmptyMarkdownFileError()

        if 'duration' in self.lesson_structure:
            lesson_duration = self.lesson_structure['duration']
        else:
            lesson_duration = None

        lesson = self.topic.topic_lessons.create(
            unit_plan=self.unit_plan,
            slug=self.lesson_slug,
            name=lesson_content.title,
            number=lesson_number,
            duration=lesson_duration,
            content=lesson_content.html_string,
            min_age=lesson_min_age,
            max_age=lesson_max_age
        )
        lesson.save()

        # Add programming exercises
        if 'programming-exercises' in self.lesson_structure:
            programming_exercise_slugs = self.lesson_structure['programming-exercises']
            for programming_exercise_slug in programming_exercise_slugs:
                try:
                    programming_exercise = ProgrammingExercise.objects.get(
                        slug=programming_exercise_slug
                    )
                    lesson.programming_exercises.add(programming_exercise)
                except:
                    raise KeyNotFoundError()

        # Add learning outcomes
        if 'learning-outcomes' in self.lesson_structure:
            learning_outcome_slugs = self.lesson_structure['learning-outcomes']
            for learning_outcome_slug in learning_outcome_slugs:
                try:
                    learning_outcome = LearningOutcome.objects.get(
                        slug=learning_outcome_slug
                    )
                    lesson.learning_outcomes.add(learning_outcome)
                except:
                    raise KeyNotFoundError()

        # Add curriculum areas
        if 'curriculum-areas' in self.lesson_structure:
            curriculum_area_slugs = self.lesson_structure['curriculum-areas']
            for curriculum_area_slug in curriculum_area_slugs:
                try:
                    curriculum_area = CurriculumArea.objects.get(
                        slug=curriculum_area_slug
                    )
                    lesson.curriculum_areas.add(curriculum_area)
                except:
                    raise KeyNotFoundError()

        # TODO figure out how to error handle class resources and generated resources

        # Add classroom resources
        if 'resources-classroom' in self.lesson_structure:
            for resource in self.lesson_structure['resources-classroom']:
                (object, created) = ClassroomResource.objects.get_or_create(
                    text=resource
                )
                lesson.classroom_resources.add(object)

        # Add generated resources
        if 'resources-generated' in self.lesson_structure:
            for resource_data in self.lesson_structure['resources-generated']:
                resource_slug = resource_data['slug']
                resource = Resource.objects.get(
                    slug=resource_slug
                )
                relationship = ConnectedGeneratedResource(
                    resource=resource,
                    lesson=lesson,
                    description=resource_data['description']
                )
                relationship.save()

        self.log('Added Lesson: {}'.format(lesson.__str__()), 2)
