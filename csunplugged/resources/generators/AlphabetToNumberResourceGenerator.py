"""Class for Alphabet to number resource generator."""

from yattag import Doc
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
import utils.alphabets


COLUMNS = 2


class AlphabetToNumberResourceGenerator(BaseResourceGenerator):
    """Class for Alphabet to number resource generator."""

    def data(self):
        """Create a image for Alphabet to number resource.

        Returns:
            A dictionary for the resource page.
        """
        doc, tag, text, line = Doc().ttl()
        alphabet = utils.alphabets.get_alphabet(get_language())

        half_alphabet_length = len(alphabet) // 2
        column_uneven = len(alphabet) % 2 == 1
        if column_uneven:
            half_alphabet_length += 1

        alphabet_description = utils.alphabets.get_alphabet_description(get_language())
        if alphabet_description:
            with tag("h3", klass="text-center"):
                text(alphabet_description)

        line("style", "th, td {text-align: center;} table {font-size: 1.4rem;}")
        with tag("table", klass="table table-sm table-bordered"):
            with tag("thead"):
                with tag("tr"):
                    for i in range(2):
                        line("th", _("Number"))
                        line("th", _("Letter"))
            with tag("tbody"):
                for i in range(1, half_alphabet_length):
                    with tag("tr"):
                        first_col_num = i
                        first_col_letter = alphabet[first_col_num]
                        line("td", first_col_num)
                        line("td", first_col_letter)

                        second_col_num = i + half_alphabet_length
                        if not second_col_num == len(alphabet):
                            second_col_letter = alphabet[second_col_num]
                            line("td", second_col_num)
                            line("td", second_col_letter)

        return {"type": "html", "data": doc.getvalue()}
