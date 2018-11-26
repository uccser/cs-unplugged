"""Class for Hash Table Worksheet resource generator."""

from random import randint
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.template.loader import render_to_string


class RandomNumbersResourceGenerator(BaseResourceGenerator):
    """Class for Hash Table Worksheet resource generator."""

    copies = True

    def data(self):
        """Create data for a copy of the Hash Table Worksheet resource.

        Returns:
            A dictionary of HTML for the resource.
        """
        pages = []

        random_numbers_col_1 = list()
        random_numbers_col_2 = list()
        random_numbers_col_3 = list()
        random_numbers_col_4 = list()

        for i in range(0, 10):
            random_numbers_col_1.append(self.generate_number(i, 10))
            random_numbers_col_2.append(self.generate_number(i, 10))
            random_numbers_col_3.append(self.generate_number(i, 10))
            random_numbers_col_4.append(self.generate_number(i, 10))

        html = render_to_string(
            "resources/random-numbers.html",
            {
                "random_numbers_col_1": random_numbers_col_1,
                "random_numbers_col_2": random_numbers_col_2,
                "random_numbers_col_3": random_numbers_col_3,
                "random_numbers_col_4": random_numbers_col_4,
            }
        )
        pages.append({"type": "html", "data": html, "thumbnail": True})

        return pages

    def generate_number(self, num, modulo):
        """Generate unique number for bucket.

        Args:
            bucket (dict): Data of bucket.
            modulo (int): Modulo used in hash function.

        Returns:
            Unique integer for bucket.
        """
        number_prefix = randint(100, 999)
        number_prefix_sum_digit = self.sum_digits(number_prefix)
        number_postfix = (modulo - (number_prefix_sum_digit - num)) % modulo
        return int(str(number_prefix) + str(number_postfix))

    def sum_digits(self, n):
        """Return sum of number's digits.

        From: https://stackoverflow.com/a/14940026.

        Args:
            n (int): Number to sum.

        Returns:
            Integer of sum.
        """
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
