from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from topics.models import LessonNumber


class LessonViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()
        self.resource_test_data = ResourcesTestDataGenerator()

    def test_lesson_view_with_valid_slugs(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_lesson_view_with_invalid_topic_slug(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "invalid-slug",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_lesson_view_with_invalid_unit_plan_slug(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "invalid-slug",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_lesson_view_with_invalid_lesson_slug(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "invalid-slug",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_lesson_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_lesson_view_unit_plan_context(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["unit_plan"],
            unit_plan
        )

    def test_lesson_view_ages_context_single_group(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["lesson_ages"],
            [{"lower": 5, "upper": 7, "number": 1}]
        )

    def test_lesson_view_ages_context_multiple_group(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        age_group_2 = self.test_data.create_age_group(8, 10)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        LessonNumber(
            age_group=age_group_2,
            lesson=lesson,
            number=1,
        ).save()
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["lesson_ages"],
            [
                {"lower": 5, "upper": 7, "number": 1},
                {"lower": 8, "upper": 10, "number": 1},
            ]
        )

    def test_lesson_view_ages_context_programming_challenges(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.add_challenge_lesson_relationship(challenge, lesson, 1, 1)
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertTrue(response.context["programming_challenges"])

    def test_lesson_view_ages_context_programming_challenges_none(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertFalse(response.context["programming_challenges"])

    def test_lesson_view_ages_context_learning_outcome_single(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        learning_outcome = self.test_data.create_learning_outcome(1)
        lesson.learning_outcomes.add(learning_outcome)
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["learning_outcomes"],
            ["<LearningOutcome: Outcome 1>"]
        )

    def test_lesson_view_ages_context_learning_outcome_multiple(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        learning_outcome1 = self.test_data.create_learning_outcome(1)
        lesson.learning_outcomes.add(learning_outcome1)
        learning_outcome2 = self.test_data.create_learning_outcome(2)
        lesson.learning_outcomes.add(learning_outcome2)
        learning_outcome3 = self.test_data.create_learning_outcome(3)
        lesson.learning_outcomes.add(learning_outcome3)
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["learning_outcomes"],
            [
                "<LearningOutcome: Outcome 1>",
                "<LearningOutcome: Outcome 2>",
                "<LearningOutcome: Outcome 3>",
            ],
            ordered=False
        )

    # Created to avoid https://github.com/uccser/cs-unplugged/issues/827
    def test_lesson_view_ages_context_learning_outcome_not_duplicated(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        learning_outcome = self.test_data.create_learning_outcome(1)
        area_1 = self.test_data.create_curriculum_area(1)
        area_2 = self.test_data.create_curriculum_area(2)
        learning_outcome.curriculum_areas.add(area_1, area_2)
        lesson.learning_outcomes.add(learning_outcome)
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["learning_outcomes"],
            ["<LearningOutcome: Outcome 1>"]
        )

    def test_lesson_view_ages_context_learning_outcome_none(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertFalse(response.context["learning_outcomes"])

    def test_lesson_view_ages_context_generated_resources_single(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        resource = self.resource_test_data.create_resource(
            "bare",
            "Bare",
            "resources/bare.html",
            "BareResourceGenerator",
        )
        self.test_data.add_lesson_resource_relationship(lesson, resource, 1)
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["generated_resources"],
            [
                {
                    "description": "Description 1",
                    "slug": "bare",
                    "name": "Bare",
                    "thumbnail": "/staticfiles/img/resources/bare/thumbnails/en/bare-paper_size-a4.png",
                }
            ]
        )

    def test_lesson_view_ages_context_generated_resources_multiple(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        resource1 = self.resource_test_data.create_resource(
            "bare",
            "Bare",
            "resources/bare.html",
            "BareResourceGenerator",
        )
        self.test_data.add_lesson_resource_relationship(lesson, resource1, 1)
        resource2 = self.resource_test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        self.test_data.add_lesson_resource_relationship(lesson, resource2, 2)
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["generated_resources"],
            [
                {
                    "description": "Description 2",
                    "slug": "arrows",
                    "name": "Arrows",
                    "thumbnail": "/static/img/resources/arrows/thumbnails/en/arrows-paper_size-a4.png",
                },
                {
                    "description": "Description 1",
                    "slug": "bare",
                    "name": "Bare",
                    "thumbnail": "/staticfiles/img/resources/bare/thumbnails/en/bare-paper_size-a4.png",
                },
            ]
        )

    def test_lesson_view_ages_context_generated_resources_none(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": "topic-1",
            "unit_plan_slug": "unit-plan-1",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["generated_resources"],
            []
        )
