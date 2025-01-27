#!/usr/bin/python3

def uniq_add(my_list=[]):

    suma_unicos = 0

    for elemento in my_list:
        if my_list.count(elemento) == 1:
            suma_unicos += elemento
    return suma_unicos
