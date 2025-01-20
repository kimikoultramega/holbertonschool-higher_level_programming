#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == '__main__':
    a = 10
    b = 5
    resultadd = add(a, b)
    print("{} + {} = {}".format(a, b, resultadd))
    resultsub = sub(a, b)
    print("{} - {} = {}".format(a, b, resultsub))
    resultmul = mul(a, b)
    print("{} * {} = {}".format(a, b, resultmul))
    resultdiv = div(a, b)
    print("{} / {} = {}".format(a, b, resultdiv))
