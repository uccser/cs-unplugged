from model_mommy import mommy
from topics.models import (
    Topic,
    Lesson,
    CurriculumIntegration,
    CurriculumArea,
)


def create_test_integration(topic, number, lessons=None, curriculum_areas=None):
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
    area = CurriculumArea(
        slug="area_{}".format(number),
        name="Area {}".format(number),
        parent=parent,
    )
    area.save()
    return area


def create_test_topic(number):
    topic = Topic(
        slug="topic_{}".format(number),
        name="Topic {}".format(number),
        content="Content for topic {}.".format(number),
    )
    topic.save()
    return topic


def create_test_lesson(topic, unit_plan, number, min_age, max_age):
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
