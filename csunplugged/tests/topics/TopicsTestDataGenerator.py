"""Create test data for topic tests."""

import os.path
import yaml

from topics.models import (
    Topic,
    UnitPlan,
    Lesson,
    LessonNumber,
    AgeGroup,
    CurriculumIntegration,
    CurriculumArea,
    ProgrammingChallenge,
    ProgrammingChallengeDifficulty,
    ProgrammingChallengeLanguage,
    ProgrammingChallengeImplementation,
    ProgrammingChallengeNumber,
    LearningOutcome,
    GlossaryTerm,
    ResourceDescription,
    ClassroomResource,
)
from plugging_it_in.models import TestCase


class TopicsTestDataGenerator:
    """Class for generating test data for topics."""

    def __init__(self):
        """Create TopicsTestDataGenerator object."""
        self.BASE_PATH = "tests/topics/"
        self.LOADER_ASSET_PATH = os.path.join(self.BASE_PATH, "loaders/assets/")

    def load_yaml_file(self, yaml_file_path):
        """Load a yaml file.

        Args:
            yaml_file_path:  The path to a given yaml file (str).

        Returns:
            Contents of a yaml file.
        """
        yaml_file = open(yaml_file_path, encoding="UTF-8").read()
        return yaml.load(yaml_file)

    def create_integration(self, topic, number, lessons=None, curriculum_areas=None):
        """Create curriculum integration object.

        Args:
            topic: The related Topic object (Topic).
            number: Identifier of the topic (int).
            lessons: List of prerequisite lessons (list).
            curriculum_areas: List of curriculum areas (list).

        Returns:
            CurriculumIntegration object.
        """
        integration = CurriculumIntegration(
            topic=topic,
            slug="integration-{}".format(number),
            name="Integration {}".format(number),
            number=number,
            content="<p>Content for integration {}.</p>".format(number),
        )
        integration.save()
        if lessons:
            for lesson in lessons:
                integration.prerequisite_lessons.add(lesson)
        if curriculum_areas:
            for curriculum_area in curriculum_areas:
                integration.curriculum_areas.add(curriculum_area)
        return integration

    def create_curriculum_area(self, number, parent=None):
        """Create curriculum area object.

        Args:
            number: Identifier of the area (int).
            parent: Parent of the curriculum area (CurriculumArea).

        Returns:
            CurriculumArea object.
        """
        area = CurriculumArea(
            slug="area-{}".format(number),
            name="Area {}".format(number),
            colour="colour-{}".format(number),
            number=number,
            parent=parent,
            languages=["en"],
        )
        area.save()
        return area

    def create_topic(self, number):
        """Create topic object.

        Args:
            number: Identifier of the topic (int).

        Returns:
            Topic object.
        """
        topic = Topic(
            slug="topic-{}".format(number),
            name="Topic {}".format(number),
            content="<p>Content for topic {}.</p>".format(number),
            languages=["en"],
        )
        topic.save()
        return topic

    def create_unit_plan(self, topic, number):
        """Create unit plan object.

        Args:
            topic: The related Topic object (Topic).
            number: Identifier of the unit plan (int).

        Returns:
            UnitPlan object.
        """
        unit_plan = UnitPlan(
            topic=topic,
            slug="unit-plan-{}".format(number),
            name="Unit Plan {}".format(number),
            content="<p>Content for unit plan {}.</p>".format(number),
            languages=["en"],
        )
        unit_plan.save()
        return unit_plan

    def create_lesson(self, topic, unit_plan, number, age_groups=None):
        """Create lesson object.

        Args:
            topic: The related Topic object (Topic).
            unit_plan: The related UnitPlan object (UnitPlan).
            number: Identifier of the topic (int).

        Returns:
            Lesson object.
        """
        if age_groups and not isinstance(age_groups, list):
            age_groups = [age_groups]
        lesson = Lesson(
            topic=topic,
            unit_plan=unit_plan,
            slug="lesson-{}".format(number),
            name="Lesson {} ({} to {})".format(
                number,
                age_groups[0].ages[0] if age_groups else "none",
                age_groups[-1].ages[1] if age_groups else "none"
            ),
            duration=number,
            content="<p>Content for lesson {}.</p>".format(number),
            languages=["en"],
        )
        lesson.save()
        if age_groups:
            for age_group in age_groups:
                LessonNumber(
                    age_group=age_group,
                    lesson=lesson,
                    number=number,
                ).save()
        return lesson

    def create_age_group(self, min_age, max_age):
        """Create AgeGroup object.

        Args:
            min_age: the minumum age for the group (int).
            max_age: the maximum age for the group (int).

        Returns:
            AgeGroup object.
        """
        age_group = AgeGroup(
            slug="{}-{}".format(min_age, max_age),
            ages=(min_age, max_age),
            languages=["en"],
        )
        age_group.save()
        return age_group

    def create_difficulty_level(self, number):
        """Create difficuly level object.

        Args:
            number: Identifier of the level (int).

        Returns:
            ProgrammingChallengeDifficulty object.
        """
        difficulty = ProgrammingChallengeDifficulty(
            level="1",
            name="Difficulty-{}".format(number),
            languages=["en"],
        )
        difficulty.save()
        return difficulty

    def create_programming_language(self, number):
        """Create programming language object.

        Args:
            number: Identifier of the language (int).

        Returns:
            ProgrammingChallengeLanguage object.
        """
        language = ProgrammingChallengeLanguage(
            slug="language-{}".format(number),
            name="Language {}".format(number),
            number=number,
            languages=["en"],
        )
        language.save()
        return language

    def create_programming_challenge(self, topic, number,
                                     difficulty,
                                     challenge_set_number=1,
                                     challenge_number=1,
                                     content="<p>Example content.</p>",
                                     testing_examples="<p>Testing example</p>",
                                     extra_challenge="<p>Example challenge.</p>",
                                     ):
        """Create programming challenge object.

        Args:
            topic: Topic related to the challenge.
            number: Identifier of the challenge (int).
            difficulty: Difficulty related to the challenge
                        (ProgrammingChallengeDifficulty).
            challenge_set_number: Integer of challenge set number (int).
            challenge_number: Integer of challenge number (int).
            content: Text of challenge (str).
            extra_challenge: Text of extra challenge (str).

        Returns:
            ProgrammingChallenge object.
        """
        challenge = ProgrammingChallenge(
            topic=topic,
            slug="challenge-{}".format(number),
            name="Challenge {}.{}: {}".format(
                challenge_set_number,
                challenge_number,
                number,
            ),
            challenge_set_number=challenge_set_number,
            challenge_number=challenge_number,
            content=content,
            testing_examples=testing_examples,
            extra_challenge=extra_challenge,
            difficulty=difficulty,
            languages=["en"],
        )
        challenge.save()
        return challenge

    def create_programming_challenge_implementation(self, topic,
                                                    language,
                                                    challenge,
                                                    expected_result="<p>Example result.</p>",
                                                    hints="<p>Example hints.</p>",
                                                    solution="<p>Example solution.</p>",
                                                    ):
        """Create programming challenge implementation object.

        Args:
            topic: Topic related to the implementation.
            language: Language related to the implementation
                        (ProgrammingChallengeLanguage).
            challenge: Challenge related to the implementation
                        (ProgrammingChallenge).
            expected_result: Text of expected_result (str).
            hints: Text of hints (str).
            solution: Text of solution (str).

        Returns:
            ProgrammingChallengeImplementation object.
        """
        implementation = ProgrammingChallengeImplementation(
            topic=topic,
            language=language,
            challenge=challenge,
            expected_result=expected_result,
            hints=hints,
            solution=solution,
            languages=["en"],
        )
        implementation.save()
        return implementation

    def create_learning_outcome(self, number):
        """Create learning outcome object.

        Args:
            number: Identifier of the outcome (int).

        Returns:
            LearningOutcome object.
        """
        outcome = LearningOutcome(
            slug="outcome-{}".format(number),
            text="Outcome {}".format(number),
            languages=["en"],
        )
        outcome.save()
        return outcome

    def create_classroom_resource(self, number):
        """Create classroom resource object.

        Args:
            number: Identifier of the resource (int).

        Returns:
            ClassroomResource object.
        """
        resource = ClassroomResource(
            slug="resource-{}".format(number),
            description="Resource {}".format(number),
            languages=["en"],
        )
        resource.save()
        return resource

    def add_challenge_lesson_relationship(self, challenge, lesson, set_number, number):
        """Add relationship between challenge and lesson objects.

        Args:
            challenge: Challenge to add relationship between
                       (ProgrammingChallenge).
            lesson: Lesson to add relationship between (Lesson).
            set_number: Number to display as challenge set number (int).
            number: Number to display as challenge number (int).
        """
        relationship = ProgrammingChallengeNumber(
            programming_challenge=challenge,
            lesson=lesson,
            challenge_set_number=set_number,
            challenge_number=number,
        )
        relationship.save()

    def create_glossary_term(self, number):
        """Create glossary term object.

        Args:
            number: Identifier of the glossary term (int).

        Returns:
            GlossaryTerm object.
        """
        term = GlossaryTerm(
            slug="term-{}".format(number),
            term="Term {}".format(number),
            definition="Defintion for term {}".format(number),
        )
        term.save()
        return term

    def add_lesson_resource_relationship(self, lesson, resource, number):
        """Add relationship between challenge and lesson objects.

        Args:
            lesson (Lesson): Lesson to add relationship between.
            resource (Resource): Resource to add relationship between.
            number (int): Number to display in description.
        """
        relationship = ResourceDescription(
            lesson=lesson,
            resource=resource,
            description="Description {}".format(number),
        )
        relationship.save()

    def create_programming_challenge_test_case(self, number, challenge):
        """Create test case object.

        Args:
            number: Identifier of the test case (int).
            challenge: Challenge that the test case is for (Challenge object).

        Returns:
            TestCase object.
        """
        test_case = TestCase(
            number=number,
            challenge=challenge,
        )
        test_case.save()
        return test_case
