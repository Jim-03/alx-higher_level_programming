#!/usr/bin/python3
"""Unittest for 6-max_integer."""


#importation of the module
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The tests for max_integer."""

    def test_random_list(self):
        """Tests for a list with random arrangement."""
        random_list = [8, 1000, 6000000, 1]
        self.assertEqual(max_integer(random_list), 6000000)

    def test_negative_list(self):
        """Test a list with negative numbers"""
        negative_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative_list), -1)

    def test_duplicated(self):
        """TEsts a list with duplicated values."""
        duplicate_list = [1, 1, 2, 3, 4, 5, 5]
        self.assertEqual(max_integer(duplicate_list), 5)

    def test_invalid_list(self):
        """Tests a  list with invalid data type."""
        invalid_list = [1, 'two', 3, 4]
        with self.assertRaises(TypeError):
            max_integer(invalid_list)

    def test_empty_list(self):
        """Tests an empty list."""
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

if __name__ == '__main__':
    unittest.main()
