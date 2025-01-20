#!/usr/bin/python3
from sys import argv


if __name__ == '__main__':
    s = 0
    for arg in argv[1:]:
        s += int(arg)
    print(s)
