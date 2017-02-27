from django.core import management

class Command(management.base.BaseCommand):
    help = 'Flush and load data for all applications'

    def handle(self, *args, **options):
        """The function called when the loaddata command is given"""
        management.call_command('flush', interactive=False)
        management.call_command('loadresources')
        management.call_command('loadtopics')
