import unittest

from tests.topics.urls.index import IndexURLTest
from tests.topics.urls.all_curriculum_integrations import AllCurriculumIntegrationsURLTest
from tests.topics.urls.topic import TopicURLTest
from tests.topics.urls.integration_list import IntegrationListURLTest
from tests.topics.urls.integration import IntegrationURLTest
from tests.topics.urls.other_resources import OtherResourcesURLTest
from tests.topics.urls.unit_plan import UnitPlanURLTest
from tests.topics.urls.lesson import LessonURLTest
from tests.topics.urls.programming_exercises_list import ProgrammingExercisesListURLTest
from tests.topics.urls.programming_exercise import ProgrammingExerciseURLTest
from tests.topics.urls.programming_exercise_language_solution import ProgrammingExerciseLanguageSolutionURLTest
from tests.topics.urls.programming_exercise_difficulty import ProgrammingExerciseDifficultyURLTest


if __name__=='__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(IndexURLTest),
        unittest.makeSuite(AllCurriculumIntegrationsURLTest),
        unittest.makeSuite(TopicURLTest),
        unittest.makeSuite(IntegrationListURLTest),
        unittest.makeSuite(IntegrationURLTest),
        unittest.makeSuite(OtherResourcesURLTest),
        unittest.makeSuite(UnitPlanURLTest),
        unittest.makeSuite(LessonURLTest),
        unittest.makeSuite(ProgrammingExercisesListURLTest),
        unittest.makeSuite(ProgrammingExerciseURLTest),
        unittest.makeSuite(ProgrammingExerciseLanguageSolutionURLTest),
        unittest.makeSuite(ProgrammingExerciseDifficultyURLTest),
    ))

    runner = unittest.TextTestRunner()
    runner.run(suite)