import unittest
from homework import custom_range


def foo(a):
    if a % 2:
        return True
    else:
        return False


class HomeworkTest(unittest.TestCase):
    def test_my_range(self):
        result = custom_range(4)
        self.assertEqual(result, [0, 1, 2, 3])

    def test_foo(self):
        self.assertIs(foo(5), True)
        self.assertIs(foo(4), False)

    def test_failed(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
