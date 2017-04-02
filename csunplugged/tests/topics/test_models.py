import unittest

from tests.topics.models.learning_outcome import LearningOutcomeModelTest
from tests.topics.models.curriculum_area import CurriculumAreaModelTest
from tests.topics.models.classroom_resource import ClassroomResourceModelTest
from tests.topics.models.topic import TopicModelTest
from tests.topics.models.unit_plan import UnitPlanModelTest
from tests.topics.models.programming_exercise_difficulty import ProgrammingExerciseDifficultyModelTest
from tests.topics.models.programming_exercise import ProgrammingExerciseModelTest
from tests.topics.models.programming_exercise_language import ProgrammingExerciseLanguageModelTest
from tests.topics.models.programming_exercise_language_implementation import ProgrammingExerciseLanguageImplementationModelTest
from tests.topics.models.lesson import LessonModelTest
from tests.topics.models.curriculum_integration import CurriculumIntegrationModelTest
from tests.topics.models.connected_generated_resource import ConnectedGeneratedResourceModelTest


# NTS think django might be bypassing this and just executing all 'test_' methods...
if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LearningOutcomeModelTest),
        unittest.makeSuite(CurriculumAreaModelTest),
        unittest.makeSuite(ClassroomResourceModelTest),
        unittest.makeSuite(TopicModelTest),
        unittest.makeSuite(UnitPlanModelTest),
        unittest.makeSuite(ProgrammingExerciseDifficultyModelTest),
        unittest.makeSuite(ProgrammingExerciseModelTest),
        unittest.makeSuite(ProgrammingExerciseLanguageModelTest),
        unittest.makeSuite(ProgrammingExerciseLanguageImplementationModelTest),
        unittest.makeSuite(LessonModelTest),
        unittest.makeSuite(CurriculumIntegrationModelTest),
        unittest.makeSuite(CurriculumAreaModelTest),
        unittest.makeSuite(ConnectedGeneratedResourceModelTest),
    ))

    runner = unittest.TextTestRunner()
    runner.run(suite)
