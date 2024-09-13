#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []  # Declaramos una nueva lista
    total = 0  # Una variable que almacene mis números
    for num in my_list:  # Bucle para iterar en lista original
        if num not in new_list:  # Si, num no se encuentra en new_list
            new_list.append(num)  # Agregar num a new_list
            total += num  # Sumamos, num al total
    return (total)
