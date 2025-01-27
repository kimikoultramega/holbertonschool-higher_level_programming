#!/usr/bin/python3

def uniq_add(my_list=[]):

    suma_unicos = 0

    for elemento in my_list:
        if isinstance(elemento, int):
                if my_list.count(elemento) == 1:
                    suma_unicos += elemento
        else:
             pass
    return suma_unicos
