"""Class for Hash Table Worksheet resource generator."""

from random import randint, sample, shuffle
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.template.loader import render_to_string


class HashTableWorksheetResourceGenerator(BaseResourceGenerator):
    """Class for Hash Table Worksheet resource generator."""

    def data(self):
        """Create data for a copy of the Hash Table Worksheet resource.

        Returns:
            A dictionary of HTML for the resource.
        """
        mod_10_buckets = [{"number": i} for i in range(10)]
        self.set_bucket_counts(mod_10_buckets, zero=1, one=1)
        self.populate_buckets(mod_10_buckets, 10)
        mod_5_buckets = [{"number": i} for i in range(5)]
        self.set_bucket_counts(mod_5_buckets, min_num=3, max_num=10)
        self.populate_buckets(mod_5_buckets, 5)
        context = {
            "mod_10_buckets": mod_10_buckets,
            "mod_5_buckets": mod_5_buckets,
        }
        html = render_to_string("resources/hash-table-worksheet.html", context)
        return {"type": "html", "data": html}

    def set_bucket_counts(self, buckets, zero=0, one=0, min_num=2, max_num=5):
        """Set bucket number counts.

        Args:
            buckets (list): List of bucket dictionaries.
            zero (int): Number of buckets to contain zero numbers.
            one (int): Number of buckets to contain one number.
            min_num (int): For remaining buckets, the minimum number of numbers.
            max_num (int): For remaining buckets, the maximum number of numbers.
        """
        bucket_numbers = list(range(0, len(buckets)))
        shuffle(bucket_numbers)
        for i in range(0, zero):
            buckets[bucket_numbers.pop()]["count"] = 0
        for i in range(0, one):
            buckets[bucket_numbers.pop()]["count"] = 1
        for bucket_number in bucket_numbers:
            buckets[bucket_number]["count"] = randint(min_num, max_num)

    def populate_buckets(self, buckets, modulo):
        """Populate buckets to their number counts.

        Currently duplicate numbers are allowed.

        Args:
            buckets (list): List of bucket dictionaries.
            modulo (int): Modulo used in hash function.
        """
        for bucket in buckets:
            bucket["numbers"] = list()
            while len(bucket["numbers"]) < bucket["count"]:
                number = self.generate_number(bucket, modulo)
                bucket["numbers"].append(number)

    def generate_number(self, bucket, modulo):
        """Generate unique number for bucket.

        Args:
            bucket (dict): Data of bucket.
            modulo (int): Modulo used in hash function.

        Returns:
            Unique integer for bucket.
        """
        number_prefix = randint(100, 999)
        number_prefix_sum_digit = self.sum_digits(number_prefix) % modulo
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
