"""Class for Hash Table Worksheet resource generator."""

from copy import deepcopy
from operator import itemgetter
from random import randint, shuffle
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.template.loader import render_to_string


class HashTableWorksheetResourceGenerator(BaseResourceGenerator):
    """Class for Hash Table Worksheet resource generator."""

    copies = True

    def data(self):
        """Create data for a copy of the Hash Table Worksheet resource.

        Returns:
            A dictionary of HTML for the resource.
        """
        pages = []

        mod_10_buckets = [{"number": i} for i in range(10)]
        self.set_bucket_counts(mod_10_buckets, zero=1, one=1)
        self.populate_buckets(mod_10_buckets, 10)
        insertion_numbers = self.create_insertion_numbers(mod_10_buckets)
        comparison_numbers = self.create_comparison_numbers(mod_10_buckets)
        html = render_to_string(
            "resources/hash-table-worksheet-page-1.html",
            {
                "mod_10_buckets": mod_10_buckets,
                "insertion_numbers": insertion_numbers,
                "comparison_numbers": comparison_numbers,
            }
        )
        pages.append({"type": "html", "data": html, "thumbnail": True})

        mod_5_buckets = [{"number": i} for i in range(5)]
        self.set_bucket_counts(mod_5_buckets, min_num=4, max_num=18)
        self.populate_buckets(mod_5_buckets, 5)
        comparison_numbers = self.create_comparison_numbers(mod_5_buckets)
        html = render_to_string(
            "resources/hash-table-worksheet-page-2.html",
            {
                "mod_5_buckets": mod_5_buckets,
                "comparison_numbers": comparison_numbers,
            }
        )
        pages.append({"type": "html", "data": html})

        return pages

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

        Args:
            buckets (list): List of bucket dictionaries.
            modulo (int): Modulo used in hash function.
        """
        for bucket in buckets:
            bucket["numbers"] = list()
            while len(bucket["numbers"]) < bucket["count"]:
                number = self.generate_number(bucket, modulo)
                if number not in bucket["numbers"]:
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
        number_prefix_sum_digit = self.sum_digits(number_prefix)
        number_postfix = (modulo - (number_prefix_sum_digit - bucket["number"])) % modulo
        return int(str(number_prefix) + str(number_postfix))

    def create_insertion_numbers(self, buckets, numbers=3):
        """Set bucket number counts.

        Args:
            buckets (list): List of bucket dictionaries.
            numbers (int): Amount of numbers to create.

        Returns:
            List of numbers for question.
        """
        table_numbers = self.hash_table_values(buckets)
        insertion_numbers = []
        while len(insertion_numbers) < numbers:
            random_number = randint(1000, 9999)
            if random_number not in table_numbers:
                insertion_numbers.append(random_number)
                table_numbers.add(random_number)
        return insertion_numbers

    def create_comparison_numbers(self, buckets):
        """Return numbers for comparison questions.

        Args:
            buckets (list): List of bucket dictionaries.

        Returns:
            List of numbers for question.
        """
        comparison_numbers = []
        table_numbers = self.hash_table_values(buckets)
        buckets_desc = sorted(deepcopy(buckets), key=itemgetter("count"), reverse=True)

        # Add number near end of bucket chain longest chain
        question_number = buckets_desc[0]["numbers"][-2]
        comparison_numbers.append(question_number)
        # Use same bucket for next question, so don't remove bucket number.

        # Add number that isn't in table for bucket with values
        question_number = None
        while question_number is None:
            number = self.generate_number(buckets_desc[0], len(buckets))
            if number not in table_numbers:
                question_number = number
        comparison_numbers.append(question_number)
        del buckets_desc[0]

        # Add number at start of bucket chain
        question_number = buckets_desc[0]["numbers"][0]
        comparison_numbers.append(question_number)
        del buckets_desc[0]

        # Add number at end of bucket chain
        question_number = buckets_desc[0]["numbers"][-1]
        comparison_numbers.append(question_number)
        del buckets_desc[0]

        # Add number that isn't in table for empty bucket
        while question_number is None:
            number = self.generate_number(buckets_desc[-1], len(buckets))
            if number not in table_numbers:
                question_number = number
        comparison_numbers.append(question_number)

        # Shuffle values
        shuffle(comparison_numbers)
        return comparison_numbers

    def hash_table_values(self, buckets):
        """Return set of all hash table values.

        Args:
            buckets (list): List of bucket dictionaries.

        Returns:
            Set of all hash table values.
        """
        numbers = set()
        for bucket in buckets:
            numbers.update(bucket["numbers"])
        return numbers

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
