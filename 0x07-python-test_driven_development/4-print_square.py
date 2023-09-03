#!/usr/bin/python3

"""This module defines a function that can be used to
print a square pictogram using `#` special character

Example:
>>> print_square(3)
###
###
###

"""


def print_square(size: int):
    """print_square prints a square pictogram to the stdout
    using the `#` character

    Args:
        size (int): the size length of the square of type int

    Returns:
        Nothing

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is negative
        TypeError: if size is a negative floating point number
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("{:s}".format('#' * size))


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
