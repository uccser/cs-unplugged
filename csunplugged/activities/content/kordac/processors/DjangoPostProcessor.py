from markdown.postprocessors import Postprocessor

FULL_TEMPLATE = """
{{% extends "main/index.html" %}}
{{% load static %}}

{{% block content %}}
{content}
{{% endblock %}}

{{% block page-scripts %}}
{scripts}
{{% endblock %}}
"""

class DjangoPostProcessor(Postprocessor):
    def __init__(self, ext, *args, **kwargs):
        self.pagescripts = ext.page_scripts
        super().__init__(*args, **kwargs)

    def run(self, text):
        return FULL_TEMPLATE.format(
            content = text,
            scripts = '\n'.join(self.pagescripts)
        )
