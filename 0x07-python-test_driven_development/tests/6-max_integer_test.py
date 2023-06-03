#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_ordered_list(self):
        """Test a list with ordered elements"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list with unordered elements"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_negative_list(self):
        """Test a list with negative elements"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_list(self):
        """Test a list with float elements"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_string_list(self):
        """Test a list with string elements"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_mixed_list(self):
        """Test a list with mixed elements"""
        with self.assertRaises(TypeError):
            max_integer([1, "b", 3, "d"])

    def test_none(self):
        """Test a None list"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_arguments(self):
        """Test no arguments passed"""
        self.assertEqual(max_integer(), None)

    def test_one_argument(self):
        """Test one argument passed"""
        self.assertEqual(max_integer([1]), 1)

    def test_no_list(self):
        """Test a non-list argument"""
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_dict(self):
        """Test a dictionary"""
        with self.assertRaises(KeyError):
            max_integer({1: "a", 2: "b", 3: "c", 4: "d"})

    def test_tuple(self):
        """Test a tuple"""
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_set(self):
        """Test a set"""
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4})


if __name__ == '__main__':
    unittest.main()
