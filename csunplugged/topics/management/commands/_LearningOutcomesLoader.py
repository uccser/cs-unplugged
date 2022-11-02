"""Custom loader for loading learning outcomes."""

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from topics.models import (
    LearningOutcome,
    CurriculumArea,
)


class LearningOutcomesLoader(TranslatableModelLoader):
    """Custom loader for loading learning outcomes."""

    @transaction.atomic
    def load(self):
        """Load the content for learning outcomes.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        learning_outcomes = self.load_yaml_file(self.structure_file_path)
        learning_outcomes_translations = self.get_yaml_translations(
            self.structure_filename,
            required_fields=["text"],
            required_slugs=learning_outcomes.keys()
        )

        for (outcome_slug, outcome_data) in learning_outcomes.items():
            translations = self.get_blank_translation_dictionary()
            translations.update(learning_outcomes_translations.get(outcome_slug, dict()))

            # Create or update learning outcome objects and save to db
            outcome, created = LearningOutcome.objects.update_or_create(
                slug=outcome_slug,
            )
            self.populate_translations(outcome, translations)
            self.mark_translation_availability(outcome, required_fields=["text"])
            outcome.save()

            # Add curriculum areas
            curriculum_area_slugs = outcome_data.get("curriculum-areas", [])

            for curriculum_area_slug in curriculum_area_slugs:
                try:
                    curriculum_area = CurriculumArea.objects.get(
                        slug=curriculum_area_slug
                    )
                    if curriculum_area.children.exists():
                        raise InvalidYAMLValueError(
                            self.structure_file_path,
                            "curriculum-areas - value '{}' is invalid".format(curriculum_area_slug),
                            "Curriculum area with no children (parent curriculum areas are not allowed)"
                        )
                    else:
                        outcome.curriculum_areas.add(curriculum_area)
                except ObjectDoesNotExist:
                    raise KeyNotFoundError(
                        self.structure_file_path,
                        curriculum_area_slug,
                        "Curriculum Areas"
                    )

            if created:
                term = 'Created'
            else:
                term = 'Updated'
            self.log(f'{term} learning outcome: {outcome.__str__()}')
        self.log("All learning outcomes loaded!\n")
