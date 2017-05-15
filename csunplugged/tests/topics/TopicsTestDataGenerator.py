"""Create test data for topic tests."""

import os.path
import yaml

from topics.models import (
    Topic,
    UnitPlan,
    Lesson,
    CurriculumIntegration,
    CurriculumArea,
    ProgrammingExerciseDifficulty,
    ProgrammingExerciseLanguage,
)


class TopicsTestDataGenerator:
    """Class for generating test data for topics."""

    def __init__(self):
        """Create TopicsTestDataGenerator object."""
        self.BASE_PATH = "tests/topics/"
        self.LOADER_ASSET_PATH = os.path.join(self.BASE_PATH, "loaders/assets/")

    def load_yaml_file(self, yaml_file_path):
        """Load a yaml file.

        Args:
            yaml_file_path:  The path to a given yaml file (str).

        Returns:
            Contents of a yaml file.
        """
        yaml_file = open(yaml_file_path, encoding="UTF-8").read()
        return yaml.load(yaml_file)

    def create_test_integration(self, topic, number, lessons=None, curriculum_areas=None):
        """Create curriculum integration object.

        Args:
            topic: The related Topic object.
            number: Integer representing the topic.
            lessons: List of prerequisite lessons.
            curriculum_areas: List of curriculum areas.

        Returns:
            CurriculumIntegration object.
        """
        integration = CurriculumIntegration(
            topic=topic,
            slug="integration-{}".format(number),
            name="Integration {}".format(number),
            number=number,
            content="Content for integration {}.".format(number),
        )
        integration.save()
        if lessons:
            for lesson in lessons:
                integration.prerequisite_lessons.add(lesson)
        if curriculum_areas:
            for curriculum_area in curriculum_areas:
                integration.curriculum_areas.add(curriculum_area)
        return integration

    def create_test_curriculum_area(self, number, parent=None):
        """Create curriculum area object.

        Args:
            number: Integer representing the area.
            parent: Parent of the curriculum area.

        Returns:
            CurriculumArea object.
        """
        area = CurriculumArea(
            slug="area-{}".format(number),
            name="Area {}".format(number),
            parent=parent,
        )
        area.save()
        return area

    def create_test_topic(self, number):
        """Create topic object.

        Args:
            number: Integer representing the topic.

        Returns:
            Topic object.
        """
        topic = Topic(
            slug="topic-{}".format(number),
            name="Topic {}".format(number),
            content="Content for topic {}.".format(number),
        )
        topic.save()
        return topic

    def create_test_unit_plan(self, topic, number):
        """Create unit plan object.

        Args:
            topic: The related Topic object.
            number: Integer representing the unit plan.

        Returns:
            Unit plan object.
        """
        unit_plan = UnitPlan(
            topic=topic,
            slug="unit-plan-{}".format(number),
            name="Unit Plan {}".format(number),
            content="Content for unit plan {}.".format(number),
        )
        unit_plan.save()
        return unit_plan

    def create_test_lesson(self, topic, unit_plan, number, min_age, max_age):
        """Create lesson object.

        Args:
            topic: The related Topic object.
            unit_plan: The related UnitPlan object.
            number: Integer representing the topic.
            min_age: Integer of the minimum age of the lesson.
            max_age: Integer of the maximum age of the lesson.

        Returns:
            Lesson object.
        """
        lesson = Lesson(
            topic=topic,
            unit_plan=unit_plan,
            slug="lesson-{}".format(number),
            name="Lesson {} ({} to {})".format(number, min_age, max_age),
            number=number,
            duration=number,
            content="Content for lesson {}.".format(number),
            min_age=min_age,
            max_age=max_age,
        )
        lesson.save()
        return lesson

    def create_test_difficulty_level(self, number):
        """
        Create difficuly level object.

        Args:
          number: Integer representing the level.
        """
        difficulty = ProgrammingExerciseDifficulty(
            level="1",
            name="Difficulty-{}".format(number)
        )
        difficulty.save()
        return difficulty

    def create_test_programming_language(self, number):
        """
        Create programming language object.

        Args:
          number: Integer representing the language.
        """
        language = ProgrammingExerciseLanguage(
            slug="language-{}".format(number),
            name="Language {}".format(number),
        )
        language.save()
        return language
