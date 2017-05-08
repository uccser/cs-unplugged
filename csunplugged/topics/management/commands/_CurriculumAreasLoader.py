"""Custom loader for loading curriculum areas."""

import os.path

from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import CurriculumArea


class CurriculumAreasLoader(BaseLoader):
    """Loader for curriculum area content."""

    def __init__(self, structure_file_path, BASE_PATH):
        """Create the loader for loading curriculum areas.

        Args:
            structure_file_path: File path to YAML file (string)
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH)
        self.structure_file_path = structure_file_path
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])

    @transaction.atomic
    def load(self):
        """Load the content for curriculum areas.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        curriculum_areas_structure = self.load_yaml_file(
            os.path.join(
                self.BASE_PATH,
                self.structure_file_path
            )
        )

        for (curriculum_area_slug, curriculum_area_data) in curriculum_areas_structure.items():

            if curriculum_area_data is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["name"],
                    "Curriculum Area"
                )

            curriculum_area_name = curriculum_area_data.get("name", None)
            if curriculum_area_name is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["name"],
                    "Curriculum Area"
                )

            curriculum_area_colour = curriculum_area_data.get("colour", None)
            if curriculum_area_colour is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["colour"],
                    "Curriculum Area"
                )

            # Create area objects and save to database
            new_area = CurriculumArea(
                slug=curriculum_area_slug,
                name=curriculum_area_name,
                colour=curriculum_area_colour,
            )
            new_area.save()

            self.log("Added Curriculum Area: {}".format(new_area.__str__()))

            # Create children curriculum areas with reference to parent
            if "children" in curriculum_area_data:
                children_curriculum_areas = curriculum_area_data["children"]
                if children_curriculum_areas is None:
                    raise MissingRequiredFieldError(
                        self.structure_file_path,
                        ["name"],
                        "Child Curriculum Area"
                    )
                for (child_slug, child_data) in children_curriculum_areas.items():
                    if child_data is None:
                        raise MissingRequiredFieldError(
                            self.structure_file_path,
                            ["name"],
                            "Child Curriculum Area"
                        )
                    child_name = child_data.get("name", None)
                    if child_name is None:
                        raise MissingRequiredFieldError(
                            self.structure_file_path,
                            ["name"],
                            "Child Curriculum Area"
                        )

                    new_child = CurriculumArea(
                        slug=child_slug,
                        name=child_name,
                        colour=curriculum_area_colour,
                        parent=new_area,
                    )
                    new_child.save()

                    self.log("Added Child Curriculum Area: {}".format(new_child.__str__()), 1)

        # Print log output
        self.print_load_log()
