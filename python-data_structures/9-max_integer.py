#!/usr/bin/python3

def max_integer(my_list=[]):

    max_value = my_list[0]

    if not my_list:
        return None
    else:
        for i in my_list:
            if i > max_value:
                max_value = i
        return max_value
