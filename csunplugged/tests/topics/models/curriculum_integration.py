from model_mommy import mommy
from tests.BaseTest import BaseTest
from topics.models import CurriculumIntegration
from topics.models import Topic
from topics.models import CurriculumArea
from topics.models import Lesson


class CurriculumIntegrationModelTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_curriculum_integration(self):
        topic = mommy.make(Topic)
        curriculum_areas = mommy.make(CurriculumArea, make_m2m=True, name='cats')
        curriculum_areas.save()
        prerequisite_lessons = mommy.make(Lesson, make_m2m=True, name='dogs')
        prerequisite_lessons.save()
        new_curriculum_integration = CurriculumIntegration.objects.create(
            topic=topic,
            slug='slug',
            number=1,
            name='name',
            content='content',
            curriculum_areas=curriculum_areas,
            prerequisite_lessons=prerequisite_lessons
        )
        query_result = CurriculumIntegration.objects.get(slug='slug')
        self.assertEqual(query_result, new_curriculum_integration)
