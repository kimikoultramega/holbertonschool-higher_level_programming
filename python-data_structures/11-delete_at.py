#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    length = len(my_list)

    if not my_list:
        return my_list

    if idx < 0 or idx >= length:
        return my_list
    else:
        del my_list[idx]

    return my_list
