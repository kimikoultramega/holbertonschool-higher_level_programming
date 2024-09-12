#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
 # Función auxiliar para obtener los dos primeros elementos de una tupla
    def get_elements(tup):
        return tup[0] if len(tup) > 0 else 0, tup[1] if len(tup) > 1 else 0

    # Obtenemos los dos primeros elementos de cada tupla
    a1, a2 = get_elements(tuple_a)
    b1, b2 = get_elements(tuple_b)
    
    # Sumamos los elementos correspondientes
    return (a1 + b1, a2 + b2)