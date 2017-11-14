"""Module for the testing custom Django loadtopics commands."""

import os.path
from unittest import mock
from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag, override_settings
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

TOPICS_PATH = "tests/topics/management/assets/"


@tag("management")
class LoadTopicsCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    # Test calls to curriculum areas loader

    @mock.patch(
        "topics.management.commands._CurriculumAreasLoader.CurriculumAreasLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "curriculum-areas-valid")
    )
    def test_loadtopics_curriculums_areas_valid(self, topic_loader, age_loader, area_loader):
        management.call_command("loadtopics")
        self.assertTrue(area_loader.called)

    @mock.patch(
        "topics.management.commands._CurriculumAreasLoader.CurriculumAreasLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "curriculum-areas-missing")
    )
    def test_loadtopics_curriculums_areas_missing(self, topic_loader, age_loader, area_loader):
        management.call_command("loadtopics")
        self.assertFalse(area_loader.called)

    @mock.patch(
        "topics.management.commands._CurriculumAreasLoader.CurriculumAreasLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "curriculum-areas-empty")
    )
    def test_loadtopics_curriculums_areas_empty(self, topic_loader, age_loader, area_loader):
        management.call_command("loadtopics")
        self.assertFalse(area_loader.called)

    # Test calls to learning outcomes loader

    @mock.patch(
        "topics.management.commands._LearningOutcomesLoader.LearningOutcomesLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "learning-outcomes-valid")
    )
    def test_loadtopics_learning_outcomes_valid(self, topic_loader, age_loader, outcome_loader):
        management.call_command("loadtopics")
        self.assertTrue(outcome_loader.called)

    @mock.patch(
        "topics.management.commands._LearningOutcomesLoader.LearningOutcomesLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "learning-outcomes-missing")
    )
    def test_loadtopics_learning_outcomes_missing(self, topic_loader, age_loader, outcome_loader):
        management.call_command("loadtopics")
        self.assertFalse(outcome_loader.called)

    @mock.patch(
        "topics.management.commands._LearningOutcomesLoader.LearningOutcomesLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "learning-outcomes-empty")
    )
    def test_loadtopics_learning_outcomes_empty(self, topic_loader, age_loader, outcome_loader):
        management.call_command("loadtopics")
        self.assertFalse(outcome_loader.called)

    # Test calls to programming challenges structure loader

    @mock.patch(
        "topics.management.commands._ProgrammingChallengesStructureLoader.ProgrammingChallengesStructureLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "programming-challenges-structure-valid")
    )
    def test_loadtopics_programming_challenges_structure_valid(self, topic_loader, age_loader, structure_loader):
        management.call_command("loadtopics")
        self.assertTrue(structure_loader.called)

    @mock.patch(
        "topics.management.commands._ProgrammingChallengesStructureLoader.ProgrammingChallengesStructureLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "programming-challenges-structure-missing")
    )
    def test_loadtopics_programming_challenges_structure_missing(self, topic_loader, age_loader, structure_loader):
        management.call_command("loadtopics")
        self.assertFalse(structure_loader.called)

    @mock.patch(
        "topics.management.commands._ProgrammingChallengesStructureLoader.ProgrammingChallengesStructureLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "programming-challenges-structure-empty")
    )
    def test_loadtopics_programming_challenges_structure_empty(self, topic_loader, age_loader, structure_loader):
        management.call_command("loadtopics")
        self.assertFalse(structure_loader.called)

    # Test calls to classroom resources loader

    @mock.patch(
        "topics.management.commands._ClassroomResourcesLoader.ClassroomResourcesLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "classroom-resources-valid")
    )
    def test_loadtopics_classroom_resources_valid(self, topic_loader, age_loader, classroom_loader):
        management.call_command("loadtopics")
        self.assertTrue(classroom_loader.called)

    @mock.patch(
        "topics.management.commands._ClassroomResourcesLoader.ClassroomResourcesLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "classroom-resources-missing")
    )
    def test_loadtopics_classroom_resources_missing(self, topic_loader, age_loader, classroom_loader):
        management.call_command("loadtopics")
        self.assertFalse(classroom_loader.called)

    @mock.patch(
        "topics.management.commands._ClassroomResourcesLoader.ClassroomResourcesLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "classroom-resources-empty")
    )
    def test_loadtopics_classroom_resources_empty(self, topic_loader, age_loader, classroom_loader):
        management.call_command("loadtopics")
        self.assertFalse(classroom_loader.called)

    # Test calls to glossary terms loader

    @mock.patch(
        "topics.management.commands._GlossaryTermsLoader.GlossaryTermsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "glossary-terms-valid")
    )
    def test_loadtopics_glossary_terms_valid(self, topic_loader, age_loader, glossary_loader):
        management.call_command("loadtopics")
        self.assertTrue(glossary_loader.called)

    @mock.patch(
        "topics.management.commands._GlossaryTermsLoader.GlossaryTermsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "glossary-terms-missing")
    )
    def test_loadtopics_glossary_terms_missing(self, topic_loader, age_loader, glossary_loader):
        management.call_command("loadtopics")
        self.assertFalse(glossary_loader.called)

    @mock.patch(
        "topics.management.commands._GlossaryTermsLoader.GlossaryTermsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "glossary-terms-empty")
    )
    def test_loadtopics_glossary_terms_empty(self, topic_loader, age_loader, glossary_loader):
        management.call_command("loadtopics")
        self.assertFalse(glossary_loader.called)

    # Test calls to age groups loader

    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "age-groups-valid")
    )
    def test_loadtopics_age_groups_valid(self, topic_loader, age_loader):
        management.call_command("loadtopics")
        self.assertTrue(age_loader.called)

    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "age-groups-missing")
    )
    def test_loadtopics_age_groups_missing(self, topic_loader, age_loader):
        self.assertRaises(
            MissingRequiredFieldError,
            management.call_command,
            "loadtopics"
        )

    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "age-groups-empty")
    )
    def test_loadtopics_age_groups_empty(self, topic_loader, age_loader):
        self.assertRaises(
            MissingRequiredFieldError,
            management.call_command,
            "loadtopics"
        )

    # Test calls to topic loader

    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "topics-valid")
    )
    def test_loadtopics_topics_valid(self, topic_loader, age_loader):
        management.call_command("loadtopics")
        self.assertTrue(topic_loader.called)

    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "topics-missing")
    )
    def test_loadtopics_topics_missing(self, topic_loader, age_loader):
        self.assertRaises(
            MissingRequiredFieldError,
            management.call_command,
            "loadtopics"
        )

    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "topics-empty")
    )
    def test_loadtopics_topics_empty(self, topic_loader, age_loader):
        self.assertRaises(
            MissingRequiredFieldError,
            management.call_command,
            "loadtopics"
        )

    @mock.patch(
        "topics.management.commands._AgeGroupsLoader.AgeGroupsLoader.load",
        return_value=True
    )
    @mock.patch(
        "topics.management.commands._TopicLoader.TopicLoader.load",
        return_value=True
    )
    @override_settings(
        TOPICS_CONTENT_BASE_PATH=os.path.join(TOPICS_PATH, "topics-not-list")
    )
    def test_loadtopics_topics_not_list(self, topic_loader, age_loader):
        self.assertRaises(
            MissingRequiredFieldError,
            management.call_command,
            "loadtopics"
        )
