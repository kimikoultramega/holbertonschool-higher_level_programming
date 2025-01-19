#!/usr/bin/python3

# # generemos el rango
# rango = range(97, 123)

# resultado = ""

# for i in rango:
#     if chr(i) not in ('q', 'e'):
#         resultado += chr(i)
# print("{}".format(resultado), end="")


# Generamos una lista, en esa lista generamos el rango convertido a ascii
secuencia = [chr(i) for i in range(97, 123)]

# Lista vacia 
unión = []

# Iteramos en secuencia, la lista generada anteriormente.
for i in secuencia:
    if i not in ('q', 'e'):
        unión.append(i) # Generamos una nueva lista, iteramos en secuencia, pero mediante append colocamos las letras menos las excluidas en union.

result = "".join(unión)
print(result)
