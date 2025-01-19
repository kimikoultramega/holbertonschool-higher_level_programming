#!/usr/bin/python3

def islower(c):
    if len(c) != 1 or not isinstance(c, str):
        raise ValueError("No me descanses")
    if 'a' <= c <= 'z':
        return True
    else:
        return False
