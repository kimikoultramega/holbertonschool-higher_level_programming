#!/usr/bin/python3

# Primero genre el rango necesario para las letras y lo amacene en una variable.
letras_en_rango = range(97, 123)

# Luego, utilizando un for, convertí esas letras a ascii con chr.
letras_convertidas = (chr(i) for i in letras_en_rango)

# Utilice join para unirlas, .join() permite unir elementos, le podemos marcar la separación, en este caso no hay.
letras_unidas = "".join(letras_convertidas)

print("{}".format(letras_unidas), end="")
