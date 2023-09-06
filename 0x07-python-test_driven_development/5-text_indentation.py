#!/usr/bin/python3

"""Defines a function that prints a text with 2 new lines
after each of these characters `.`, `?` and `:`

"""


def text_indentation(text: str):
    """text_indentation print a text with 2 lines
    after each of these characters `.`, `?` and `:`

    Args:
        text (str): the string to be printed

    Returns: Nothing

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delims: str = ".?:"
    f_str: str = text

    for chr in delims:
        f_str = (chr + "\n\n").join(
            [line.strip(" ") for line in f_str.split(chr)])
    print(f_str, end="")
