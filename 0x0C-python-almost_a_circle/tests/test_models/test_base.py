#!/usr/bin/python3

"""This module tests the base module (base.py) in
the models folder
"""

import unittest


class TestBase(unittest.TestCase):
    """Tesrt case for the base class"""

    def test_no_arg(self):
        """New Base object without argument"""
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)

    def test_valid_arg(self):
        """New Base object with valid argument"""
        b = Base(10)
        self.assertEqual(b.id, 10)
