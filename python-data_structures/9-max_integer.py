#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    valor_max = my_list[0] #tomamos como el valor máximo [0]
    for num in my_list:
        if num > valor_max:
            valor_max = num
    return valor_max
