"""Custom loader for loading lessons."""

import os.path
from utils.BaseLoader import BaseLoader
from utils.convert_heading_tree_to_dict import convert_heading_tree_to_dict
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.InvalidConfigValueError import InvalidConfigValueError

from topics.models import (
    ProgrammingExercise,
    LearningOutcome,
    Resource,
    ConnectedGeneratedResource,
)


class LessonsLoader(BaseLoader):
    """Custom loader for loading lessons."""

    def __init__(self, unit_plan_structure_file_path, load_log, lessons_structure, topic, unit_plan, BASE_PATH):
        """Create the loader for loading lessons.

        Args:
            unit_plan_structure_file_path: file path to unit plan yaml file (string).
            load_log: List of log messages (list).
            lessons_structure: List of dictionaries for each lesson (list).
            topic: Object of Topic model.
            unit_plan: Object of UnitPlan model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH, load_log)
        self.unit_plan_structure_file_path = unit_plan_structure_file_path
        self.lessons_structure = lessons_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """Load the content for a single lesson.

        Raises:
            KeyNotFoundError: when no object can be found with the matching attribute.
            MissingRequiredFieldError: when a value for a required model field cannot be
                found in the config file.
        """
        for (lesson_slug, lesson_structure) in self.lessons_structure.items():

            if lesson_structure is None:
                raise MissingRequiredFieldError(
                    self.unit_plan_structure_file_path,
                    ["min-age", "max-age", "number"],
                    "Lesson"
                )

            # Retrieve required variables from structure dictionary
            lesson_min_age = lesson_structure.get("min-age", None)
            lesson_max_age = lesson_structure.get("max-age", None)
            lesson_number = lesson_structure.get("number", None)
            if None in [lesson_min_age, lesson_max_age, lesson_number]:
                raise MissingRequiredFieldError(
                    self.unit_plan_structure_file_path,
                    ["min-age", "max-age", "number"],
                    "Lesson"
                )

            # Build the file path to the lesson"s md file
            file_path = os.path.join(
                self.BASE_PATH,
                "lessons",
                "{}-{}".format(lesson_min_age, lesson_max_age),
                "{}.md".format(lesson_slug)
            )

            lesson_content = self.convert_md_file(
                file_path,
                self.unit_plan_structure_file_path
            )

            if "duration" in lesson_structure:
                lesson_duration = lesson_structure["duration"]
            else:
                lesson_duration = None

            heading_tree = convert_heading_tree_to_dict(lesson_content.heading_tree)

            classroom_resources = lesson_structure.get("classroom-resources", None)
            if isinstance(classroom_resources, list):
                for classroom_resource in classroom_resources:
                    if not isinstance(classroom_resource, str):
                        raise InvalidConfigValueError(
                            self.unit_plan_structure_file_path,
                            "classroom-resources list item",
                            "A string describing the classroom resource."
                        )
                    elif len(classroom_resource) > 100:
                        raise InvalidConfigValueError(
                            self.unit_plan_structure_file_path,
                            "classroom-resources list item",
                            "Item description must be less than 100 characters."
                        )
            elif classroom_resources is not None:
                raise InvalidConfigValueError(
                    self.unit_plan_structure_file_path,
                    "classroom-resources",
                    "List of strings."
                )

            lesson = self.topic.topic_lessons.create(
                unit_plan=self.unit_plan,
                slug=lesson_slug,
                name=lesson_content.title,
                number=lesson_number,
                duration=lesson_duration,
                content=lesson_content.html_string,
                min_age=lesson_min_age,
                max_age=lesson_max_age,
                heading_tree=heading_tree,
                classroom_resources=classroom_resources,
            )
            lesson.save()

            # Add programming exercises
            if "programming-exercises" in lesson_structure:
                programming_exercise_slugs = lesson_structure["programming-exercises"]
                if programming_exercise_slugs is not None:
                    for programming_exercise_slug in programming_exercise_slugs:
                        try:
                            programming_exercise = ProgrammingExercise.objects.get(
                                slug=programming_exercise_slug,
                                topic=self.topic
                            )
                            lesson.programming_exercises.add(programming_exercise)
                        except:
                            raise KeyNotFoundError(
                                self.unit_plan_structure_file_path,
                                programming_exercise_slug,
                                "Programming Exercises"
                            )

            # Add learning outcomes
            if "learning-outcomes" in lesson_structure:
                learning_outcome_slugs = lesson_structure["learning-outcomes"]
                if learning_outcome_slugs is not None:
                    for learning_outcome_slug in learning_outcome_slugs:
                        try:
                            learning_outcome = LearningOutcome.objects.get(
                                slug=learning_outcome_slug
                            )
                            lesson.learning_outcomes.add(learning_outcome)
                        except:
                            raise KeyNotFoundError(
                                self.unit_plan_structure_file_path,
                                learning_outcome_slug,
                                "Learning Outcomes"
                            )

            # Add generated resources
            if "generated-resources" in lesson_structure:
                resources = lesson_structure["generated-resources"]
                if resources is not None:
                    for (resource_slug, resource_data) in resources.items():
                        if resource_data is None:
                            raise MissingRequiredFieldError(
                                self.unit_plan_structure_file_path,
                                ["description"],
                                "Generated Resource"
                            )
                        try:
                            resource = Resource.objects.get(
                                slug=resource_slug
                            )
                        except:
                            raise KeyNotFoundError(
                                self.unit_plan_structure_file_path,
                                resource_slug,
                                "Resources"
                            )
                    resource_description = resource_data.get("description", None)
                    if resource_description is None:
                        raise MissingRequiredFieldError(
                            self.unit_plan_structure_file_path,
                            ["description"],
                            "Generated Resource"
                        )

                    relationship = ConnectedGeneratedResource(
                        resource=resource,
                        lesson=lesson,
                        description=resource_description
                    )
                    relationship.save()

            self.log("Added Lesson: {}".format(lesson.__str__()), 2)
