#!/usr/bin/python3

"""This module defines a function that perform string formatting
over the first and the last name of a user and prints it to the stdout

Example:
>>> say_my_name("Fabrice", "The Great")
My name is Fabrice The Great

"""


def say_my_name(first_name, last_name=""):
    """Perform string formatting over first_name and last_name
    and prints it to the stdout

    Args:
        first_name (str): a required argument of type string representing
            the first name of the user
        last_name (str): a non required argument of type string representing
            the last name of the user `set to an empty string by default`

    Returns:
        str: a new formatted string, user introduction

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string


    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
