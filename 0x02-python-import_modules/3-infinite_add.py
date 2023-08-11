#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    result = 0

    for index, value in enumerate(argv):
        if index == 0:
            continue
        result += int(value)
    print("{}".format(result))
