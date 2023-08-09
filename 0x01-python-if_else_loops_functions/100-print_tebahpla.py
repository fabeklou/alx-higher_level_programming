#!/usr/bin/python3
num: int = 122
while num >= 97:
    ch = chr(num) if num % 2 == 0 else chr(num - 32)
    print("{}".format(ch), end="")
    num -= 1
