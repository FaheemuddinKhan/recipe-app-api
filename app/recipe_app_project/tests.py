from django.test import TestCase
from . import calc


class CalcTests(TestCase):
    """Unit Test function for the add function"""
    def test_add_numbers(self):
        self.assertEqual(calc.add(3, 5), 8)
