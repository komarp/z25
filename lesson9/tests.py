import unittest
from homework import DataType


class HomeworkTest(unittest.TestCase):
    def test_ok(self):
        self.assertTrue(True)

    def test_init(self):
        obj = DataType()
        self.assertIs(obj._size, None)
        self.assertEqual(obj._data, [])
        obj = DataType(5)
        self.assertIs(obj._size, 5)

    def test_data_type(self):
        obj = DataType(2)
        self.assertTrue(obj.is_empty())
        obj.push('smth')
        self.assertFalse(obj.is_empty())
        value = obj.pop()
        self.assertEqual(value, 'smth')
        with self.assertRaises(Exception) as ctx:
            obj.pop()
        self.assertEqual(str(ctx.exception), "DataType is empty")
        obj.push(1)
        obj.push(2)
        self.assertTrue(obj.is_full())
        with self.assertRaises(Exception) as ctx:
            obj.push(3)
        self.assertEqual(str(ctx.exception), 'Queue is full')


if __name__ == '__main__':
    unittest.main()
