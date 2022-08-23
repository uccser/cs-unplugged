"""Create test data for at a distance tests."""

import os.path
import yaml

from at_a_distance.models import (
    Lesson,
    SupportingResource,
)


class AtADistanceTestDataGenerator:
    """Class for generating test data for at a distance application."""

    def __init__(self):
        """Create AtADistanceTestDataGenerator object."""
        self.BASE_PATH = "tests/at_a_distance/"
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

    def create_lesson(self, number, student_suitability=Lesson.SUITABLE, educator_suitability=Lesson.SUITABLE):
        """Create lesson object.

        Args:
            number: Identifier of the lesson (int).

        Returns:
            Lesson object.
        """
        lesson = Lesson(
            slug=f"lesson-{number}",
            name=f"Lesson {number}",
            order_number=number,
            icon=f"img/lesson-{number}.png",
            languages=["en"],
            suitable_for_teaching_students=student_suitability,
            suitable_for_teaching_educators=educator_suitability,
            introduction=f"Content for Lesson {number}",
        )
        lesson.save()
        return lesson

    def create_supporting_resource(self, lesson, number):
        """Create supporting resource object.

        Args:
            lesson: The related lesson object (Lesson).
            number: Identifier of the supporting resource (int).

        Returns:
            SupportingResource object.
        """
        supporting_resource = SupportingResource(
            order_number=number,
            text=f"Supporting Resource {number}",
            url=f"https://www.resource-{number}.com",
            language="en",
            lesson=lesson,
        )
        supporting_resource.save()
        return supporting_resource
