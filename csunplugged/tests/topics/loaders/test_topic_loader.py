import os.path
from unittest.mock import Mock
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import Topic
from topics.management.commands._TopicLoader import TopicLoader
from django.utils import translation
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.NoHeadingFoundInMarkdownFileError import NoHeadingFoundInMarkdownFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class TopicLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "topic"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_topic_loader_configuration(self):
        content_path, structure_filename = "topic-1", "topic-1.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        topic_loader.load()
        # Delete temp topic after loader is run
        temp_topic.delete()
        self.assertQuerysetEqual(
            Topic.objects.all(),
            ["<Topic: Topic 1>"]
        )
        self.assertSetEqual(set(["en"]), set(Topic.objects.get(slug="topic-1").languages))

    def test_topic_loader_slug(self):
        content_path, structure_filename = "topic-1", "topic-1.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        topic_loader.load()
        self.assertEquals(
            Topic.objects.get(slug="topic-1").slug,
            "topic-1",
        )

    def test_topic_loader_missing_configuration_file(self):
        content_path, structure_filename = "topic-1", "topic-missing.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        self.assertRaises(
            CouldNotFindYAMLFileError,
            topic_loader.load,
        )

    def test_topic_loader_valid_name_text(self):
        content_path, structure_filename = "topic-1", "topic-1.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        topic_loader.load()
        self.assertEquals(
            Topic.objects.get(slug="topic-1").name,
            "Topic 1",
        )

    def test_topic_loader_missing_name_text(self):
        content_path, structure_filename = "topic-missing-name", "topic-missing-name.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        self.assertRaises(
            NoHeadingFoundInMarkdownFileError,
            topic_loader.load,
        )

    def test_topic_loader_valid_content_text(self):
        content_path, structure_filename = "topic-1", "topic-1.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        topic_loader.load()
        self.assertEquals(
            Topic.objects.get(slug="topic-1").content,
            "<p>Etiam in massa. Nam ut metus. In rhoncus venenatis tellus.</p>",
        )

    def test_topic_loader_missing_content_text(self):
        content_path, structure_filename = "topic-missing-content", "topic-missing-content.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        self.assertRaises(
            EmptyMarkdownFileError,
            topic_loader.load,
        )

    def test_topic_loader_missing_lessons(self):
        content_path, structure_filename = "topic-missing-lessons", "topic-missing-lessons.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        self.assertRaises(
            MissingRequiredFieldError,
            topic_loader.load,
        )

    def test_topic_loader_valid_icon(self):
        content_path, structure_filename = "topic-valid-icon", "topic-valid-icon.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        topic_loader.load()
        self.assertEquals(
            Topic.objects.get(slug="topic-valid-icon").icon,
            "img/logo.png",
        )

    def test_topic_loader_missing_icon(self):
        content_path, structure_filename = "topic-1", "topic-1.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        # Passes if loader throws no exception
        topic_loader.load()

    def test_topic_loader_with_other_resources(self):
        content_path, structure_filename = "topic-with-other-resources", "topic-with-other-resources.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        # Passes if loader throws no exception
        topic_loader.load()
        topic = Topic.objects.get(slug="topic-with-other-resources")
        self.assertIn("Other resources content.", topic.other_resources)

    def test_topic_translation(self):
        content_path, structure_filename = "topic-translation", "topic-translation.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        # Passes if loader throws no exception
        topic_loader.load()
        topic = Topic.objects.get(slug="topic-translation")

        self.assertSetEqual(set(["en", "de"]), set(topic.languages))

        self.assertEqual("English Heading", topic.name)
        self.assertIn("English topic content", topic.content)
        self.assertIn("English other resources content.", topic.other_resources)

        with translation.override("de"):
            self.assertEqual("German Heading", topic.name)
            self.assertIn("German topic content", topic.content)
            self.assertIn("German other resources content.", topic.other_resources)

    def test_topic_translation_other_resources_missing(self):
        content_path = "topic-translation-other-resources-missing"
        structure_filename = "topic-translation-other-resources-missing.yaml"
        factory = Mock()

        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)

        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        # Passes if loader throws no exception
        topic_loader.load()
        topic = Topic.objects.get(slug="topic-translation-other-resources-missing")

        # 'de' should still be an available language as other_resources is optional
        self.assertSetEqual(set(["en", "de"]), set(topic.languages))
        self.assertIn("English other resources content.", topic.other_resources)
        with translation.override("de"):
            # accessing the untranslated field should not default back to english
            self.assertEqual("", topic.other_resources)

    def test_topic_loader_empty_icon(self):
        content_path = "empty-icon"
        structure_filename = "empty-icon.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        topic_loader.load()
        topic = Topic.objects.get(slug="empty-icon")
        self.assertIsNone(topic.icon)

    def test_topic_loader_other_resources_empty(self):
        content_path = "empty-other-resources"
        structure_filename = "empty-other-resources.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        topic_loader.load()
        topic = Topic.objects.get(slug="empty-other-resources")
        self.assertEqual(topic.other_resources, "")

    def test_topic_loader_programming_challenges_empty(self):
        content_path = "empty-programming-challenges"
        structure_filename = "empty-programming-challenges.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        # Passes if loader throws no exception
        topic_loader.load()

    def test_topic_loader_curriculum_integrations_empty(self):
        content_path = "empty-curriculum-integrations"
        structure_filename = "empty-curriculum-integrations.yaml"
        factory = Mock()
        # Create data as other loaders are mocked
        self.test_data.create_age_group(5, 12)
        temp_topic = self.test_data.create_topic("test")
        self.test_data.create_lesson(temp_topic, 1)
        topic_loader = TopicLoader(
            factory,
            content_path=content_path,
            base_path=self.base_path,
            structure_filename=structure_filename
        )
        # Passes if loader throws no exception
        topic_loader.load()
