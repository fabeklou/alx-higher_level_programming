#!/usr/bin/python3

"""square module: defines a square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square: defines a basic structure for
    Square objects

    """

    def __init__(self, size):
        """constructor or the Square class

        Args:
            size (int): size of the Square object

        Raises:
            TypeError:
                if size is not an integer
            ValueError:
                if size is a null or negative integer

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """the str magic method returns a formatted
        string to be printed

        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """area method calculate the area of
        the rectangle object and return the result

        """
        return self.__size * self.__size
