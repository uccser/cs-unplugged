from django.template.loader import render_to_string
from at_a_distance.models import Lesson
from lxml import html


def get_slide_lengths():
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
