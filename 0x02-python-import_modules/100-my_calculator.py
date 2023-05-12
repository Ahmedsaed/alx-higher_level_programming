#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        r = 0

        if argv[2] == "+":
            r = add(a, b)
        elif argv[2] == "-":
            r = sub(a, b)
        elif argv[2] == "*":
            r = mul(a, b)
        elif argv[2] == "/":
            r = div(a, b)

        print("{} {} {} = {}".format(a, argv[2], b, r))
