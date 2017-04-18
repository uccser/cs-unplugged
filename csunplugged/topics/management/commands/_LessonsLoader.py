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
    Resource,
    ConnectedGeneratedResource,
)


class LessonsLoader(BaseLoader):
    '''Loader for lessons'''

    def __init__(self, load_log, lessons_structure, topic, unit_plan, BASE_PATH):
        '''Inititiates the loader for lessons

        Args:
            lessons_structure: list of dictionaries for each lesson
            topic: Topic model object
            unit_plan: UnitPlan model object
        '''
        super().__init__(BASE_PATH, load_log)
        self.lessons_structure = lessons_structure
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
        for (lesson_slug, lesson_structure) in self.lessons_structure.items():
            
            # Retrieve required variables from structure dictionary
            try:
                lesson_min_age = lesson_structure['min-age']
                lesson_max_age = lesson_structure['max-age']
                lesson_number = lesson_structure['number']
            except:
                raise MissingRequiredFieldError()

            # Build the file path to the lesson's md file
            file_path = os.path.join(
                self.BASE_PATH,
                'lessons',
                '{}-{}'.format(lesson_min_age, lesson_max_age),
                '{}.md'.format(lesson_slug)
            )

            lesson_content = self.convert_md_file(file_path)

            if 'duration' in lesson_structure:
                lesson_duration = lesson_structure['duration']
            else:
                lesson_duration = None

            lesson = self.topic.topic_lessons.create(
                unit_plan=self.unit_plan,
                slug=lesson_slug,
                name=lesson_content.title,
                number=lesson_number,
                duration=lesson_duration,
                content=lesson_content.html_string,
                min_age=lesson_min_age,
                max_age=lesson_max_age
            )
            lesson.save()

            # Add programming exercises
            if 'programming-exercises' in lesson_structure:
                programming_exercise_slugs = lesson_structure['programming-exercises']
                for programming_exercise_slug in programming_exercise_slugs:
                    try:
                        programming_exercise = ProgrammingExercise.objects.get(
                            slug=programming_exercise_slug
                        )
                        lesson.programming_exercises.add(programming_exercise)
                    except:
                        raise KeyNotFoundError()

            # Add learning outcomes
            if 'learning-outcomes' in lesson_structure:
                learning_outcome_slugs = lesson_structure['learning-outcomes']
                for learning_outcome_slug in learning_outcome_slugs:
                    try:
                        learning_outcome = LearningOutcome.objects.get(
                            slug=learning_outcome_slug
                        )
                        lesson.learning_outcomes.add(learning_outcome)
                    except:
                        raise KeyNotFoundError()

            # Add curriculum areas
            if 'curriculum-areas' in lesson_structure:
                curriculum_area_slugs = lesson_structure['curriculum-areas']
                for curriculum_area_slug in curriculum_area_slugs:
                    try:
                        curriculum_area = CurriculumArea.objects.get(
                            slug=curriculum_area_slug
                        )
                        lesson.curriculum_areas.add(curriculum_area)
                    except:
                        raise KeyNotFoundError()

            # Add generated resources
            if 'generated-resources' in lesson_structure:
                resources = lesson_structure['generated-resources']
                for (resource_slug, resource_data) in resources.items():
                    try:
                        resource = Resource.objects.get(
                            slug=resource_slug
                        )
                    except:
                        raise KeyNotFoundError()

                    try:
                        resource_description = resource_data['description']
                    except:
                        raise MissingRequiredFieldError()

                    relationship = ConnectedGeneratedResource(
                        resource=resource,
                        lesson=lesson,
                        description=resource_description
                    )
                    relationship.save()

            self.log('Added Lesson: {}'.format(lesson.__str__()), 2)

