#!/usr/bin/python3

def element_at(my_list, idx):

    length = len(my_list)
    if idx < 0 or idx >= length:
        return None
    else:
        return my_list[idx]

    # for i in my_list:
    #     idx = i
    #     if i < 0 or i >= lenght:
    #         return None
