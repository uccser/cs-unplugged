from django.urls import reverse
from model_mommy import mommy
from tests.BaseTestWithDB import BaseTestWithDB
from topics.models import (
    CurriculumIntegration,
    Topic,
    CurriculumArea,
    Lesson,
)

class AllCurriculumIntegrationViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_all_curriculum_integration_view_with_no_integrations(self):
        url = reverse("topics:all_curriculum_integrations")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["curriculum_integrations"]), 0)

    def test_all_curriculum_integration_view_with_one_integration(self):
        topic = mommy.make(Topic)
        self.create_test_integration(topic, 1)

        url = reverse("topics:all_curriculum_integrations")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["curriculum_integrations"]), 1)
        self.assertQuerysetEqual(
            response.context["curriculum_integrations"],
            ["<CurriculumIntegration: Integration 1>"]
        )

    def test_all_curriculum_integration_view_with_multiple_integration(self):
        topic = mommy.make(Topic)
        self.create_test_integration(topic, 1)
        self.create_test_integration(topic, 2)
        self.create_test_integration(topic, 3)

        url = reverse("topics:all_curriculum_integrations")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["curriculum_integrations"]), 3)
        self.assertQuerysetEqual(
            response.context["curriculum_integrations"],
            [
                "<CurriculumIntegration: Integration 1>",
                "<CurriculumIntegration: Integration 2>",
                "<CurriculumIntegration: Integration 3>",
            ]
        )

    def test_all_curriculum_integration_view_order(self):
        topic_1 = mommy.make(Topic, name="1")
        topic_2 = mommy.make(Topic, name="2")
        self.create_test_integration(topic_2, 3)
        self.create_test_integration(topic_2, 2)
        self.create_test_integration(topic_2, 1)
        self.create_test_integration(topic_1, 4)
        self.create_test_integration(topic_1, 5)
        self.create_test_integration(topic_1, 6)

        url = reverse("topics:all_curriculum_integrations")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["curriculum_integrations"]), 6)
        self.assertQuerysetEqual(
            response.context["curriculum_integrations"],
            [
                "<CurriculumIntegration: Integration 4>",
                "<CurriculumIntegration: Integration 5>",
                "<CurriculumIntegration: Integration 6>",
                "<CurriculumIntegration: Integration 1>",
                "<CurriculumIntegration: Integration 2>",
                "<CurriculumIntegration: Integration 3>",
            ]
        )

    def create_test_integration(self, topic, number, lessons=None, curriculum_areas=None):
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
