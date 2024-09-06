#!/usr/bin/python3
"""Find the max integer in a list"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer."""

    def test_ordered_list(self):
        """Test the ordered list of integers."""
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def test_unordered_list(self):
        """Test the unordered list of integers."""
        unorder = [1, 3, 4, 2]
        self.assertEqual(max_integer(unorder), 4)

    def test_max_at_begginning(self):
        """Test the list with a beginning max value."""
        max_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_beginning), 4)

    def test_empty_list(self):
        """Test if the list is empty."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test the list with a single element."""
        un_elementt = [7]
        self.assertEqual(max_integer(un_element), 7)

    def test_floats(self):
        """Test the list of floats."""
        a_float = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(a_float), 15.2)

    def test_ints_and_floats(self):
        """Test the list of ints and floats."""
        int_and_float = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(int_and_float), 15.5)

    def test_string(self):
        """Test the string."""
        a_string = "Brennan"
        self.assertEqual(max_integer(a_string), 'r')

    def test_list_of_strings(self):
        """Test the list of strings."""
        a_string = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(a_string), "name")

    def test_empty_string(self):
        """Test if the string is empty."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
