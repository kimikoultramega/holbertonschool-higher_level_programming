#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    copy_list = my_list[:]
    length = len(my_list)

    if idx < 0 or idx >= length:
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
