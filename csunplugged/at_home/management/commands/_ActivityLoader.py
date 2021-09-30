"""Custom loader for loading an activity."""

import os.path
from django.db import transaction
from django.template.loader import render_to_string
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.language_utils import get_available_languages, get_default_language
from utils.check_required_files import find_image_files
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from at_home.models import Activity

INTRODUCTION_FILENAME = 'introduction.md'
ACTIVITY_STEPS_FILENAME = 'activity-steps.yaml'
ACTIVITY_EXTRA_INFORMATION_FILENAME = 'activity-extra-information.md'
INSIDE_THE_COMPUTER_FILENAME = 'inside-the-computer.md'
PROJECT_FILENAME = 'project.md'
MORE_INFORMATION_FILENAME = 'more-information.md'
ACTIVITY_STEPS = 'activity-steps.yaml'


class ActivityLoader(TranslatableModelLoader):
    """Custom loader for loading an activity."""

    def __init__(self, factory, activity_data, **kwargs):
        """Create the loader for loading an activity.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
        """
        super().__init__(**kwargs)
        self.factory = factory
        self.activity_slug = self.content_path
        self.activity_data = activity_data

    @transaction.atomic
    def load(self):
        """Load the content for an activity.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching attribute.
        """
        activity_translations = self.get_blank_translation_dictionary()

        try:
            order_number = self.activity_data['order-number']
            activity_icon = self.activity_data['icon']
        except KeyError:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                [
                    "order-number",
                    "icon"
                ],
                "Activity"
            )

        # Check if icon is available
        find_image_files([activity_icon], self.structure_file_path)

        # Introduction content
        content_translations = self.get_markdown_translations(INTRODUCTION_FILENAME)
        for language, content in content_translations.items():
            activity_translations[language]['name'] = content.title
            activity_translations[language]['introduction'] = content.html_string

        activity_steps_translations = self.get_activity_step_translations()
        for language, content in activity_steps_translations.items():
            activity_translations[language]['activity_steps'] = content

        activity_extra_info_md_file_path = self.get_localised_file(
            language,
            ACTIVITY_EXTRA_INFORMATION_FILENAME,
        )
        activity_extra_info_exists = os.path.exists(activity_extra_info_md_file_path)
        if activity_extra_info_exists:
            activity_extra_info_translations = self.get_markdown_translations(
                ACTIVITY_EXTRA_INFORMATION_FILENAME,
                heading_required=False,
                remove_title=False,
            )
            for language, content in activity_extra_info_translations.items():
                activity_translations[language]['activity_extra_information'] = content.html_string

        inside_computer_translations = self.get_markdown_translations(
            INSIDE_THE_COMPUTER_FILENAME,
            heading_required=False,
            remove_title=False,
        )
        for language, content in inside_computer_translations.items():
            activity_translations[language]['inside_the_computer'] = content.html_string

        project_md_file_path = self.get_localised_file(
            language,
            PROJECT_FILENAME,
        )
        project_exists = os.path.exists(project_md_file_path)
        if project_exists:
            project_translations = self.get_markdown_translations(
                PROJECT_FILENAME,
                heading_required=False,
                remove_title=False,
            )
            for language, content in project_translations.items():
                activity_translations[language]['project'] = content.html_string

        more_information_md_file_path = self.get_localised_file(
            language,
            MORE_INFORMATION_FILENAME,
        )
        more_information_exists = os.path.exists(more_information_md_file_path)
        if more_information_exists:
            more_information_translations = self.get_markdown_translations(
                MORE_INFORMATION_FILENAME,
                heading_required=False,
                remove_title=False,
            )
            for language, content in more_information_translations.items():
                activity_translations[language]['more_information'] = content.html_string

        # Create or update activity objects and save to the database
        activity, created = Activity.objects.update_or_create(
            slug=self.activity_slug,
            defaults={
                'order_number': order_number,
                'icon': activity_icon,
            },
        )

        self.populate_translations(activity, activity_translations)
        self.mark_translation_availability(activity, required_fields=['name', 'introduction'])
        activity.save()

        if created:
            self.log('Added Activity: {}'.format(activity.name))
        else:
            self.log('Updated Activity: {}'.format(activity.name))

        # structure_filename = os.path.join(unit_plan_file_path)
        self.factory.create_challenge_loader(
            activity,
            base_path=self.base_path,
            content_path=self.content_path,
            structure_filename=self.structure_filename,
            lite_loader=self.lite_loader,
        ).load()

    def get_activity_step_translations(self):
        """Get dictionary of translations of activity steps.

        Returns:
            Dictionary mapping language codes to VertoResult objects.

        Raises:
            CouldNotFindYAMLFileError: If the requested file could not be found
                in the /en directory tree
        """
        content_translations = {}
        for language in get_available_languages():
            try:
                content_translations[language] = self.convert_activity_step_file(
                    self.get_localised_file(
                        language,
                        ACTIVITY_STEPS_FILENAME,
                    )
                )
            except CouldNotFindYAMLFileError:
                if language == get_default_language():
                    raise
        return content_translations

    def convert_activity_step_file(self, yaml_file_path):
        """Return HTML for a given YAML file.

        Args:
            yaml_file_path: Location of YAML file to convert (str).

        Returns:
            String of HTML

        Raises:
            CouldNotFindYAMLFileError: When a given YAML file cannot be found.
        """
        activity_steps_data = self.load_yaml_file(yaml_file_path)

        # Check all images exist
        activity_image_filenames = set()
        for step_data in activity_steps_data:
            activity_image_filenames.add(step_data.get('image'))
        find_image_files(activity_image_filenames, yaml_file_path)

        # Render as HTML
        html = render_to_string(
            'at_home/activity_steps.html',
            {'activity_steps': activity_steps_data}
        )
        return html
