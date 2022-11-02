"""Custom loader for loading curriculum areas."""

from django.db import transaction
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import CurriculumArea


class CurriculumAreasLoader(TranslatableModelLoader):
    """Loader for curriculum area content."""

    @transaction.atomic
    def load(self):
        """Load the content for curriculum areas.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        curriculum_areas_structure = self.load_yaml_file(self.structure_file_path)
        curriculum_areas_translations = self.get_yaml_translations(
            self.structure_filename,
            required_fields=["name"],
            required_slugs=curriculum_areas_structure.keys()
        )

        for (curriculum_area_slug, curriculum_area_data) in curriculum_areas_structure.items():

            if curriculum_area_data is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["name"],
                    "Curriculum Area"
                )
            translations = curriculum_areas_translations.get(curriculum_area_slug, dict())

            curriculum_area_colour = curriculum_area_data.get("colour", None)
            if curriculum_area_colour is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["colour"],
                    "Curriculum Area"
                )

            curriculum_area_number = curriculum_area_data.get("number", None)
            if curriculum_area_number is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["number"],
                    "Curriculum Area"
                )

            # Create area objects and save to database
            new_area, created = CurriculumArea.objects.update_or_create(
                slug=curriculum_area_slug,
                defaults={
                    'colour': curriculum_area_colour,
                    'number': curriculum_area_number,
                }
            )
            self.populate_translations(new_area, translations)
            self.mark_translation_availability(new_area, required_fields=["name"])

            new_area.save()

            if created:
                term = 'Created'
            else:
                term = 'Updated'
            self.log(f'{term} curriculum area: {new_area.__str__()}')

            # Create children curriculum areas with reference to parent
            if "children" in curriculum_area_data:
                children_curriculum_areas = curriculum_area_data["children"]
                if children_curriculum_areas is None:
                    raise MissingRequiredFieldError(
                        self.structure_file_path,
                        ["slug"],
                        "Child Curriculum Area"
                    )
                for child_slug in children_curriculum_areas:
                    translations = curriculum_areas_translations.get(child_slug, dict())

                    new_child, created_child = CurriculumArea.objects.update_or_create(
                        slug=child_slug,
                        defaults={
                            'colour': curriculum_area_colour,
                            'number': curriculum_area_number,
                            'parent': new_area,
                        }
                    )
                    self.populate_translations(new_child, translations)
                    self.mark_translation_availability(new_child, required_fields=["name"])

                    new_child.save()

                    if created_child:
                        term = 'Created'
                    else:
                        term = 'Updated'
                    self.log(f'{term} child curriculum area: {new_child.__str__()}', 1)

        self.log("All curriculum areas loaded!\n")
