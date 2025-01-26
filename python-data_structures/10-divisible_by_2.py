#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    copy_list = []

    if not my_list:
        return None

    for num in my_list:
        if num % 2 == 0:
            copy_list.append(True)
        else:
            copy_list.append(False)
    return copy_list
