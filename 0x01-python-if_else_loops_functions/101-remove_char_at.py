#!/usr/bin/python3
def remove_char_at(str, n):
    length: int = len(str)
    new_str: str = ""
    if length - 1 < n or n < 0:
        return str
    for index, c in enumerate(str):
        if index != n:
            new_str += c
    return new_str
