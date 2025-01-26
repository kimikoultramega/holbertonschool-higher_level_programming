#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_value = my_list[0]  # Inicializa con el primer elemento
        for num in my_list:
            if num > max_value:
                max_value = num  # Actualiza si encuentra un valor mayor
        return max_value  # Retorna el valor máximo encontrado
