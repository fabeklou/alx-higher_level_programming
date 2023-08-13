#!/usr/bin/python3
def no_c(my_string):
    new_str: str = ""
    for ch in my_string:
        if ch not in "cC":
            new_str += ch
    return new_str
