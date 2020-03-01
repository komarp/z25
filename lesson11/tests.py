import unittest
from homework import BinomialCoefficients


class HomeworkTest(unittest.TestCase):
    def test_binom(self):
        self.assertEqual(list(BinomialCoefficients(0)), [1])
        self.assertEqual(list(BinomialCoefficients(1)), [1, 1])
        self.assertEqual(list(BinomialCoefficients(5)), [1, 5, 10, 10, 5, 1])


if __name__ == '__main__':
    unittest.main()
