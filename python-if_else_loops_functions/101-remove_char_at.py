#!/usr/bin/python3

def remove_char_at(str, n):

    if n < 0 or n >= len(str): #Verificamos y evitamos errores, por un indice fuera de la cadena
        return str
    
    str1 =str[:n] # Toma desde el inicio de la cadena str hasta que encuentra n
    str2 =str[n+1:] # Toma desde n en adelante, por eso n+1

    resultado = str1 + str2

    return resultado

