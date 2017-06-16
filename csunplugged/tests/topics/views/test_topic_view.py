from django.urls import reverse

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from topics.models import ResourceDescription


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
        self.assertEqual(200, response.status_code)

    def test_topic_view_with_invalid_slug(self):
        self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": "wrong_slug",
        }
        url = reverse("topics:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_topic_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": topic.slug,
        }
        url = reverse("topics:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_topic_view_lessons_context(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_range_1 = self.test_data.create_age_range(5, 7)
        lesson1 = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_range_1
        )
        lesson2 = self.test_data.create_lesson(
            topic,
            unit_plan,
            2,
            age_range_1
        )
        kwargs = {
            "topic_slug": topic.slug,
        }
        url = reverse("topics:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["grouped_lessons"]),
            1
        )
        grouped_lessons = response.context["grouped_lessons"]
        for (age_range, lessons) in grouped_lessons.items():
            self.assertEqual(age_range, "<AgeRange: NumericRange(5, 7, '[)')>")
            self.assertEqual(
                lessons,
                [lesson1, lesson2]
            )

    def test_topic_view_resources_context(self):
        resource_test_data = ResourcesTestDataGenerator()
        # Create topic data
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_range_1 = self.test_data.create_age_range(5, 7)
        lesson1 = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_range_1
        )
        lesson2 = self.test_data.create_lesson(
            topic,
            unit_plan,
            2,
            age_range_1
        )
        # Create resource data
        resource1 = resource_test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "binary_cards_small.py",
        )
        resource2 = resource_test_data.create_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "binary_windows.py",
        )
        # Create relationships
        relationship1 = ResourceDescription(
            resource=resource1,
            lesson=lesson1,
            description="Description of Binary Cards (small)"
        )
        relationship1.save()
        relationship2 = ResourceDescription(
            resource=resource2,
            lesson=lesson2,
            description="Description of Binary Windows"
        )
        relationship2.save()
        # Perform tests
        kwargs = {
            "topic_slug": topic.slug,
        }
        url = reverse("topics:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["resources"]),
            2
        )
        self.assertQuerysetEqual(
            response.context["resources"],
            [
                "<Resource: Resource Binary Windows>",
                "<Resource: Resource Binary Cards (small)>",
            ],
            ordered=False,
        )
