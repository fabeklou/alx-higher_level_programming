#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    idx: int = 0
    while idx < x:
        try:
            print("{}".format(my_list[idx]), end="")
            idx += 1
        except IndexError:
            break
    print()
    return idx
