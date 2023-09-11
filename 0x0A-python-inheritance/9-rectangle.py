#!/usr/bin/python3

"""This module defines a BaseGeometry class and a
Rectangle class which is a sub_class of the BaseGeometry class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This class is a sub_class of the BaseGeometry class
    and can be used to create and work with Rectangle objects

    """
    def __init__(self, width, height):
        """Constructor of the Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

            Raises:
                TypeError: if width/hright is not an integer
                ValueError: if width/height is <= 0

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """the str magic method returns a formatted
        string to be printed

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """area method calculate the area of
        the rectangle object and return the result

        """
        return self.__width * self.__height
