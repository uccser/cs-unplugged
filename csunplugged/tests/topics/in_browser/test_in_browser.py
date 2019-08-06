import unittest

from django.test import tag
from selenium import webdriver

from . import helpers

from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


@tag("browser")
class BrowserTest(unittest.TestCase):
    """ Test cases for the in_browser test suite"""

    def test_local_2(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        driver.get("{}resources/".format(helpers.BASE_URL))
        element = driver.title
        if "Printables" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

    def test_local(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        driver.get(helpers.BASE_URL)
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

    def test_local_dup(self):
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        driver.get(helpers.BASE_URL)
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()


@tag("browser")
class UnitPlanViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_unit_plan_view_lessons_context(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson1 = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        lesson2 = self.test_data.create_lesson(
            topic,
            unit_plan,
            2,
            age_group_1
        )
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)

        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=helpers.CAPABILITIES)

        driver.get("http://localhost/" + url)
        driver.quit()

        response = self.client.get(url)
        self.assertEqual(
            len(response.context["grouped_lessons"]),
            1
        )
        grouped_lessons = response.context["grouped_lessons"]
        for (age_group, lessons) in grouped_lessons.items():
            self.assertEqual(repr(age_group), "<AgeGroup: NumericRange(5, 7, '[)')>")
            self.assertEqual(
                lessons,
                [lesson1, lesson2]
            )