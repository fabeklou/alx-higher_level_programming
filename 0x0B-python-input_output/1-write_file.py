#!/usr/bin/python3

"""This module defines a function that can writea string
to a text file and return the number of written chracter

"""


def write_file(filename="", text=""):
    """write_file: writes some text to a text file if it exists
    or create the file first if it doesn't and returns the
    number of characters that was written to the file

    Args:
        filename (str):
            a path to the file in which the string should be written to
        text (str):
            the string that should be written to the text file

    Returns:
        (int): total number of written characters

    """
    with open(filename, "w", encoding="utf-8") as fo:
        return fo.write(text)
