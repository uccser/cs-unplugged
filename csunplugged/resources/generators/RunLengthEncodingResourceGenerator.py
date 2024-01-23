"""Class for Run Length Encoding resource generator."""

from yattag import Doc
from PIL import Image
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter

WORKSHEET_OPTIONS = {
    "student-basic": _("Student Worksheet - Kid Fax"),
    "student-create": _("Student Worksheet - Create your own"),
    "student-create-colour": _("Student Worksheet - Create your own in colour"),
    "teacher": _("Teacher Worksheet"),
}

WORKSHEET_INTRODUCTION_TEXT = {
    "student-basic": _(
        "The first picture is the easiest and the last one is the most complex. "
        "It is easy to make mistakes and therefore a good idea to use a pencil to "
        "colour with and have an eraser handy!"
    ),
    "student-create": _(
        "Now that you know how numbers can represent pictures, why not try making "
        "your own coded picture for a friend? Draw your picture on the top grid, and "
        "when you’ve finished, write the code numbers beside the bottom grid. Cut along "
        "the dotted line and give the bottom grid to a friend to colour in. (Note: you don’t "
        "have to use the whole grid if you don’t want to—just leave some blank lines at "
        "the bottom if your picture doesn’t take up the whole grid.)"
    ),
    "student-create-colour": _(
        "Extra for Experts: If you want to produce coloured images you can use a "
        "number to represent the colour (e.g. 0 is black, 1 is red, 2 is green etc.) Two "
        "numbers are now used to represent a run of pixels: the first gives the length of "
        "the run as before, and the second specifies the colour. Try making a coloured "
        "picture for a friend. Don’t forget to let your friend know which number stands for "
        "which colour!"
    ),
}


class RunLengthEncodingResourceGenerator(BaseResourceGenerator):
    """Class for Run Length Encoding resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for RunLengthEncodingResourceGenerator."""
        return {
            "worksheet_type": EnumResourceParameter(
                name="worksheet_type",
                description=_("Worksheet Type"),
                values=WORKSHEET_OPTIONS,
                default="student-basic"
            )
        }

    def data(self):
        """Create data for a copy of the resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        worksheet_type = self.options["worksheet_type"].value

        if worksheet_type.startswith("student"):
            doc, tag, text, line = Doc().ttl()
            with tag("h3"):
                text(WORKSHEET_OPTIONS[worksheet_type])

            line(
                "style",
                """
                table {
                    margin-bottom: 1cm;
                }
                td {
                    border-collapse: collapse;
                    height: 0.5cm;
                    margin: 0;
                    padding: 0;
                }
                td.bordered-cell {
                    border: 1px solid black;
                    width: 0.5cm;
                }
                td.label-cell {
                    padding-left: 0.5cm;
                    font-size: 0.4cm;
                    line-height: 0.4cm;
                }
                """
            )

            with tag("p"):
                text(WORKSHEET_INTRODUCTION_TEXT[worksheet_type])

            if worksheet_type == "student-basic":
                # Table one
                self.add_run_length_encoding_table(
                    tag,
                    line,
                    9,
                    18,
                    row_labels=[
                        "4, 11",
                        "4, 9, 2, 1",
                        "4, 9, 2, 1",
                        "4, 11",
                        "4, 9",
                        "4, 9",
                        "5, 7",
                        "0, 17",
                        "1, 15",
                    ]
                )
                # Table two
                self.add_run_length_encoding_table(
                    tag,
                    line,
                    13,
                    18,
                    row_labels=[
                        "6, 5, 2, 3",
                        "4, 2, 5, 2, 3, 1",
                        "3, 1, 9, 1, 2, 1",
                        "3, 1, 9, 1, 1, 1",
                        "2, 1, 11, 1",
                        "2, 1, 10, 2",
                        "2, 1, 9, 1, 1, 1",
                        "2, 1, 8, 1, 2, 1",
                        "2, 1, 7, 1, 3, 1",
                        "1, 1, 1, 1, 4, 2, 3, 1",
                        "0, 1, 2, 1, 2, 2, 5, 1",
                        "0, 1, 3, 2, 5, 2",
                        "1, 3, 2, 5 ",
                    ]
                )
                # Table three
                self.add_run_length_encoding_table(
                    tag,
                    line,
                    17,
                    18,
                    row_labels=[
                        "6, 2, 2, 2",
                        "5, 1, 2, 2, 2, 1",
                        "6, 6",
                        "4, 2, 6, 2",
                        "3, 1, 10, 1",
                        "2, 1, 12, 1",
                        "2, 1, 3, 1, 4, 1, 3, 1",
                        "1, 2, 12, 2",
                        "0, 1, 16, 1",
                        "0, 1, 6, 1, 2, 1, 6, 1",
                        "0, 1, 7, 2, 7, 1",
                        "1, 1, 14, 1",
                        "2, 1, 12, 1",
                        "2, 1, 5, 2, 5, 1",
                        "3, 1, 10, 1",
                        "4, 2, 6, 2",
                        "6, 6",
                    ]
                )
            else:
                line(
                    "style",
                    """
                    td.padding-cell {
                        width: 0.5cm;
                    }
                    td.underline-cell {
                        border-bottom: 1px solid #999;
                        width: 8cm;
                    }
                    div.dotted-line {
                        margin-top: 1cm;
                        margin-bottom: 1cm;
                        border-top: 1px dotted #888;
                    }
                    """
                )
                self.add_run_length_encoding_table(tag, line, 16, 16, underline=True)
                line("div", "", klass="dotted-line")
                self.add_run_length_encoding_table(tag, line, 16, 16, underline=True)
            return {"type": "html", "data": doc.getvalue()}
        else:
            image = Image.open("static/img/resources/run-length-encoding/teacher-worksheet.png")
            image = image.rotate(270, expand=True)
            return {"type": "image", "data": image}

    def add_run_length_encoding_table(self, tag, line, rows, columns, row_labels=None, underline=False):
        """Create HTML for run length encoding table.

        Args:
            tag: Tag function from yattag.
            line: Line function from yattag.
            rows (int): Number of rows the table should be.
            columns (int): Number of columns the table should be.
            row_labels (list): List of strings to display after to each row if required.
            underline (bool): True if writing prompt should be displayed after each row.
        """
        if row_labels:
            columns += 1

        with tag("table"):
            with tag("tbody"):
                for row_index in range(rows):
                    with tag("tr"):
                        for column_index in range(columns):
                            line("td", "", klass="bordered-cell")
                        if row_labels and row_index < len(row_labels):
                            line("td", row_labels[row_index], klass="label-cell")
                        if underline:
                            line("td", "", klass="padding-cell")
                            line("td", "", klass="underline-cell")

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        worksheet_type = self.options["worksheet_type"].value
        return "{} - {}".format(WORKSHEET_OPTIONS[worksheet_type], super().subtitle)
