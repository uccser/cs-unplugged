"""Module for the custom Django loadtopics command."""

import os.path
from django.core.management.base import BaseCommand

from utils.BaseLoader import BaseLoader
from utils.LoaderFactory import LoaderFactory
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class Command(BaseCommand):
    """Required command class for the custom Django loadtopics command."""

    help = "Converts Markdown files listed in structure file and stores"

    def handle(self, *args, **options):
        """Automatically called when the loadresources command is given.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        factory = LoaderFactory()
        # Get structure and content files
        base_loader = BaseLoader()
        BASE_PATH = "topics/content/"

        structure_file_path = os.path.join(
            BASE_PATH,
            base_loader.STRUCTURE_DIR,
            "structure.yaml"
        )

        structure_file = base_loader.load_yaml_file(structure_file_path)

        if "curriculum-areas" in structure_file:
            curriculum_areas_structure_file_path = structure_file["curriculum-areas"]
            if curriculum_areas_structure_file_path is not None:
                curriculum_areas_path, structure_filename = os.path.split(curriculum_areas_structure_file_path)
                factory.create_curriculum_areas_loader(
                    BASE_PATH=BASE_PATH,
                    INNER_PATH=curriculum_areas_path,
                    STRUCTURE_FILE=structure_filename
                ).load()

        if "learning-outcomes" in structure_file:
            learning_outcomes_structure_file_path = structure_file["learning-outcomes"]
            if learning_outcomes_structure_file_path is not None:
                learning_outcomes_path, structure_filename = os.path.split(learning_outcomes_structure_file_path)
                factory.create_learning_outcomes_loader(
                    BASE_PATH=BASE_PATH,
                    INNER_PATH=learning_outcomes_path,
                    STRUCTURE_FILE=structure_filename
                ).load()

        if "programming-challenges-structure" in structure_file:
            programming_challenges_structure_file_path = structure_file["programming-challenges-structure"]
            if programming_challenges_structure_file_path is not None:
                programming_challenges_path, structure_filename = os.path.split(programming_challenges_structure_file_path)
                factory.create_programming_challenges_structure_loader(
                    BASE_PATH=BASE_PATH,
                    INNER_PATH=programming_challenges_path,
                    STRUCTURE_FILE=structure_filename
                ).load()

        if "glossary-folder" in structure_file:
            glossary_folder_path = structure_file["glossary-folder"]
            if glossary_folder_path is not None:
                factory.create_glossary_terms_loader(
                    BASE_PATH=BASE_PATH,
                    INNER_PATH=glossary_folder_path,
                ).load()

        if structure_file["age-groups"] is None:
            raise MissingRequiredFieldError(
                structure_file_path,
                ["age-groups"],
                "Application Structure"
            )
        else:
            age_groups_structure_file_path = structure_file["age-groups"]
            if age_groups_structure_file_path is not None:
                age_groups_path, structure_filename = os.path.split(age_groups_structure_file_path)
                factory.create_age_groups_loader(
                    INNER_PATH=age_groups_path,
                    BASE_PATH=BASE_PATH,
                    STRUCTURE_FILE=structure_filename
                ).load()

        if structure_file["topics"] is None:
            raise MissingRequiredFieldError(
                structure_file_path,
                ["topics"],
                "Application Structure"
            )

        for topic in structure_file["topics"]:
            topic_path = topic
            topic_structure_file = "{}.yaml".format(topic)
            factory.create_topic_loader(
                BASE_PATH=BASE_PATH,
                INNER_PATH=topic_path,
                STRUCTURE_FILE=topic_structure_file
            ).load()
