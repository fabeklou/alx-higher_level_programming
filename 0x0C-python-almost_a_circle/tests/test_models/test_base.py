#!/usr/bin/python3

"""This module tests the base module (base.py) in
the models folder
"""

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Test case for the base class"""

    def test_no_arg(self):
        """New Base object without argument"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_valid_arg(self):
        """New Base object with valid argument"""
        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    def test_invalid_arg(self):
        """New Base object with invalid argument"""
        b4 = Base(None)
        self.assertEqual(b4.id, 1)

        b_str = Base("Fab is great")
        self.assertEqual(b_str.id, "Fab is great")
