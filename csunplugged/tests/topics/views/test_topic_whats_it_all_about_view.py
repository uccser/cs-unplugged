from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class TopicWhatsItAllAboutViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_topic_whats_it_all_about_view_with_valid_slugs(self):
        topic = self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": topic.slug,
        }
        url = reverse("topics:topic_whats_it_all_about", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_topic_whats_it_all_about_view_with_invalid_topic_slug(self):
        self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": "wrong_slug",
        }
        url = reverse("topics:topic_whats_it_all_about", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_topic_whats_it_all_about_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": topic.slug,
        }
        url = reverse("topics:topic_whats_it_all_about", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_topic_whats_it_all_about_view_templates(self):
        topic = self.test_data.create_topic(1)
        kwargs = {
            "topic_slug": topic.slug,
        }
        url = reverse("topics:topic_whats_it_all_about", kwargs=kwargs)
        response = self.client.get(url)
        template_found = False
        for template in response.templates:
            if template.name == "topics/topic-whats-it-all-about.html":
                template_found = True
        self.assertTrue(template_found)
