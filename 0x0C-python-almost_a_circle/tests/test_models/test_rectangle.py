#!/usr/bin/python3

"""This module tests the recrangle module (rectangle.py) in
the models folder
"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
import sys
import io


class TestRectangle(unittest.TestCase):
    """TestRectangle class defines test cases for the
    rectangle class
    """

    def test_with_valid_id(self):
        """New Rectangle object with valid id"""
        r = Rectangle(4, 3, 1, 1, 7)
        self.assertEqual(r.id,  7)

    def test_with_invalid_id(self):
        pass

    def test_with_no_id(self):
        """New Rectangle object without id"""
        Base._Base__nb_objects = 0
        r = Rectangle(9, 7, 0, 0)
        self.assertEqual(r.id, 1)

    def test_no_args(self):
        """new rectangle object without argument"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_valid_args(self):
        """new rectangle object with valid arguments"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(10, 5, 2)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 5, 1, 2)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(5, 11, 1, 1, 7)
        self.assertEqual(r4.id, 7)

    def test_nonvalid_args(self):
        """new rectangle object with non valid arguments"""
        with self.assertRaises(TypeError):
            Rectangle("Fab", "is Great")
        with self.assertRaises(ValueError):
            Rectangle(-1, "is Great")
        with self.assertRaises(TypeError):
            Rectangle(7, "Fab")
        with self.assertRaises(TypeError):
            Rectangle(7, 4, "Fab", "is Great")
        with self.assertRaises(TypeError):
            Rectangle(7, 4, 2, "Great")

    def test_toomany_args(self):
        """new rectangle object with too many argument"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_not_enough_args(self):
        """new rectangle object with not enough argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width_prop(self):
        "Test the with property of a rectangle object"
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)

        r1.width = 20
        self.assertEqual(r1.width, 20)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = -5

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = "Greatness"

    def test_height_prop(self):
        "Test the height property of a rectangle object"
        Base._Base__nb_objects = 1
        r2 = Rectangle(10, 5, 2)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.height, 5)

        r2.height = 15
        self.assertEqual(r2.height, 15)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.height = -5

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = "Fab"

    def test_x_prop(self):
        "Test the x property of a rectangle object"
        r3 = Rectangle(15, 10, 2, 1, 3)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.x, 2)

        r3.x = 1
        self.assertEqual(r3.x, 1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r3.x = -2

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r3.x = 'x'

    def test_y_prop(self):
        "Test the y property of a rectangle object"
        r4 = Rectangle(6, 10)
        self.assertEqual(r4.y, 0)

        r4.y = 2
        self.assertEqual(r4.y, 2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r4.y = -2

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4.y = 'y'

    def test_area(self):
        "Test the area method of a rectangle object"
        r = Rectangle(6, 4)
        self.assertEqual(r.area(), 24)

    def test_dispplay(self):
        "Test the display method of a rectangle object"
        r = Rectangle(4, 2)
        prev_stdout = sys.stdout
        result = io.StringIO()
        sys.stdout = result
        r.display()
        sys.stdout = prev_stdout
        self.assertEqual(result.getvalue(), "####\n" * 2)

    def test_update(self):
        "Test the update method of a rectangle object"
        rx = Rectangle(10, 10, 10, 10)

        rx.update(101)
        self.assertEqual(str(rx), "[Rectangle] (101) 10/10 - 10/10")

        rx.update(101, 2)
        self.assertEqual(str(rx), "[Rectangle] (101) 10/10 - 2/10")

        rx.update(101, 2, 3)
        self.assertEqual(str(rx), "[Rectangle] (101) 10/10 - 2/3")

        rx.update(101, 2, 3, 4)
        self.assertEqual(str(rx), "[Rectangle] (101) 4/10 - 2/3")

        rx.update(101, 2, 3, 4, 5)
        self.assertEqual(str(rx), "[Rectangle] (101) 4/5 - 2/3")

    def test_to_dict(self):
        "Test the to_dictionary method of a rectangle object"
        r = Rectangle(10, 5, 2, 2, 107)
        self.assertTrue(r.to_dictionary() == {"id": 107, "width": 10,
                                              "height": 5, "x": 2, "y": 2})

    def test__str__(self):
        "Test the __str__ magic method of a rectangle object"
        r = Rectangle(7, 5, 1, 1, 201)
        self.assertEqual(r.id, 201)
        self.assertEqual(str(r), "[Rectangle] (201) 1/1 - 7/5")


if __name__ == "__main__":
    unittest.main()
