"""This module defines a test class used to test the
max_integer function

"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """subclass of unittest.TestCase baseclass used to
    implement unit test of the function max_integer

    """
    def test_empty_list(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_no_arg(self):
        result = max_integer()
        self.assertEqual(result, None)

    def test_int_list(self):
        self.assertEqual(max_integer([11, 2, 3, 0, 13]), 13)
        self.assertEqual(max_integer([13, 2, 3, 0, 12]), 13)
        self.assertEqual(max_integer([7, -2, 8, 0, 1]), 8)
        self.assertEqual(max_integer([11]), 11)
        self.assertEqual(max_integer([11, 2, 3, 0, 17]), 17)

    def test_negative_int_list(self):
        result = max_integer([-11, -2, -3, -1, -12])
        self.assertEqual(result, -1)

    def test_string_argument(self):
        result = max_integer("string")
        self.assertEqual(result, 't')
        self.assertIsInstance(result, str)

    def test_list_of_float(self):
        result = max_integer([1.0, 7.1, 9.2, 9])
        self.assertIsInstance(result, float)
        self.assertEqual(result, 9.2)

    def test_list_of_bool(self):
        result = max_integer([True, False, False, True])
        self.assertIsInstance(result, bool)
        self.assertEqual(result, True)

    def test_char(self):
        result = max_integer('d')
        self.assertEqual(result, 'd')

    def test_list_of_char(self):
        result = max_integer(['d', 'f', 'z'])
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'z')

    def test_int_tuple(self):
        result = max_integer((9, 2, 1, 11))
        self.assertEqual(result, 11)

    def test_float_tuple(self):
        result = max_integer((7.1, 2.3, 7.9, 9.1))
        self.assertEqual(result, 9.1)
