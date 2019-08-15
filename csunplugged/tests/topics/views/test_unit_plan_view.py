from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class UnitPlanViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_unit_plan_view_with_valid_slugs(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_unit_plan_view_with_invalid_topic_slug(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": "wrong_slug",
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_unit_plan_view_with_invalid_unit_plan_slug(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": "wrong_slug",
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_unit_plan_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

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


        #TODO remove this selenium test after check.
        CAPABILITIES = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'Chrome',
            'browser_version': '60.0',
            'resolution': '1920x1080',
            'browserstack.local': 'true'
        }
        from selenium import webdriver
        from ..in_browser import helpers
        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=CAPABILITIES)

        driver.get("{}resources/".format(helpers.BASE_URL))
        element = driver.title
        if "Printables" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=CAPABILITIES)

        driver.get(helpers.BASE_URL)
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

        driver = webdriver.Remote(
            command_executor=helpers.COMMAND_EXECUTOR,
            desired_capabilities=CAPABILITIES)

        driver.get("127.0.0.1" + url)
        element = driver.title
        if "CS Unplugged" not in element:
            raise Exception("Unable to load local page!")
        driver.quit()

        response = self.client.get(url)
        print("VALUES TO FOLLOW")
        print(type(response))
        print(response)
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

    def test_unit_plan_view_lessons_context_order(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        age_group_2 = self.test_data.create_age_group(8, 10)
        lesson1 = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_2
        )
        lesson2 = self.test_data.create_lesson(
            topic,
            unit_plan,
            2,
            age_group_1
        )
        lesson3 = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["grouped_lessons"]),
            2
        )

        expected_grouped_lessons = [
            ("<AgeGroup: NumericRange(5, 7, '[)')>", [lesson3, lesson2]),
            ("<AgeGroup: NumericRange(8, 10, '[)')>", [lesson1]),
        ]
        grouped_lessons = response.context["grouped_lessons"]
        i = 0
        for (age_group, lessons) in grouped_lessons.items():
            self.assertEqual(repr(age_group), expected_grouped_lessons[i][0])
            self.assertEqual(
                lessons,
                expected_grouped_lessons[i][1]
            )
            i += 1

    def test_unit_plan_view_templates(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        template_found = False
        for template in response.templates:
            if template.name == "topics/unit-plan.html":
                template_found = True
        self.assertTrue(template_found)
