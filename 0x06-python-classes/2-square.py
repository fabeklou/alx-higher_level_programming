#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """The Square class has a private instance attribute <size> and
    no class attributes.

    """

    def __init__(self, size=0):
        """The __init__ method is automatically called when
        the class is instantiate

        Args:
            size (int): is the size of the square and set to zero by default

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero (0)

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
