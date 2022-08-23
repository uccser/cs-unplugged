from http import HTTPStatus
from django.test import tag, override_settings
from django.urls import reverse
from django.utils import translation
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import ResourceDescription
from collections import OrderedDict


@tag("resource")
class ResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_resource_view_with_valid_slug(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_resource_view_with_invalid_slug(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        kwargs = {
            "resource_slug": "wrong_slug",
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_resource_view_context(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["resource"],
            resource
        )
        self.assertFalse(response.context["debug"])
        self.assertFalse(response.context["grouped_lessons"])

    @override_settings(DEPLOYED=True)
    def test_resource_view_resource_thumbnail_base_context_production_en(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["resource_thumbnail_base"],
            "/static/img/resources/grid/thumbnails/{}/".format(self.language)
        )

    @override_settings(DEPLOYED=True)
    def test_resource_view_resource_thumbnail_base_context_production_de(self):
        with translation.override("de"):
            resource = self.test_data.create_resource(
                "grid",
                "Grid",
                "resources/grid.html",
                "GridResourceGenerator",
            )
            kwargs = {
                "resource_slug": resource.slug,
            }
            url = reverse("resources:resource", kwargs=kwargs)
            response = self.client.get(url)
            self.assertEqual(
                response.context["resource_thumbnail_base"],
                "/static/img/resources/grid/thumbnails/de/"
            )

    def test_resource_view_lesson_context(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )

        # Create topic data
        topic_test_data = TopicsTestDataGenerator()
        topic = topic_test_data.create_topic(1)
        age_group_1 = topic_test_data.create_age_group(5, 7)
        age_group_2 = topic_test_data.create_age_group(8, 10)
        lesson1 = topic_test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        lesson2 = topic_test_data.create_lesson(
            topic,
            2,
            age_group_1
        )
        lesson3 = topic_test_data.create_lesson(
            topic,
            1,
            age_group_2
        )

        # Create relationships
        relationship1 = ResourceDescription(
            resource=resource,
            lesson=lesson1,
            description="Description between resource and lesson1."
        )
        relationship1.save()
        relationship2 = ResourceDescription(
            resource=resource,
            lesson=lesson2,
            description="Description between resource and lesson2."
        )
        relationship2.save()
        relationship3 = ResourceDescription(
            resource=resource,
            lesson=lesson3,
            description="Description between resource and lesson3."
        )
        relationship3.save()

        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["grouped_lessons"],
            OrderedDict([(age_group_1, [lesson1, lesson2]), (age_group_2, [lesson3])])
        )
