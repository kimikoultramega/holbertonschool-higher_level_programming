#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    # extender tuplas en caso de no tener valores
    extend_tuple = tuple_a + (0, 0)
    extend_tuple2 = tuple_b + (0, 0)
    # tomar solo los primero dos valores
    extend_tuple = extend_tuple[:2]
    extend_tuple2 = extend_tuple2[:2]
    # desempaquetar esos valores
    a1, a2 = extend_tuple
    b1, b2 = extend_tuple2
    # Sumar las tuplas
    sum1 = a1 + b1
    sum2 = a2 + b2

    return (sum1, sum2)
