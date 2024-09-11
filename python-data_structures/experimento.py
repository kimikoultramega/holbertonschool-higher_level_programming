#!/usr/bin/python3
fruits = ['manzana', 'banana', 'cherry']
result = ' '.join(elemento for elemento in fruits if 'a' not in elemento.lower())
print(result)