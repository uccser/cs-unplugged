from http import HTTPStatus
from django.urls import reverse
from django.core import management
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from tests.create_query_string import query_string
from topics.models import Topic, Lesson


class IndexViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    # No query

    def test_search_view_with_no_query_with_index(self):
        self.test_data.create_topic(1)
        self.test_data.create_topic(2)
        self.test_data.create_topic(3)
        management.call_command("rebuild_search_indexes")
        url = reverse("search:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertNotIn("results", response.context)
        self.assertNotIn("query", response.context)

    def test_search_view_with_no_query_with_no_index(self):
        url = reverse("search:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertNotIn("results", response.context)
        self.assertNotIn("query", response.context)

    # Context

    def test_search_view_context_model_data(self):
        management.call_command("rebuild_search_indexes")
        url = reverse("search:index")
        response = self.client.get(url)
        self.assertEqual(
            response.context["models"],
            [
                {
                    "value": "topics.topic",
                    "name": "Topic",
                    "selected": False,
                },
                {
                    "value": "topics.lesson",
                    "name": "Lesson",
                    "selected": False,
                },
                {
                    "value": "resources.resource",
                    "name": "Printable",
                    "selected": False,
                },
                {
                    "value": "general.generalpage",
                    "name": "General Page",
                    "selected": False,
                },
                {
                    "value": "at_home.activity",
                    "name": "At Home Activity",
                    "selected": False,
                },
                {
                    "value": "topics.curriculumintegration",
                    "name": "Curriculum Integration",
                    "selected": False,
                },
                {
                    "value": "classic.classicpage",
                    "name": "Classic CS Unplugged Page",
                    "selected": False,
                },
                {
                    "value": "topics.programmingchallenge",
                    "name": "Programming Challenge",
                    "selected": False,
                },
            ]
        )

    def test_search_view_context_model_data_with_selected(self):
        management.call_command("rebuild_search_indexes")
        url = reverse("search:index")
        get_parameters = [
            ("models", "topics.topic"),
        ]
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(
            response.context["models"],
            [
                {
                    "value": "topics.topic",
                    "name": "Topic",
                    "selected": True,
                },
                {
                    "value": "topics.lesson",
                    "name": "Lesson",
                    "selected": False,
                },
                {
                    "value": "resources.resource",
                    "name": "Printable",
                    "selected": False,
                },
                {
                    "value": "general.generalpage",
                    "name": "General Page",
                    "selected": False,
                },
                {
                    "value": "at_home.activity",
                    "name": "At Home Activity",
                    "selected": False,
                },
                {
                    "value": "topics.curriculumintegration",
                    "name": "Curriculum Integration",
                    "selected": False,
                },
                {
                    "value": "classic.classicpage",
                    "name": "Classic CS Unplugged Page",
                    "selected": False,
                },
                {
                    "value": "topics.programmingchallenge",
                    "name": "Programming Challenge",
                    "selected": False,
                },
            ]
        )

    # def test_search_view_context_curriculum_areas_data(self):
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     area_2 = self.test_data.create_curriculum_area(2)
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     response = self.client.get(url)
    #     self.assertEqual(
    #         response.context["curriculum_areas"],
    #         [
    #             {
    #                 "pk": area_1.pk,
    #                 "name": "Area 1",
    #                 "colour": "colour-1",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "children": []
    #             },
    #             {
    #                 "pk": area_2.pk,
    #                 "name": "Area 2",
    #                 "colour": "colour-2",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "children": []
    #             },
    #         ]
    #     )

    # def test_search_view_context_curriculum_areas_data_with_selected(self):
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     area_2 = self.test_data.create_curriculum_area(2)
    #     area_3 = self.test_data.create_curriculum_area(3)
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     get_parameters = [
    #         ("curriculum_areas", area_1.pk),
    #         ("curriculum_areas", area_3.pk),
    #     ]
    #     url += query_string(get_parameters)
    #     response = self.client.get(url)
    #     self.assertEqual(
    #         response.context["curriculum_areas"],
    #         [
    #             {
    #                 "pk": area_1.pk,
    #                 "name": "Area 1",
    #                 "colour": "colour-1",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "children": [],
    #                 "selected": "true",
    #             },
    #             {
    #                 "pk": area_2.pk,
    #                 "name": "Area 2",
    #                 "colour": "colour-2",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "children": [],
    #             },
    #             {
    #                 "pk": area_3.pk,
    #                 "name": "Area 3",
    #                 "colour": "colour-3",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "children": [],
    #                 "selected": "true",
    #             },
    #         ]
    #     )

    # def test_search_view_context_curriculum_areas_data_with_children(self):
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     area_2 = self.test_data.create_curriculum_area(2)
    #     area_3 = self.test_data.create_curriculum_area(3, parent=area_2)
    #     area_4 = self.test_data.create_curriculum_area(4, parent=area_2)
    #     area_5 = self.test_data.create_curriculum_area(5, parent=area_2)
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     response = self.client.get(url)
    #     self.assertEqual(
    #         response.context["curriculum_areas"],
    #         [
    #             {
    #                 "pk": area_1.pk,
    #                 "name": "Area 1",
    #                 "colour": "colour-1",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "children": []
    #             },
    #             {
    #                 "pk": area_2.pk,
    #                 "name": "Area 2",
    #                 "colour": "colour-2",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "children": [
    #                     {
    #                         "pk": area_3.pk,
    #                         "name": "Area 3",
    #                         "colour": "colour-3",
    #                         "parent__pk": area_2.pk,
    #                         "parent__name": "Area 2",
    #                     },
    #                     {
    #                         "pk": area_4.pk,
    #                         "name": "Area 4",
    #                         "colour": "colour-4",
    #                         "parent__pk": area_2.pk,
    #                         "parent__name": "Area 2",
    #                     },
    #                     {
    #                         "pk": area_5.pk,
    #                         "name": "Area 5",
    #                         "colour": "colour-5",
    #                         "parent__pk": area_2.pk,
    #                         "parent__name": "Area 2",
    #                     },
    #                 ]
    #             },
    #         ]
    #     )

    # def test_search_view_context_curriculum_areas_data_with_children_with_selected(self):
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     area_2 = self.test_data.create_curriculum_area(2)
    #     area_3 = self.test_data.create_curriculum_area(3, parent=area_2)
    #     area_4 = self.test_data.create_curriculum_area(4, parent=area_2)
    #     area_5 = self.test_data.create_curriculum_area(5, parent=area_2)
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     get_parameters = [
    #         ("curriculum_areas", area_1.pk),
    #         ("curriculum_areas", area_2.pk),
    #         ("curriculum_areas", area_3.pk),
    #         ("curriculum_areas", area_5.pk),
    #     ]
    #     url += query_string(get_parameters)
    #     response = self.client.get(url)
    #     self.assertEqual(
    #         response.context["curriculum_areas"],
    #         [
    #             {
    #                 "pk": area_1.pk,
    #                 "name": "Area 1",
    #                 "colour": "colour-1",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "children": [],
    #                 "selected": "true",
    #             },
    #             {
    #                 "pk": area_2.pk,
    #                 "name": "Area 2",
    #                 "colour": "colour-2",
    #                 "parent__pk": None,
    #                 "parent__name": None,
    #                 "selected": "true",
    #                 "children": [
    #                     {
    #                         "pk": area_3.pk,
    #                         "name": "Area 3",
    #                         "colour": "colour-3",
    #                         "parent__pk": area_2.pk,
    #                         "parent__name": "Area 2",
    #                         "selected": "true",
    #                     },
    #                     {
    #                         "pk": area_4.pk,
    #                         "name": "Area 4",
    #                         "colour": "colour-4",
    #                         "parent__pk": area_2.pk,
    #                         "parent__name": "Area 2",
    #                     },
    #                     {
    #                         "pk": area_5.pk,
    #                         "name": "Area 5",
    #                         "colour": "colour-5",
    #                         "parent__pk": area_2.pk,
    #                         "parent__name": "Area 2",
    #                         "selected": "true",
    #                     },
    #                 ]
    #             },
    #         ]
    #     )

    # TODO: Test is broken as query text provides zero matches
    # def test_search_view_context_lesson_data(self):
    #     topic = self.test_data.create_topic(1)
    #     age_group = self.test_data.create_age_group(5, 7)
    #     lesson = self.test_data.create_lesson(
    #         topic,
    #         1,
    #         age_group
    #     )
    #     learning_outcome1 = self.test_data.create_learning_outcome(1)
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     learning_outcome1.curriculum_areas.add(area_1)
    #     lesson.learning_outcomes.add(learning_outcome1)
    #     learning_outcome2 = self.test_data.create_learning_outcome(2)
    #     area_2 = self.test_data.create_curriculum_area(2)
    #     learning_outcome2.curriculum_areas.add(area_2)
    #     area_3 = self.test_data.create_curriculum_area(3)
    #     learning_outcome2.curriculum_areas.add(area_3)
    #     lesson.learning_outcomes.add(learning_outcome2)
    #     self.test_data.create_curriculum_area(4)
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     get_parameters = [("q", lesson.name)]
    #     url += query_string(get_parameters)
    #     response = self.client.get(url)
    #     result_lesson = response.context["results"][0]
    #     self.assertEqual(
    #         result_lesson.lesson_ages,
    #         [
    #             {
    #                 "lower": 5,
    #                 "upper": 7,
    #                 "number": 1,
    #             },
    #         ]
    #     )
    #     self.assertQuerysetEqual(
    #         result_lesson.curriculum_areas,
    #         [
    #             "<CurriculumArea: Area 1>",
    #             "<CurriculumArea: Area 2>",
    #             "<CurriculumArea: Area 3>",
    #         ]
    #     )

    # With query

    def test_search_view_all_items(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_topic(2)
        self.test_data.create_topic(3)
        age_group = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            1,
            age_group
        )
        management.call_command("rebuild_search_indexes")
        url = reverse("search:index")
        get_parameters = [("q", "")]
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(len(response.context["results"]), 4)

    def test_search_view_assert_order(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_topic(2)
        age_group = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            1,
            age_group
        )
        management.call_command("rebuild_search_indexes")
        url = reverse("search:index")
        get_parameters = [("q", "")]
        url += query_string(get_parameters)
        response = self.client.get(url)
        result_objects = response.context["results"]
        self.assertIsInstance(result_objects[0], Topic)
        self.assertIsInstance(result_objects[1], Topic)
        self.assertIsInstance(result_objects[2], Lesson)

    def test_search_view_model_filter(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_topic(2)
        age_group = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            1,
            age_group
        )
        management.call_command("rebuild_search_indexes")
        url = reverse("search:index")
        get_parameters = [
            ("models", "topics.topic"),
        ]
        url += query_string(get_parameters)
        response = self.client.get(url)
        result_objects = response.context["results"]
        self.assertEqual(len(result_objects), 2)
        self.assertIsInstance(result_objects[0], Topic)
        self.assertIsInstance(result_objects[1], Topic)

    def test_search_view_model_filter_multiple(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_topic(2)
        age_group = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            1,
            age_group
        )
        management.call_command("rebuild_search_indexes")
        url = reverse("search:index")
        get_parameters = [
            ("models", "topics.topic"),
        ]
        url += query_string(get_parameters)
        response = self.client.get(url)
        result_objects = response.context["results"]
        self.assertEqual(len(result_objects), 2)
        self.assertIsInstance(result_objects[0], Topic)
        self.assertIsInstance(result_objects[1], Topic)

    # TODO: Test is broken as query text provides zero matches
    # def test_search_view_model_filter_multiple_with_query(self):
    #     topic = self.test_data.create_topic(1)
    #     self.test_data.create_topic(2)
    #     age_group = self.test_data.create_age_group(5, 7)
    #     self.test_data.create_lesson(
    #         topic,
    #         1,
    #         age_group
    #     )
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     get_parameters = [
    #         ("q", "Unit Plan 1"),
    #         ("models", "topics.topic"),
    #     ]
    #     url += query_string(get_parameters)
    #     response = self.client.get(url)
    #     result_objects = response.context["results"]

    # def test_search_view_curriculum_areas_filter_1(self):
    #     topic = self.test_data.create_topic(1)
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     self.test_data.create_integration(topic, 1, curriculum_areas=[area_1])
    #     area_2 = self.test_data.create_curriculum_area(2)
    #     self.test_data.create_integration(topic, 2, curriculum_areas=[area_1, area_2])
    #     self.test_data.create_integration(topic, 3)
    #     self.test_data.create_integration(topic, 4)
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     get_parameters = [
    #         ("curriculum_areas", area_1.pk),
    #     ]
    #     url += query_string(get_parameters)
    #     response = self.client.get(url)
    #     result_objects = response.context["results"]
    #     self.assertEqual(len(result_objects), 2)

    # def test_search_view_curriculum_areas_filter_2(self):
    #     topic = self.test_data.create_topic(1)
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     self.test_data.create_integration(topic, 1, curriculum_areas=[area_1])
    #     area_2 = self.test_data.create_curriculum_area(2)
    #     self.test_data.create_integration(topic, 2, curriculum_areas=[area_1, area_2])
    #     self.test_data.create_integration(topic, 3)
    #     self.test_data.create_integration(topic, 4)
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     get_parameters = [
    #         ("curriculum_areas", area_2.pk),
    #     ]
    #     url += query_string(get_parameters)
    #     response = self.client.get(url)
    #     result_objects = response.context["results"]
    #     self.assertEqual(len(result_objects), 1)

    # def test_search_view_curriculum_areas_filter_parent_no_results(self):
    #     # This search is not accessible to user, but
    #     # checks indexes are created without including parent.
    #     topic = self.test_data.create_topic(1)
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     area_2 = self.test_data.create_curriculum_area(2, parent=area_1)
    #     self.test_data.create_integration(topic, 1, curriculum_areas=[area_2])

    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     get_parameters = [
    #         ("curriculum_areas", area_1.pk),
    #     ]
    #     url += query_string(get_parameters)
    #     response = self.client.get(url)
    #     self.assertFalse(response.context["results"])

    # def test_search_view_curriculum_areas_filter_with_query(self):
    #     topic = self.test_data.create_topic(1)
    #     area_1 = self.test_data.create_curriculum_area(1)
    #     self.test_data.create_integration(topic, 1, curriculum_areas=[area_1])
    #     area_2 = self.test_data.create_curriculum_area(2)
    #     self.test_data.create_integration(topic, 2, curriculum_areas=[area_1, area_2])
    #     self.test_data.create_integration(topic, 3)
    #     self.test_data.create_integration(topic, 4)
    #     management.call_command("rebuild_search_indexes")
    #     url = reverse("search:index")
    #     get_parameters = [
    #         ("q", "Integration"),
    #         ("curriculum_areas", area_2.pk),
    #     ]
    #     url += query_string(get_parameters)
    #     response = self.client.get(url)
    #     result_objects = response.context["results"]
    #     self.assertEqual(len(result_objects), 1)
    #     self.assertEqual(result_objects[0].object.name, "Integration 2")
