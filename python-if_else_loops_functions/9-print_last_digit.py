#!/usr/bin/python3

def print_last_digit(number):

    absoluto = abs(number % 10)
    print("{}".format(absoluto), end="")
    return (absoluto)
