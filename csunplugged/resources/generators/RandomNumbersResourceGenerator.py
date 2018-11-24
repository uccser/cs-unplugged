"""Class for Hash Table Worksheet resource generator."""

from copy import deepcopy
from operator import itemgetter
from random import randint, shuffle
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

        random_numbers = list()
        self.set_bucket_counts(mod_10_buckets, zero=1, one=1)
        self.populate_buckets(mod_10_buckets, 10)
        insertion_numbers = self.create_insertion_numbers(mod_10_buckets)
        comparison_numbers = self.create_comparison_numbers(mod_10_buckets)
        html = render_to_string(
            "resources/hash-table-worksheet-page-1.html",
            {
                "random_numbers": random_numbers,
            }
        )
        pages.append({"type": "html", "data": html, "thumbnail": True})

        return pages

    def generate_number(self, bucket, modulo):
        """Generate unique number for bucket.

        Args:
            bucket (dict): Data of bucket.
            modulo (int): Modulo used in hash function.

        Returns:
            Unique integer for bucket.
        """
        number_prefix = randint(100, 999)
        number_prefix_sum_digit = self.sum_digits(number_prefix)
        number_postfix = (modulo - (number_prefix_sum_digit - bucket["number"])) % modulo
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
