#!/usr/bin/python3

"""This module defines a BaseGeometry class and a
Rectangle class which is a sub_class of the BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry class defines basic methods and
    attributes to perform geometric tasks

    """
    def area(self):
        """A method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> int:
        """A method that validates a value

        Args:
            name (str):
                is the identifier of the varible (tag)
            value (int):
                is the data of type integer to validate

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less or equal to 0

        """
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


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
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
