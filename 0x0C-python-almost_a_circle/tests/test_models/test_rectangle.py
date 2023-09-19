#!/usr/bin/python3

"""This module tests the recrangle module (rectangle.py) in
the models folder
"""

from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """TestRectangle class defines test cases for the
    rectangle class
    """

    def test_with_vald_id(self):
        pass

    def test_with_invalid_id(self):
        pass

    def test_with_no_id(self):
        pass

    def test_no_args(self):
        """new rectangle object without argument"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_valid_args(self):
        """new rectangle object with valid arguments"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.area, 50)

        r2 = Rectangle(10, 5, 2)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 2)

        r3 = Rectangle(1, 5, 1, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.area, 5)
        self.assertEqual(print(r3), "[Rectangle] (3) 1/2 - 1/5")

        r4 = Rectangle(5, 11, 1, 1, 7)
        self.assertEqual(r4.id, 7)
        self.assertEqual(r4.area, 55)

        r5 = Rectangle(5, 1, 1, 1, 7)
        self.assertEqual(r4.display, "#####")

    def test_nonvalid_args(self):
        """new rectangle object with non valid arguments"""
        with self.asserRaises(TypeError):
            Rectangle("Fab", "is Great")
        with self.asserRaises(TypeError):
            Rectangle(-1, "is Great")
        with self.asserRaises(TypeError):
            Rectangle(7, "Fab")
        with self.asserRaises(TypeError):
            Rectangle(7, 4, "Fab", "is Great")
        with self.asserRaises(TypeError):
            Rectangle(7, 4, 2, "Great")

    def test_toomany_args(self):
        """new rectangle object with too many argument"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_notenough_args(self):
        """new rectangle object with not enough argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)
