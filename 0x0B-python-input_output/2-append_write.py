#!/usr/bin/python3

"""This module defines a function that can append a string
to the content of a text file and return the number of
written chracters
"""


def append_write(filename="", text=""):
    """append_write: opens a text file, append a string to his content,
    close it back and returns the number of appended chracaters

    Args:
        filename (str):
            a path to the file in which the string should be appended to
        text (str):
            the string that should be appended to the content of text file

    Returns:
        (int): total number of appended characters

    """
    with open(filename, "a", encoding="utf-8") as fo:
        return fo.write(text)
