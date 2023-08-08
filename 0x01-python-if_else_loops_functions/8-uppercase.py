#!/usr/bin/python3
def uppercase(str):
    lenght: int = len(str)
    i: int = 0
    for c in str:
        c_int = ord(c)
        i += 1
        if c_int >= 65 and c_int <= 90:
            print("{:s}".format(c), end=("" if i < lenght else "\n"))
        else:
            c = chr(c_int - 32)
            print("{:s}".format(c),
                  end=("" if i < lenght else "\n"))
