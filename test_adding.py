import adding
from unittest import TestCase


class AdderTestCase(TestCase):
    """Examples of unit tests"""

    def test_adder(self):
        self.assertEqual(adding.adder(2, 2), 4)
        # self.assertEqual(adding.adder(2, 3), 9)
        self.assertEqual(adding.adder(40, 50), 90)
        self.assertEqual(adding.adder(-2, -4), -6)

    def test_adder2(self):
        assert adding.adder(2, 3) == 5
