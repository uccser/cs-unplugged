import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import Lesson
from topics.management.commands._LessonsLoader import LessonsLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class LessonsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_log = Mock()
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "lessons"

    def test_basic_config(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()

        self.assertQuerysetEqual(
            Lesson.objects.all(),
            ["<Lesson: Lesson 1>"]
        )

    def test_min_age(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").min_age,
            1,
        )

    def test_max_age(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").max_age,
            99,
        )

    def test_number(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").number,
            1,
        )

    def test_topic(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").topic,
            topic,
        )

    def test_unit_plan(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").unit_plan,
            unit_plan,
        )

    def test_slug(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").slug,
            "lesson-1",
        )

    def test_name(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").name,
            "Lesson 1",
        )

    def test_duration(self):
        config_file = os.path.join(self.loader_name, "duration.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()

        self.assertQuerysetEqual(
            Lesson.objects.all(),
            ["<Lesson: Lesson 1>"]
        )
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").duration,
            60,
        )

    def test_heading_tree(self):
        config_file = os.path.join(self.loader_name, "heading-tree.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-2").heading_tree,
            [
                {
                    'level': 2,
                    'text': 'Heading 2',
                    'slug': 'heading-2',
                    'children': [
                        {
                            'level': 3,
                            'text': 'Heading 3',
                            'slug': 'heading-3',
                            'children': [],
                        }
                    ],
                },
                {
                    'level': 2,
                    'text': 'Heading 4',
                    'slug': 'heading-4',
                    'children': [],
                }
            ],
        )

    def test_missing_min_age_value(self):
        config_file = os.path.join(self.loader_name, "missing-min-age.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load,
        )

    def test_missing_max_age_value(self):
        config_file = os.path.join(self.loader_name, "missing-max-age.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load,
        )

    def test_missing_number_value(self):
        config_file = os.path.join(self.loader_name, "missing-number.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load,
        )
