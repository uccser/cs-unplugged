"""Class for Binary to Alphabet resource generator."""

from yattag import Doc
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from resources.utils.resource_parameters import EnumResourceParameter
import utils.alphabets


WORKSHEET_VERSION_VALUES = {
    "student": _("Student"),
    "teacher": _("Teacher (solutions)"),
}
COLUMNS = 2


class BinaryToAlphabetResourceGenerator(BaseResourceGenerator):
    """Class for Binary to Alphabet resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for BinaryToAlphabetResourceGenerator."""
        return {
            "worksheet_version": EnumResourceParameter(
                name="worksheet_version",
                description=_("Worksheet Version"),
                values=WORKSHEET_VERSION_VALUES,
                default="student"
            )
        }

    def data(self):
        """Create a image for Binary to Alphabet resource.

        Returns:
            A dictionary for the resource page.
        """
        doc, tag, text, line = Doc().ttl()
        alphabet = utils.alphabets.get_alphabet(get_language())
        teacher_version = self.options["worksheet_version"].value == "teacher"
        binary_length = len("{:b}".format(len(alphabet)))
        binary_template = "{:0" + str(binary_length) + "b}"
        half_binary_length = len(alphabet) // 2
        column_uneven = len(alphabet) % 2 == 1
        if column_uneven:
            half_binary_length += 1

        alphabet_description = utils.alphabets.get_alphabet_description(get_language())
        if alphabet_description:
            with tag("h3", klass="text-center"):
                text(alphabet_description)

        line("style", "th, td {text-align: center;} table {font-size: 1.4rem;}")
        with tag("table", klass="table table-sm table-bordered"):
            with tag("thead"):
                with tag("tr"):
                    for i in range(2):
                        line("th", _("Base 10"))
                        line("th", _("Binary"))
                        line("th", _("Letter"))
            with tag("tbody"):
                for i in range(half_binary_length):
                    with tag("tr"):
                        first_col_num = i
                        first_col_letter = alphabet[first_col_num]
                        line("td", first_col_num)
                        if teacher_version:
                            line("td", binary_template.format(first_col_num), klass="text-monospace")
                            line("td", first_col_letter)
                        else:
                            line("td", "")
                            line("td", "")
                        second_col_num = i + half_binary_length
                        if not second_col_num == len(alphabet):
                            second_col_letter = alphabet[second_col_num]
                            line("td", second_col_num)
                            if teacher_version:
                                line("td", binary_template.format(second_col_num), klass="text-monospace")
                                line("td", second_col_letter)
                            else:
                                line("td", "")
                                line("td", "")
        return {"type": "html", "data": doc.getvalue()}

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            Text for subtitle (str).
        """
        text = "{} - {}".format(
            WORKSHEET_VERSION_VALUES[self.options["worksheet_version"].value],
            super().subtitle
        )
        return text
