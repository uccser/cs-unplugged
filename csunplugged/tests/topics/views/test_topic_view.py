from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class TopicViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_topic_view_with_valid_slug(self):
        topic = self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": topic.slug
        }
        url = reverse("topics:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_topic_view_with_invalid_slug(self):
        self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": "wrong_slug",
        }
        url = reverse("topics:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_topic_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": topic.slug,
        }
        unit_plan_1 = self.test_data.create_unit_plan(topic, 1)
        unit_plan_2 = self.test_data.create_unit_plan(topic, 2)
        age_group_1 = self.test_data.create_age_group(5, 7)
        age_group_2 = self.test_data.create_age_group(5, 10)
        age_group_3 = self.test_data.create_age_group(8, 12)

        lesson1 = self.test_data.create_lesson(
            topic,
            unit_plan_1,
            1,
            age_group_2
        )
        lesson2 = self.test_data.create_lesson(
            topic,
            unit_plan_1,
            1,
            age_group_1
        )
        lesson3 = self.test_data.create_lesson(
            topic,
            unit_plan_2,
            1,
            age_group_3
        )
        lesson4 = self.test_data.create_lesson(
            topic,
            unit_plan_2,
            1,
            age_group_2
        )

        url = reverse("topics:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["unit_plans"],
            [
                <UnitPlan: Unit Plan 1>, 
                <UnitPlan: Unit Plan 2>
            ]
        )
