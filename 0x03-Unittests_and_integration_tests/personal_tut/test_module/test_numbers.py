import unittest


class NumbersTest(unittest.TestCase):
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all odd.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 1)
