import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from topics.models import Lesson
from topics.management.commands._LessonsLoader import LessonsLoader
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.EmptyYAMLFileError import EmptyYAMLFileError
from django.utils import translation
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.NoHeadingFoundInMarkdownFileError import NoHeadingFoundInMarkdownFileError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError


class LessonsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.resource_test_data = ResourcesTestDataGenerator()
        self.loader_name = "lessons"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, "lessons")

    def test_basic_lesson_loader_configuration(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()

        self.assertQuerysetEqual(
            Lesson.objects.all(),
            ["<Lesson: Lesson 1>"]
        )

    def test_lesson_loader_topic_set_correctly(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").topic,
            topic,
        )

    # Note: Missing topic does not need to be tested as the topic loader
    #       is a parent loader to the lesson loader. Therefore this loader,
    #       is not run if the topic cannot be found.

    def test_lesson_loader_slug_set_correctly(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").slug,
            "lesson-1",
        )

    # Note: Missing slug cannot be tested as this is parsed in the unit plan
    #       loader.

    def test_lesson_loader_name_set_correctly(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").name,
            "Lesson 1",
        )

    def test_lesson_loader_missing_name_text(self):
        config_file = "missing-title.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            NoHeadingFoundInMarkdownFileError,
            lesson_loader.load,
        )

    def test_lesson_loader_content_set_correctly(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-1").content,
            "<p>Etiam in massa. Nam ut metus. In rhoncus venenatis tellus.</p>",
        )

    def test_lesson_loader_missing_content_text(self):
        config_file = "missing-content.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            EmptyMarkdownFileError,
            lesson_loader.load,
        )

    def test_lesson_loader_valid_computational_thinking_content(self):
        config_file = "ct-links.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="ct-links").computational_thinking_links,
            "<p>Example text for Computational Thinking links.</p>",
        )

    def test_lesson_loader_missing_computational_thinking_content(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEqual("", Lesson.objects.get(slug="lesson-1").computational_thinking_links)

    def test_lesson_loader_duration_set_correctly(self):
        config_file = "duration.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
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
        config_file = "heading-tree.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="lesson-2").heading_tree,
            [
                {
                    "level": 2,
                    "text": "Heading 2",
                    "slug": "heading-2",
                    "children": [
                        {
                            "level": 3,
                            "text": "Heading 3",
                            "slug": "heading-3",
                            "children": [],
                        }
                    ],
                },
                {
                    "level": 2,
                    "text": "Heading 4",
                    "slug": "heading-4",
                    "children": [],
                }
            ],
        )

    def test_lesson_loader_no_heading_tree(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        # Empty dict will evaluate to false
        self.assertFalse(Lesson.objects.get(slug="lesson-1").heading_tree)

    def test_lesson_loader_optional_programming_challenges_set_correctly(self):
        config_file = "programming-challenges.yaml"

        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge(topic, 2, difficulty)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
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
        config_file = "programming-challenges-empty.yaml"
        topic = self.test_data.create_topic(1)
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()

    def test_lesson_loader_optional_programming_challenges_invalid_slug(self):
        config_file = "programming-challenges-invalid.yaml"

        topic = self.test_data.create_topic(1)
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            KeyNotFoundError,
            lesson_loader.load,
        )

    def test_lesson_loader_optional_programming_challenges_set_correctly_when_omitted(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge(topic, 2, difficulty)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").programming_challenges.all(),
            [],
        )

    def test_lesson_loader_valid_programming_challenges_description(self):
        config_file = "programming-challenges-description.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug="programming-challenges-description").programming_challenges_description,
            "<p>Description of lesson programming challenges.</p>",
        )

    def test_lesson_loader_missing_programming_challenges_description(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEqual("", Lesson.objects.get(slug="lesson-1").programming_challenges_description)

    def test_lesson_loader_optional_learning_outcomes_set_correctly(self):
        config_file = "learning-outcomes.yaml"

        topic = self.test_data.create_topic(1)
        self.test_data.create_learning_outcome(1)
        self.test_data.create_learning_outcome(2)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
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
        config_file = "learning-outcomes.yaml"

        topic = self.test_data.create_topic(1)
        self.test_data.create_learning_outcome(1)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            KeyNotFoundError,
            lesson_loader.load
        )

    def test_lesson_loader_optional_learning_outcomes_empty(self):
        config_file = "learning-outcomes-empty.yaml"

        topic = self.test_data.create_topic(1)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            InvalidYAMLValueError,
            lesson_loader.load
        )

    def test_lesson_loader_optional_learning_outcomes_set_correctly_when_omitted(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic(1)
        self.test_data.create_learning_outcome(1)
        self.test_data.create_learning_outcome(2)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").learning_outcomes.all(),
            [],
        )

    def test_lesson_loader_optional_classroom_resources_set_correctly(self):
        config_file = "classroom-resources.yaml"

        topic = self.test_data.create_topic(1)
        self.test_data.create_classroom_resource(1)
        self.test_data.create_classroom_resource(2)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").classroom_resources.all(),
            [
                "<ClassroomResource: Resource 1>",
                "<ClassroomResource: Resource 2>",
            ],
            ordered=False,
        )

    def test_lesson_loader_optional_classroom_resources_invalid(self):
        config_file = "classroom-resources.yaml"

        topic = self.test_data.create_topic(1)
        self.test_data.create_classroom_resource(1)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            KeyNotFoundError,
            lesson_loader.load
        )

    def test_lesson_loader_optional_classroom_resources_empty(self):
        config_file = "classroom-resources-empty.yaml"

        topic = self.test_data.create_topic(1)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertFalse(
            Lesson.objects.get(slug="lesson-1").classroom_resources.exists()
        )

    def test_lesson_loader_optional_classroom_resources_set_correctly_when_omitted(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic(1)

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").classroom_resources.all(),
            [],
        )

    def test_lesson_loader_multiple_lessons(self):
        config_file = "multiple-lessons.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
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
        config_file = "missing.yaml"
        topic = self.test_data.create_topic("1")
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            CouldNotFindYAMLFileError,
            lesson_loader.load,
        )

    def test_lessons_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        topic = self.test_data.create_topic("1")
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            EmptyYAMLFileError,
            lesson_loader.load,
        )

    def test_lessons_loader_missing_lesson_data(self):
        config_file = "missing-lesson-data.yaml"
        topic = self.test_data.create_topic("1")
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load,
        )

    def test_lesson_loader_optional_generated_resources_set_correctly(self):
        config_file = "generated-resources.yaml"

        topic = self.test_data.create_topic(1)
        self.resource_test_data.create_resource(
            "grid",
            "Grid",
            "Grid description",
            "GridResourceGenerator",
        )
        self.resource_test_data.create_resource(
            "arrows",
            "Arrows",
            "Arrows description",
            "ArrowsResourceGenerator",
        )
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.get(slug="lesson-1").generated_resources.order_by("name"),
            [
                "<Resource: Arrows>",
                "<Resource: Grid>",
            ],
        )

    def test_lesson_loader_optional_generated_resources_empty(self):
        config_file = "generated-resources-empty.yaml"
        topic = self.test_data.create_topic(1)
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        lesson = Lesson.objects.get(slug="lesson-1")
        self.assertFalse(lesson.generated_resources.exists())

    def test_lesson_loader_optional_generated_resources_description_empty(self):
        config_file = "generated-resources-description-empty.yaml"
        topic = self.test_data.create_topic(1)
        self.resource_test_data.create_resource(
            "grid",
            "Grid",
            "Grid description",
            "GridResourceGenerator",
        )
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            InvalidYAMLValueError,
            lesson_loader.load
        )

    def test_lesson_loader_optional_generated_resources_description_missing(self):
        config_file = "generated-resources-description-missing.yaml"
        topic = self.test_data.create_topic(1)
        self.resource_test_data.create_resource(
            "grid",
            "Grid",
            "Grid description",
            "GridResourceGenerator",
        )
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()

    def test_lesson_loader_optional_generated_resources_slug_invalid(self):
        config_file = "generated-resources.yaml"
        topic = self.test_data.create_topic(1)
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        self.assertRaises(
            KeyNotFoundError,
            lesson_loader.load
        )

    def test_lessons_loader_translation_basic(self):
        config_file = "basic-translation.yaml"
        topic = self.test_data.create_topic("1")
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        lesson = Lesson.objects.get(slug="lesson-basic-translation")
        self.assertSetEqual(set(["en", "de"]), set(lesson.languages))
        self.assertEqual(lesson.name, "Basic Translated Lesson English")
        self.assertIn("English lesson content", lesson.content)
        with translation.override("de"):
            self.assertEqual(lesson.name, "Basic Translated Lesson German")
            self.assertIn("German lesson content", lesson.content)

    def test_lessons_loader_translation_complex(self):
        config_file = "complex-translation.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()

        lesson = Lesson.objects.get(slug="lesson-complex-translation")

        self.assertSetEqual(set(["en", "de"]), set(lesson.languages))

        self.assertEqual(lesson.name, "Complex Translated Lesson English")
        self.assertIn("English lesson content", lesson.content)
        self.assertIn("Another English header", str(lesson.heading_tree))
        self.assertIn(
            "English text for Computational Thinking links.",
            lesson.computational_thinking_links
        )
        self.assertIn(
            "English description of lesson programming challenges.",
            lesson.programming_challenges_description
        )

        with translation.override("de"):
            self.assertEqual(lesson.name, "Complex Translated Lesson German")
            self.assertIn("German lesson content", lesson.content)
            self.assertIn("Another German header", str(lesson.heading_tree))
            self.assertIn(
                "German text for Computational Thinking links.",
                lesson.computational_thinking_links
            )
            self.assertIn(
                "German description of lesson programming challenges.",
                lesson.programming_challenges_description
            )

    def test_lessons_loader_translation_missing_lesson_file(self):
        config_file = "basic-config.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        lesson = Lesson.objects.get(slug="lesson-1")

        # 'de' should not be stored as available language
        self.assertSetEqual(set(["en"]), set(lesson.languages))

    def test_lessons_loader_translation_missing_ct_links(self):
        config_file = "translation-missing-ct-links.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        lesson = Lesson.objects.get(slug="lesson-complex-translation")

        self.assertEqual(lesson.name, "Complex Translated Lesson English")
        self.assertIn(
            "English text for Computational Thinking links.",
            lesson.computational_thinking_links
        )

        # 'de' should still be an available language as ct_links is optional
        self.assertIn("de", lesson.languages)
        with translation.override("de"):
            self.assertEqual(lesson.name, "Complex Translated Lesson German")
            # accessing the untranslated field should not default back to english
            self.assertEqual("", lesson.computational_thinking_links)

    def test_lessons_loader_translation_missing_programming_challenges(self):
        config_file = "translation-missing-pcd.yaml"

        topic = self.test_data.create_topic("1")

        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        lesson = Lesson.objects.get(slug="lesson-complex-translation")

        self.assertEqual(lesson.name, "Complex Translated Lesson English")
        self.assertIn(
            "English description of lesson programming challenges.",
            lesson.programming_challenges_description
        )

        # 'de' should still be an available language as programming challenge description is optional
        self.assertIn("de", lesson.languages)
        with translation.override("de"):
            self.assertEqual(lesson.name, "Complex Translated Lesson German")
            # accessing the untranslated field should not default back to english
            self.assertEqual("", lesson.programming_challenges_description)

    def test_lessons_loader_insert_start(self):
        config_file = "multiple-lessons.yaml"
        topic = self.test_data.create_topic("1")
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        
        lesson_objects = Lesson.objects.all()
        self.assertQuerysetEqual(
            list(lesson_objects),
            [
                "<Lesson: Lesson 1>",
                "<Lesson: Lesson 2>",
                "<Lesson: Lesson 3>",
            ]
        )

        config_file = "insert-start.yaml"
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()

        lesson_objects = Lesson.objects.all()
        self.assertQuerysetEqual(
            list(lesson_objects),
            [
                "<Lesson: Lesson 0>",
                "<Lesson: Lesson 1>",
                "<Lesson: Lesson 2>",
                "<Lesson: Lesson 3>",
            ],
        )

    def test_lessons_loader_delete_start(self):
        config_file = "insert-start.yaml"
        topic = self.test_data.create_topic("1")
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()

        lesson_objects = Lesson.objects.all()
        self.assertQuerysetEqual(
            list(lesson_objects),
            [
                "<Lesson: Lesson 0>",
                "<Lesson: Lesson 1>",
                "<Lesson: Lesson 2>",
                "<Lesson: Lesson 3>",
            ],
        )
        
        config_file = "multiple-lessons.yaml"
        lesson_loader = LessonsLoader(
            topic,
            structure_filename=config_file,
            base_path=self.base_path
        )
        lesson_loader.load()
        
        lesson_objects = Lesson.objects.all()
        self.assertQuerysetEqual(
            list(lesson_objects),
            [
                "<Lesson: Lesson 1>",
                "<Lesson: Lesson 2>",
                "<Lesson: Lesson 3>",
            ]
        )
