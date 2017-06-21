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

    def create_age_groups_loader(self, structure_file_path, BASE_PATH):
        """Create age group loader."""
        return AgeGroupsLoader(structure_file_path, BASE_PATH)

    def create_curriculum_areas_loader(self, structure_file_path, BASE_PATH):
        """Create curriculum area loader."""
        return CurriculumAreasLoader(structure_file_path, BASE_PATH)

    def create_curriculum_integrations_loader(self, structure_file_path, topic, BASE_PATH):
        """Create curriculum integrations loader."""
        return CurriculumIntegrationsLoader(structure_file_path, topic, BASE_PATH)

    def create_glossary_terms_loader(self, glossary_folder_path, structure_file_path, BASE_PATH):
        """Create glossary terms loader."""
        return GlossaryTermsLoader(glossary_folder_path, structure_file_path, BASE_PATH)

    def create_learning_outcomes_loader(self, structure_file_path, BASE_PATH):
        """Create learning outcomes loader."""
        return LearningOutcomesLoader(structure_file_path, BASE_PATH)

    def create_lessons_loader(self, structure_file_path, topic, unit_plan, BASE_PATH):
        """Create lessons loader."""
        return LessonsLoader(structure_file_path, topic, unit_plan, BASE_PATH)

    def create_programming_challenges_loader(self, structure_file, topic, BASE_PATH):
        """Create programming challenges loader."""
        return ProgrammingChallengesLoader(structure_file, topic, BASE_PATH)

    def create_programming_challenges_structure_loader(self, structure_file_path, BASE_PATH):
        """Create programming challenges structure loader."""
        return ProgrammingChallengesStructureLoader(structure_file_path, BASE_PATH)

    def create_topic_loader(self, structure_file_path, BASE_PATH):
        """Create topic loader."""
        return TopicLoader(self, structure_file_path, BASE_PATH)

    def create_unit_plan_loader(self, structure_file_path, topic, BASE_PATH):
        """Create unit plan loader."""
        return UnitPlanLoader(self, structure_file_path, topic, BASE_PATH)

    def create_resources_loader(self, structure_file, BASE_PATH):
        """Create resources loader."""
        return ResourcesLoader(structure_file, BASE_PATH)
