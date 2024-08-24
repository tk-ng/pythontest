from operator import is_
from algorithms import reverse_str, is_Palindrome, factorial
from unittest import TestCase


class AlgorithmsTestCase(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str("hello"), "olleh")
        self.assertEqual(reverse_str("Apple"), "elppA")

    def test_is_palindrome(self):
        self.assertTrue(is_Palindrome('racecar'))
        self.assertTrue(is_Palindrome('kayak'))
        self.assertFalse(is_Palindrome('taco'))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertRaises(ValueError, factorial, -3)
