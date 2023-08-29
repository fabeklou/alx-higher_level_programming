#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """The Square class has a private instance attribute and
    no class attributes"""
    def __init__(self, size=0):
        """The __init__ method is automatically called when
        the class is instantiate

        Args:
            size (int): is the size of the square and set to zero by default"""
        self.__size = size
