# test_my_module.py

import unittest
from my_module import add, subtract, multiply, divide, power

class TestMyModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)  # This should raise ValueError

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
