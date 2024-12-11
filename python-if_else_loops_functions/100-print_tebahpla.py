#!/usr/bin/python3

def b():
    for i in range(ord('z'), ord('a') -1, -1):
        char = chr(i)
        print(f"{char.lower() if i % 2 == 0 else char.upper()}", end="")

b()