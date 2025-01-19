#!/usr/bin/python3


letras_en_rango = range(97, 123)

# Luego, utilizando un for, convertí esas letras a ascii con chr.
letras_convertidas = (chr(i) for i in letras_en_rango)


letras_unidas = "".join(letras_convertidas)

print("{}".format(letras_unidas), end="")
