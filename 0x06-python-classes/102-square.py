#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """The Square class has a private instance attribute <size> and
    no class attributes.

    """

    def __init__(self, size=0):
        """The __init__ method is automatically called when
        the class is instantiate

        """
        self.__size = size

    @property
    def size(self) -> int:
        """The size property can be used along with the dot notation to get
        or to set the size of a Square object

        The getter: returns the actual size of the Square object

        The setter: reset the size of the Square object to the given value
        Args:
            size (int): is the size of the square and set to zero by default
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

    def area(self) -> int:
        """The area method computs and returns the square area of a
        Square object (instance of the Square class)

        Returns:
            the square area of the Square object

        """
        return self.__size ** 2

    def __eq__(self, other):
        """The __eq__ method return <True> if the left hand operand is
        equal to the right hand operand, <False> otherwise

        """
        return self.size == other.size

    def __gt__(self, other):
        """The __gt__ method return <True> if the left hand operand is
        greater than the right hand operand, <False> otherwise

        """
        return self.size > other.size

    def __ge__(self, other):
        """The __ge__ method return <True> if the left hand operand is
        greater than or equal to the <right> hand operand, <False> otherwise

        """
        return self.size >= other.size
