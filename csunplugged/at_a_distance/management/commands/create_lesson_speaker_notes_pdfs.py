"""Module for the custom Django create_lesson_speaker_notes_pdfs command."""

import os.path
from django.conf import settings
from django.core.management.base import BaseCommand
from at_a_distance.models import Lesson
from at_a_distance.settings import (
    AT_A_DISTANCE_FILE_GENERATION_LOCATION,
    AT_A_DISTANCE_SLIDE_RESOLUTION,
)
from at_a_distance.utils import get_lesson_speaker_notes
from django.template.loader import render_to_string


class Command(BaseCommand):
    """Required command class for the custom Django create_lesson_speaker_notes_pdfs command."""

    help = "Create PDF of lessons."

    def add_arguments(self, parser):
        """Add optional parameter to create_lesson_speaker_notes_pdfs command."""
        parser.add_argument(
            "--language",
            default=None,
            dest="language",
            help="The language to generate speaker notes PDF for.",
        )

    def handle(self, *args, **options):
        """Automatically called when the create_lesson_speaker_notes_pdfs command is given."""
        # If deployed, throw error
        if settings.DEPLOYED:
            raise Exception("The 'create_lesson_pdfs' command cannot be run when deployed")

        given_language_parameter = options["language"]
        if given_language_parameter == 'all':
            languages = settings.DEFAULT_LANGUAGES
            print("Generating speaker notes PDF files for all languages")
        elif given_language_parameter:
            languages = [(given_language_parameter, "")]
            print(f"Generating speaker notes PDF files for {given_language_parameter} only")
        else:
            languages = [("en", "")]
            print("Generating speaker notes PDF files for 'en' only")

        for language_code, _ in languages:
            for lesson in Lesson.objects.all():
                # Gather speaker notes
                speaker_notes = get_lesson_speaker_notes(lesson)

                context = dict()
                slides = []
                image_directory = os.path.join(
                    AT_A_DISTANCE_FILE_GENERATION_LOCATION,
                    language_code,
                    lesson.slug,
                )
                filename = f"{lesson.slug}_{{}}_{AT_A_DISTANCE_SLIDE_RESOLUTION}.png"

                for (slide_number, speaker_note) in enumerate(speaker_notes, start=1):
                    slides.append(
                        {
                            'number': slide_number,
                            'image': os.path.join(
                                image_directory,
                                filename.format(slide_number),
                            ),
                            'notes': speaker_note,
                        }
                    )
                context["slides"] = slides

                # Render to PDF using Weasyprint
                (pdf_file, filename) = create_speaker_notes_pdf(lesson, context)

                pdf_directory = os.path.join(
                    AT_A_DISTANCE_FILE_GENERATION_LOCATION,
                    language_code,
                    lesson.slug,
                )
                if not os.path.exists(pdf_directory):
                    os.makedirs(pdf_directory)

                filename = f"{filename}.pdf"
                pdf_file_output = open(os.path.join(pdf_directory, filename), "wb")
                pdf_file_output.write(pdf_file)
                pdf_file_output.close()
                print(f"  - Created '{language_code}' speaker notes PDF for {lesson.slug}")


def create_speaker_notes_pdf(lesson, context):
    """Return PDF for speaker notes lesson.

    Args:
        lesson (Lesson): The lesson the PDF is related too.
        context (dict): Data for rendering in the PDF.

    Return:
        PDF file.
    """
    # Only import weasyprint when required as production environment
    # does not have it installed.
    from weasyprint import HTML, CSS

    filename = f"{lesson.slug}-speaker-notes"

    context["lesson"] = lesson
    context["filename"] = filename

    pdf_html = render_to_string(
        "at_a_distance/components/base-speaker-notes-pdf.html",
        context,
    )
    html = HTML(string=pdf_html, base_url=settings.BUILD_ROOT)
    css_file = os.path.join(
        settings.BUILD_ROOT,
        "css/at-a-distance/speaker-notes-pdf.print.css",
    )
    css_string = open(css_file, encoding="UTF-8").read()
    base_css = CSS(string=css_string)
    pdf = html.write_pdf(stylesheets=[base_css])
    return (pdf, filename)
