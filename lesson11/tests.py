import unittest
from homework import Fib, Even, Factorials


class HomeworkTest(unittest.TestCase):
    def test_Fib(self):
        a = Fib(5)
        self.assertTrue(a)
        self.assertEqual(next(a), 1)
        self.assertEqual(next(a), 1)
        self.assertEqual(next(a), 2)
        self.assertEqual(next(a), 3)
        self.assertEqual(next(a), 5)
        with self.assertRaises(StopIteration):
            next(a)

    def test_Even(self):
        b = Even(6)
        self.assertTrue(b)
        self.assertEqual(next(b), 0)
        self.assertEqual(next(b), 2)
        self.assertEqual(next(b), 4)
        self.assertEqual(next(b), 6)
        with self.assertRaises(StopIteration):
            next(b)

    def test_Factorials(self):
        c = Factorials(5)
        self.assertTrue(c)
        self.assertEqual(next(c), 1)
        self.assertEqual(next(c), 2)
        self.assertEqual(next(c), 6)
        self.assertEqual(next(c), 24)
        self.assertEqual(next(c), 120)
        with self.assertRaises(StopIteration):
            next(c)


if __name__ == '__main__':
    unittest.main()
