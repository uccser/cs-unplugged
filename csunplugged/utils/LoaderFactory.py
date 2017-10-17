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
from topics.management.commands._UnitPlanLoader import UnitPlanLoader
from resources.management.commands._ResourcesLoader import ResourcesLoader


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

    def create_lessons_loader(self, topic, unit_plan, **kwargs):
        """Create lessons loader."""
        return LessonsLoader(topic, unit_plan, **kwargs)

    def create_programming_challenges_loader(self, topic, **kwargs):
        """Create programming challenges loader."""
        return ProgrammingChallengesLoader(topic, **kwargs)

    def create_programming_challenges_structure_loader(self, **kwargs):
        """Create programming challenges structure loader."""
        return ProgrammingChallengesStructureLoader(**kwargs)

    def create_topic_loader(self, **kwargs):
        """Create topic loader."""
        return TopicLoader(self, **kwargs)

    def create_unit_plan_loader(self, topic, **kwargs):
        """Create unit plan loader."""
        return UnitPlanLoader(self, topic, **kwargs)

    def create_resources_loader(self, structure_file, base_path):
        """Create resources loader."""
        return ResourcesLoader(structure_file, base_path)
