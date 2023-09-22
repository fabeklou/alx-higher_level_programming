#!/usr/bin/python3

"""This tests the square module from models"""

from models.base import Base
from models.square import Square
import unittest
import sys
import io


def saves_output(func):
    """Saves the value previously printed to stdout
    and returns it

    Args:
        func (fnc): is a function pointer (a reference)
            to the function be used

    Returns:
        (): value previously printed to stdout

    """
    prev_stdout = sys.stdout
    output = io.StringIO()
    sys.stdout = output
    func()
    sys.stdout = prev_stdout
    return output.getvalue()


class TestSquare(unittest.TestCase):
    """TestSquare class defines test cses for the Square class
    """

    def test_without_id(self):
        """Create a new Square object without id"""
        Base._Base__nb_objects = 0
        s = Square(10, 2)
        self.assertEqual(s.id, 1)

    def test_with_id(self):
        """Create a new Square object with valid id"""
        s = Square(10, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_number_of_objects(self):
        """Test the effective number of square object created"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_size_prop(self):
        """Test size property of a square object"""
        s = Square(8)
        self.assertEqual(s.size, 8)

        s.size = 4
        self.assertEqual(s.size, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "Fab"

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -3

    def test_x_prop(self):
        """Test the x property of a square object"""
        s = Square(8)
        self.assertEqual(s.x, 0)

        s.x = 2
        self.assertEqual(s.x, 2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.x = "Fab"

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.x = -3

    def test_y_prop(self):
        """Test the y property of a square object"""
        s = Square(8)
        self.assertEqual(s.y, 0)

        s.y = 2
        self.assertEqual(s.y, 2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.y = "Fab"

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.y = -3

    def test_area(self):
        """Test the area method of a square object"""
        s = Square(8)
        self.assertEqual(s.area(), 64)

    def test_display(self):
        """Test the display method of a square object"""
        Square._nb_instances = 0

        s1 = Square(5)
        output1 = saves_output(s1.display)
        self.assertEqual(output1, "#####\n" * 5)

        s2 = Square(4, 4)
        output2 = saves_output(s2.display)
        self.assertEqual(output2, "    ####\n" * 4)

        s3 = Square(4, 2, 2)
        output3 = saves_output(s3.display)
        self.assertEqual(output3, "\n\n" + "  ####\n" * 4)

    def test_update(self):
        """Test the update method of a square object"""
        sx = Square(4)
        sx.update(101)
        self.assertEqual(str(sx), "[Square] (101) 0/0 - 4")

        sx.update(101, 6)
        self.assertEqual(str(sx), "[Square] (101) 0/0 - 6")

        sx.update(101, 6, 1)
        self.assertEqual(str(sx), "[Square] (101) 1/0 - 6")

        sx.update(101, 6, 1, 1)
        self.assertEqual(str(sx), "[Square] (101) 1/1 - 6")

        sx.update(size=10, x=2, y=2, id=77)
        self.assertEqual(str(sx), "[Square] (77) 2/2 - 10")

    def test_to_dict(self):
        """Test to_dictionary method of a square object"""
        s = Square(10, 2, 2, 107)
        self.assertTrue(s.to_dictionary() == {"id": 107, "size": 10,
                                              "x": 2, "y": 2})

    def test__str__(self):
        """Test the str magic method of a square object"""
        s = Square(8, 0, 0, 11)
        self.assertEqual(str(s), "[Square] (11) 0/0 - 8")


if __name__ == "__main__":
    unittest.main()
