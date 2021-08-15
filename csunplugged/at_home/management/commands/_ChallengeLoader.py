"""Custom loader for loading activity challenges."""

from django.db import transaction
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.check_required_files import find_image_files
from at_home.models import Challenge

CHALLENGES_FILENAME = 'challenges.yaml'


class ChallengeLoader(TranslatableModelLoader):
    """Custom loader for loading activity challenges."""

    def __init__(self, factory, activity, **kwargs):
        """Create the loader for loading activity challenges.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
            activty: Object of related activity model (Activity).
        """
        super().__init__(**kwargs)
        self.factory = factory
        self.activity = activity

    @transaction.atomic
    def load(self):
        """Load the activity challenges.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        challenge_translations = self.get_yaml_translations(
            CHALLENGES_FILENAME,
            required_fields=["question"]
        )

        for (challenge_order_number, challenge_data) in challenge_translations.items():
            translations = self.get_blank_translation_dictionary()
            translations.update(challenge_translations.get(
                challenge_order_number,
                dict()
            ))
            # Store all answers in lower case
            # TODO: Check if this ruins answers, especially in translations
            for language, translation in translations.items():
                if 'answer' in translation:
                    translation['answer'] = translation['answer'].lower()

            if "image" in challenge_data:
                challenge_image = challenge_data["image"]
                # Check if challenge image is available
                find_image_files([challenge_image], self.structure_file_path)

            # Create or update challenge and save to databbase
            challenge, created = Challenge.objects.update_or_create(
                order_number=challenge_order_number,
                activity=self.activity,
            )
            self.populate_translations(challenge, translations)
            if "answer" in challenge_data:
                self.mark_translation_availability(
                    challenge,
                    required_fields=["question", "answer"]
                )
            else:
                self.mark_translation_availability(
                    challenge,
                    required_fields=["question"]
                )
            challenge.save()

            if created:
                self.log("Added challenge: {}".format(challenge.__str__()), 1)
            else:
                self.log("Updated challenge: {}".format(challenge.__str__()), 1)
