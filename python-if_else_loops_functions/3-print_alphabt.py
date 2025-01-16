#!/usr/bin/python3

# generemos el rango
rango = range(97, 123)

resultado = ""

for i in rango:
    if chr(i) not in ('q', 'e'):
        resultado += chr(i)
print("{}".format(resultado), end="")
