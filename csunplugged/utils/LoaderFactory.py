"""Factory for creating loader objects."""

from topics.management.commands._AgeGroupsLoader import AgeGroupsLoader
from topics.management.commands._CurriculumAreasLoader import CurriculumAreasLoader
from topics.management.commands._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader
from topics.management.commands._GlossaryTermsLoader import GlossaryTermsLoader
from topics.management.commands._LearningOutcomesLoader import LearningOutcomesLoader
from topics.management.commands._LessonsLoader import LessonsLoader
from topics.management.commands._ProgrammingChallengesLoader import ProgrammingChallengesLoader
from topics.management.commands._ProgrammingChallengesStructureLoader import ProgrammingChallengesStructureLoader
from topics.management.commands._TopicLoader import TopicLoader
from topics.management.commands._ClassroomResourcesLoader import ClassroomResourcesLoader
from at_home.management.commands._ActivityLoader import ActivityLoader
from at_home.management.commands._ChallengeLoader import ChallengeLoader
from resources.management.commands._ResourcesLoader import ResourcesLoader
from classic.management.commands._ClassicPagesLoader import ClassicPagesLoader
from general.management.commands._GeneralPagesLoader import GeneralPagesLoader


class LoaderFactory:
    """Factory for creating loader objects."""

    def create_age_groups_loader(self, **kwargs):
        """Create age group loader."""
        return AgeGroupsLoader(**kwargs)

    def create_curriculum_areas_loader(self, **kwargs):
        """Create curriculum area loader."""
        return CurriculumAreasLoader(**kwargs)

    def create_curriculum_integrations_loader(self, topic, **kwargs):
        """Create curriculum integrations loader."""
        return CurriculumIntegrationsLoader(topic, **kwargs)

    def create_glossary_terms_loader(self, **kwargs):
        """Create glossary terms loader."""
        return GlossaryTermsLoader(**kwargs)

    def create_learning_outcomes_loader(self, **kwargs):
        """Create learning outcomes loader."""
        return LearningOutcomesLoader(**kwargs)

    def create_lessons_loader(self, topic, **kwargs):
        """Create lessons loader."""
        return LessonsLoader(topic, **kwargs)

    def create_classroom_resources_loader(self, **kwargs):
        """Create lessons loader."""
        return ClassroomResourcesLoader(**kwargs)

    def create_programming_challenges_loader(self, topic, **kwargs):
        """Create programming challenges loader."""
        return ProgrammingChallengesLoader(topic, **kwargs)

    def create_programming_challenges_structure_loader(self, **kwargs):
        """Create programming challenges structure loader."""
        return ProgrammingChallengesStructureLoader(**kwargs)

    def create_topic_loader(self, **kwargs):
        """Create topic loader."""
        return TopicLoader(self, **kwargs)

    def create_activity_loader(self, **kwargs):
        """Create activity loader."""
        return ActivityLoader(self, **kwargs)

    def create_challenge_loader(self, activity, **kwargs):
        """Create challenge loader."""
        return ChallengeLoader(self, activity, **kwargs)

    def create_resources_loader(self, **kwargs):
        """Create resources loader."""
        return ResourcesLoader(**kwargs)

    def create_classic_pages_loader(self, **kwargs):
        """Create Classic CS Unplugged pages loader."""
        return ClassicPagesLoader(structure_dir="", **kwargs)

    def create_general_pages_loader(self, **kwargs):
        """Create general pages loader."""
        return GeneralPagesLoader(structure_dir="", **kwargs)
