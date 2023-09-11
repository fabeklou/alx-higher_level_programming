#!/usr/bin/python3

"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class defines basic methods and
    attributes to perform geometric tasks

    """
    def area(self):
        """A method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> None:
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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
