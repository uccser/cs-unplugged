"""Module for the custom Django loadtopics command."""

import os.path
from django.core.management.base import BaseCommand

from utils.BaseLoader import BaseLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from ._LearningOutcomesLoader import LearningOutcomesLoader
from ._CurriculumAreasLoader import CurriculumAreasLoader
from ._TopicLoader import TopicLoader
from ._ProgrammingExercisesStructureLoader import ProgrammingExercisesStructureLoader
from ._GlossaryTermsLoader import GlossaryTermsLoader


class Command(BaseCommand):
    """Required command class for the custom Django loadtopics command."""

    help = "Converts Markdown files listed in structure file and stores"

    def handle(self, *args, **options):
        """Automatically called when the loadresources command is given.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        # Get structure and content files
        base_loader = BaseLoader()
        BASE_PATH = "topics/content/en/"

        structure_file_path = os.path.join(
            BASE_PATH,
            "structure.yaml"
        )

        structure_file = base_loader.load_yaml_file(structure_file_path)

        if "curriculum-areas" in structure_file:
            curriculum_areas_structure_file_path = structure_file["curriculum-areas"]
            if curriculum_areas_structure_file_path is not None:
                CurriculumAreasLoader(
                    curriculum_areas_structure_file_path,
                    BASE_PATH
                ).load()

        if "learning-outcomes" in structure_file:
            learning_outcomes_structure_file_path = structure_file["learning-outcomes"]
            if learning_outcomes_structure_file_path is not None:
                LearningOutcomesLoader(
                    learning_outcomes_structure_file_path,
                    BASE_PATH
                ).load()

        if "programming-challenges-structure" in structure_file:
            programming_challenges_structure_file_path = structure_file["programming-challenges-structure"]
            if programming_challenges_structure_file_path is not None:
                ProgrammingExercisesStructureLoader(
                    programming_challenges_structure_file_path,
                    BASE_PATH
                ).load()

        if "glossary-folder" in structure_file:
            glossary_folder_path = structure_file["glossary-folder"]
            if glossary_folder_path is not None:
                GlossaryTermsLoader(
                    glossary_folder_path,
                    structure_file_path,
                    BASE_PATH
                ).load()

        if structure_file["topics"] is None:
            raise MissingRequiredFieldError(
                structure_file_path,
                ["topics"],
                "Application Structure"
            )

        for topic in structure_file["topics"]:
            topic_structure_file = "{0}/{0}.yaml".format(topic)
            TopicLoader(
                topic_structure_file,
                BASE_PATH
            ).load()
