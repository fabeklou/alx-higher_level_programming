#!/usr/bin/python3

"""read_file: defines a function that can be used
to read from a file
"""


def read_file(filename=""):
    """read_file: open a text file, read from it,
    print the content as a string and close it back

    Args:
        filename (str): a path to the file to read from
    
    """
    with open("my_file_0.txt", encoding="utf-8") as fo:
        print("{}".format(fo.read()), end="")
