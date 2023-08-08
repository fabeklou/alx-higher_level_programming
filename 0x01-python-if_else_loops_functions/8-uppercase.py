#!/usr/bin/python3
def uppercase(str):
    lenght: int = len(str)
    i: int = 0
    if lenght == 0:
        print("")
    for c in str:
        c_int = ord(c)
        i += 1
        if c_int >= 97 and c_int <= 122:
            c = chr(c_int - 32)
        print("{:s}".format(c), end=("" if i < lenght else "\n"))
