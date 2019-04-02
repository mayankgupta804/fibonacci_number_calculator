from django.test import TestCase

from .fibonacci_number import calculate_fibonacci_number

class FibonacciNumberTests(TestCase):

    def test_calculate_fibonacci_number_positive_input(self):
        input = 6
        expected = 8
        actual = calculate_fibonacci_number(input)
        self.assertEqual(actual, expected)

    def test_calculate_fibonacci_number_negative_input(self):
        input = -6
        expected = -1
        actual = calculate_fibonacci_number(input)
        self.assertEqual(actual, expected)