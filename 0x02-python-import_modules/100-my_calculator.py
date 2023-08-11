#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1
    import sys

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    ope = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if ope == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif ope == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif ope == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif ope == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
