"""Module for the custom Django updatedata command."""

from django.core import management


class Command(management.base.BaseCommand):
    """Required command class for the custom Django updatedata command."""

    help = "Update all data from content folders for all applications"

    def add_arguments(self, parser):
        """Add optional parameter to updatedata command."""
        parser.add_argument(
            "--lite-load",
            action="store_true",
            dest="lite_load",
            help="Perform lite load (only load key content)",
        )

    def handle(self, *args, **options):
        """Automatically called when the updatedata command is given."""
        lite_load = options.get("lite_load")
        management.call_command("flush", interactive=False)
        management.call_command("loadresources", lite_load=lite_load)
        management.call_command("loadtopics", lite_load=lite_load)
        management.call_command("loadgeneralpages", lite_load=lite_load)
        management.call_command("loadclassicpages", lite_load=lite_load)
        management.call_command("loadactivities", lite_load=lite_load)
        management.call_command("load_at_a_distance_data", lite_load=lite_load)
        management.call_command("rebuild_search_indexes")
