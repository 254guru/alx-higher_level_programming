#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases
    """
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer(self):
        result = max_integer([1, 3, 2, 4, 5])
        self.assertEqual(result, 5)

    def test_max_negative_integer(self):
        result = max_integer([-1, -3, -2, -4, -5])
        self.assertEqual(result, -1)

    def test_max_floats(self):
        result = max_integer([1.5, 3.7, 2.2, 4.9])
        self.assertEqual(result, 4.9)

    def test_mixed_data_types(self):
        result = max_integer([1, "two", 3, "four"])
        self.assertIsNone(result)

    def test_duplicate_max_values(self):
        result = max_integer([4, 4, 4, 4])
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
