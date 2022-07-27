"""Utility functions for the at a distance application."""

from django.template.loader import render_to_string
from at_a_distance.models import Lesson
from lxml import html


def get_lesson_speaker_notes(lesson):
    """Get speaker notes for lesson slides suitable for PDF creation.

    Args:
        lesson (Lesson): Lesson object for rendering HTML.

    Returns:
        Array of HTML of lesson slides speaker notes.
    """
    slide_html = render_to_string(
        "at_a_distance/components/reveal-slides-structure.html",
        {
            "lesson": lesson,
        }
    )
    root = html.fromstring(slide_html)
    speaker_notes = []
    slide_elements = root.cssselect('div.slides section')
    for slide_element in slide_elements:
        slide_notes = slide_element.cssselect('aside.notes')
        if slide_notes:
            speaker_note_html = html.tostring(slide_notes[0], pretty_print=True, encoding='unicode')
            speaker_notes.append(speaker_note_html)
        else:
            speaker_notes.append(False)
    return speaker_notes


def get_slide_lengths():
    """Return slide lengths for every lesson.

    Returns:
        Dictionary of lesson slugs mapped to slide counts.
    """
    data = dict()
    for lesson in Lesson.objects.all():
        slide_html = render_to_string(
            "at_a_distance/components/reveal-slides-structure.html",
            {
                "lesson": lesson,
            }
        )
        root = html.fromstring(slide_html)
        slide_count = len(root.cssselect('div.slides section'))
        data[lesson.slug] = slide_count
    return data
