#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """The Square class has two private instance attributes <size> and
    no class attributes.

    """

    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method is automatically called when
        the class is instantiate

        Args:
            size (int): is the size of the square and set to zero by default
            position (tuple): is a tuple of two positive integers

        Raises:
            TypeError: if size is not an integer or at least one member of
                position tuple is negative
            ValueError: if size is less than zero (0)

        """
        self.__size = size
        self.__position = position

    @property
    def size(self) -> int:
        """The size property can be used along with the dot notation to get
        or to set the size of a Square object

        The getter: returns the actual size of the Square object
        Returns:
            a positive integer

        The setter: set/reset the size of the Square object to the given value
        Args:
            value (int): is the size of the square and set to zero by default
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero (0)

        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self) -> tuple:
        """The position property can be used along with the dot notation to get
        or to set he positionof a Square object

        The getter: returns the actual position of a Square object
        Returns:
            a tuple of two positive integers

        The setter: set/reset the position of the Square object to the
        given value
        Args:
            value (tuple): a tuple of two positive integers
        Raises:
            TypeError: if at least one member of the position tuple is negative

        """
        return self.__position

    @position.setter
    def position(self, value) -> None:
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self) -> int:
        """The area method computs and returns the square area of a
        Square object (instance of the Square class)

        Returns:
            the square area of the Square object

        """
        return self.__size ** 2

    def my_print(self):
        """The my_print public instance method, prints to the stdout
        (a square pictogram using '#' characters) if the size is
        greater than 0 (size > 0) otherwise it prints a empty line

        """
        if self.size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for y in range(self.size):
                print("{}{}".format(" " * self.position[0], '#' * self.size))
