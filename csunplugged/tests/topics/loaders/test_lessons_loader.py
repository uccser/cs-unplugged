import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from topics.models import Lesson
from topics.management.commands._LessonsLoader import LessonsLoader
from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.EmptyConfigFileError import EmptyConfigFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.NoHeadingFoundInMarkdownFileError import NoHeadingFoundInMarkdownFileError
from utils.errors.InvalidConfigValueError import InvalidConfigValueError


class LessonsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.resource_test_data = ResourcesTestDataGenerator()
        self.loader_name = "lessons"

    def test_basic_lesson_loader_configuration(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
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

    def test_lesson_loader_topic_set_correctly(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
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

    # Note: Missing topic does not need to be tested as the topic loader
    #       is a parent loader to the lesson loader. Therefore this loader,
    #       is not run if the topic cannot be found.

    def test_lesson_loader_unit_plan_set_correctly(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
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

    # Note: Missing unit plan does not need to be tested as the unit plan loader
    #       is a parent loader to the lesson loader. Therefore this loader,
    #       is not run if the unit plan cannot be found.

    def test_lesson_loader_slug_set_correctly(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
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

    # Note: Missing slug cannot be tested as this is parsed in the unit plan
    #       loader.

    def test_lesson_loader_name_set_correctly(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
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

    def test_lesson_loader_missing_name_text(self):
        config_file = os.path.join(self.loader_name, "missing-title.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            NoHeadingFoundInMarkdownFileError,
            lesson_loader.load,
        )

    def test_lesson_loader_content_set_correctly(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").content,
            "<p>Etiam in massa. Nam ut metus. In rhoncus venenatis tellus.</p>",
        )

    def test_lesson_loader_missing_content_text(self):
        config_file = os.path.join(self.loader_name, "missing-content.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            EmptyMarkdownFileError,
            lesson_loader.load,
        )

    def test_lesson_loader_valid_computational_thinking_content(self):
        config_file = os.path.join(self.loader_name, "ct-links.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="ct-links").computational_thinking_links,
            "<p>Example text for Computational Thinking links.</p>",
        )

    def test_lesson_loader_missing_computational_thinking_content(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertIsNone(Lesson.objects.get(slug="lesson-1").computational_thinking_links)

    def test_lesson_loader_duration_set_correctly(self):
        config_file = os.path.join(self.loader_name, "duration.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
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

    def test_lesson_loader_heading_tree_set_correctly(self):
        config_file = os.path.join(self.loader_name, "heading-tree.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
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

    def test_lesson_loader_no_heading_tree(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertIsNone(Lesson.objects.get(slug="lesson-1").heading_tree)

    def test_lesson_loader_optional_programming_challenges_set_correctly(self):
        config_file = os.path.join(self.loader_name, "programming-challenges.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        difficulty = self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge(topic, 2, difficulty)

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").programming_challenges.all(),
            [
                "<ProgrammingChallenge: Challenge 1.1: 1>",
                "<ProgrammingChallenge: Challenge 1.1: 2>",
            ],
            ordered=False,
        )

    def test_lesson_loader_optional_programming_challenges_empty(self):
        config_file = os.path.join(self.loader_name, "programming-challenges-empty.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()

    def test_lesson_loader_optional_programming_challenges_invalid_slug(self):
        config_file = os.path.join(self.loader_name, "programming-challenges-invalid.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            KeyNotFoundError,
            lesson_loader.load,
        )

    def test_lesson_loader_optional_programming_challenges_set_correctly_when_omitted(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        difficulty = self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge(topic, 2, difficulty)

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").programming_challenges.all(),
            [],
        )

    def test_lesson_loader_valid_programming_challenges_description(self):
        config_file = os.path.join(self.loader_name, "programming-challenges-description.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="programming-challenges-description").programming_challenges_description,
            "<p>Description of lesson programming challenges.</p>",
        )

    def test_lesson_loader_missing_programming_challenges_description(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertIsNone(Lesson.objects.get(slug="lesson-1").programming_challenges_description)

    def test_lesson_loader_optional_learning_outcomes_set_correctly(self):
        config_file = os.path.join(self.loader_name, "learning-outcomes.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.test_data.create_learning_outcome(1)
        self.test_data.create_learning_outcome(2)

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").learning_outcomes.all(),
            [
                "<LearningOutcome: Outcome 1>",
                "<LearningOutcome: Outcome 2>",
            ],
            ordered=False,
        )

    def test_lesson_loader_optional_learning_outcomes_invalid(self):
        config_file = os.path.join(self.loader_name, "learning-outcomes.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.test_data.create_learning_outcome(1)

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            KeyNotFoundError,
            lesson_loader.load
        )

    def test_lesson_loader_optional_learning_outcomes_empty(self):
        config_file = os.path.join(self.loader_name, "learning-outcomes-empty.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()

    def test_lesson_loader_optional_learning_outcomes_set_correctly_when_omitted(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.test_data.create_learning_outcome(1)
        self.test_data.create_learning_outcome(2)

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").learning_outcomes.all(),
            [],
        )

    def test_lesson_loader_optional_classroom_resources_set_correctly_when_omitted(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertEqual(
            Lesson.objects.get(slug="lesson-1").classroom_resources,
            None,
        )

    def test_lesson_loader_multiple_lessons(self):
        config_file = os.path.join(self.loader_name, "multiple-lessons.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.all(),
            [
                "<Lesson: Lesson 1>",
                "<Lesson: Lesson 2>",
                "<Lesson: Lesson 3>",
            ],
            ordered=False,
        )

    def test_lessons_loader_missing_configuration_file(self):
        config_file = os.path.join(self.loader_name, "missing.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            CouldNotFindConfigFileError,
            lesson_loader.load,
        )

    def test_lessons_loader_empty_configuration_file(self):
        config_file = os.path.join(self.loader_name, "empty.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            EmptyConfigFileError,
            lesson_loader.load,
        )

    def test_lessons_loader_missing_lesson_data(self):
        config_file = os.path.join(self.loader_name, "missing-lesson-data.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load,
        )

    def test_lesson_loader_optional_generated_resources_set_correctly(self):
        config_file = os.path.join(self.loader_name, "generated-resources.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)

        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.resource_test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        self.resource_test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").generated_resources.order_by("name"),
            [
                "<Resource: Resource Arrows>",
                "<Resource: Resource Grid>",
            ],
        )

    def test_lesson_loader_optional_generated_resources_empty(self):
        config_file = os.path.join(self.loader_name, "generated-resources-empty.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()
        lesson = Lesson.objects.get(slug="lesson-1")
        self.assertFalse(lesson.generated_resources.exists())

    def test_lesson_loader_optional_generated_resources_slug_empty(self):
        config_file = os.path.join(self.loader_name, "generated-resources-slug-empty.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load
        )

    def test_lesson_loader_optional_generated_resources_slug_invalid(self):
        config_file = os.path.join(self.loader_name, "generated-resources.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            KeyNotFoundError,
            lesson_loader.load
        )

    def test_lesson_loader_optional_generated_resources_slug_description_empty(self):
        config_file = os.path.join(self.loader_name, "generated-resources-description-empty.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.resource_test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load
        )

    def test_lesson_loader_no_classroom_resources(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()

    def test_lesson_loader_empty_classroom_resources(self):
        config_file = os.path.join(self.loader_name, "empty-classroom-resources.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()

    def test_lesson_loader_invalid_classroom_resources(self):
        config_file = os.path.join(self.loader_name, "invalid-classroom-resources.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            InvalidConfigValueError,
            lesson_loader.load
        )

    def test_lesson_loader_invalid_classroom_resources_item(self):
        config_file = os.path.join(self.loader_name, "invalid-classroom-resources-item.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            InvalidConfigValueError,
            lesson_loader.load
        )

    def test_lesson_loader_invalid_classroom_resources_string_too_long(self):
        config_file = os.path.join(self.loader_name, "invalid-classroom-resources-string-too-long.yaml")
        lessons_structure = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        lesson_loader = LessonsLoader(
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        self.assertRaises(
            InvalidConfigValueError,
            lesson_loader.load
        )
