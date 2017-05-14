"""Create test data for topic tests."""
import os.path

from topics.models import (
    Topic,
    Lesson,
    CurriculumIntegration,
    CurriculumArea,
)


class TestDataGenerator:

    def __init__(self):
        self.BASE_PATH = "tests/topics/"
        self.LOADER_ASSET_PATH = os.path.join(self.BASE_PATH, "loaders/assets/")

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
