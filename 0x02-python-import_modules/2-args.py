#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    args = argc - 1

    if args == 0:
        value = "arguments."
    elif args == 1:
        value = "argument:"
    else:
        value = "arguments:"

    print("{:d} {:s}".format(args, value))
    for index, arg in enumerate(argv):
        if index == 0:
            continue
        print("{:d}: {:s}".format(index, arg))
