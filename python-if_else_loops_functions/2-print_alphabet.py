#!/usr/bin/python3

letras_en_rango = range(97, 123)

letras_convertidas = (chr(i) for i in letras_en_rango)

letras_unidas = "".join(letras_convertidas)

print("{}".format(letras_unidas))
