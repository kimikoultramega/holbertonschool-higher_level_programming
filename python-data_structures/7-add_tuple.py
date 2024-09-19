#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    #a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    #a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    #b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    #b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    def obtener_elementos(tup):
        return tup[0] if len(tup) > 0 else 0, tup[1] if len(tup) > 0 else 0

    #ahora yo tengo dos elementos que debo de almacenar en 2 variables

    a1, a2 = obtener_elementos(tuple_a)
    b1, b2 = obtener_elementos(tuple_b)

    return(a1 + b1, a2 + b2)