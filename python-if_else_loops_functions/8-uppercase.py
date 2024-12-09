#!/usr/bin/python3

def uppercase(str):

    container = ""

    for c in str:

        if 97 <= ord(c) <= 122:
            container += chr(ord(c) -32)
        else:
            container += c
