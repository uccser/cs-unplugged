"""Create test data for topic tests."""

from topics.models import (
    Topic,
    UnitPlan,
    Lesson,
    CurriculumIntegration,
    CurriculumArea,
)


def create_test_integration(topic, number, lessons=None, curriculum_areas=None):
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
        slug="integration_{}".format(number),
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


def create_test_curriculum_area(number, parent=None):
    """Create curriculum area object.

    Args:
        number: Integer representing the area.
        parent: Parent of the curriculum area.

    Returns:
        CurriculumArea object.
    """
    area = CurriculumArea(
        slug="area_{}".format(number),
        name="Area {}".format(number),
        parent=parent,
    )
    area.save()
    return area


def create_test_topic(number):
    """Create topic object.

    Args:
        number: Integer representing the topic.

    Returns:
        Topic object.
    """
    topic = Topic(
        slug="topic_{}".format(number),
        name="Topic {}".format(number),
        content="Content for topic {}.".format(number),
    )
    topic.save()
    return topic


def create_test_unit_plan(number, topic):
    """Create unit plan object.

    Args:
        number: Integer representing the topic.
        topic: The related Topic object.

    Returns:
        UnitPlan object.
    """
    unit_plan = UnitPlan(
        topic=topic,
        slug="unit-plan-{}".format(number),
        name="Unit Plan {}".format(number),
        content="Content for unit plan {}.".format(number),
    )
    unit_plan.save()
    return unit_plan


def create_test_lesson(topic, unit_plan, number, min_age, max_age):
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
        slug="lesson_{}".format(number),
        name="Lesson {} ({} to {})".format(number, min_age, max_age),
        number=number,
        duration=number,
        content="Content for lesson {}.".format(number),
        min_age=min_age,
        max_age=max_age,
    )
    lesson.save()
    return lesson
