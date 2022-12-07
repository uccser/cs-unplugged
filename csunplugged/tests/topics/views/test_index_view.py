from http import HTTPStatus
from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class IndexViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_index_with_no_topics(self):
        url = reverse("topics:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_index_with_one_topic(self):
        topic = self.test_data.create_topic(1)
        age_group = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            1,
            age_group
        )
        url = reverse("topics:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["topics"],
            ["<Topic: Topic 1>"]
        )

    def test_index_with_multiple_topics(self):
        topic_1 = self.test_data.create_topic(1)
        age_group = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic_1,
            1,
            age_group
        )
        topic_2 = self.test_data.create_topic(2)
        self.test_data.create_lesson(
            topic_2,
            1,
            age_group
        )
        url = reverse("topics:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["topics"],
            ["<Topic: Topic 1>", "<Topic: Topic 2>"]
        )

    def test_index_topic_single_age_group_context(self):
        topic = self.test_data.create_topic(1)
        age_group = self.test_data.create_age_group(10, 30)
        self.test_data.create_lesson(
            topic,
            1,
            age_group
        )
        url = reverse("topics:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        topic = response.context["topics"][0]
        self.assertEqual(topic.min_age, 10)
        self.assertEqual(topic.max_age, 30)

    def test_index_topic_multiple_age_groups_context(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(10, 30)
        age_group_2 = self.test_data.create_age_group(30, 50)
        age_group_3 = self.test_data.create_age_group(50, 99)
        self.test_data.create_lesson(
            topic,
            1,
            [age_group_1, age_group_2, age_group_3]
        )
        url = reverse("topics:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        topic = response.context["topics"][0]
        self.assertEqual(topic.min_age, 10)
        self.assertEqual(topic.max_age, 99)
