#!/usr/bin/python3

if __name__ == "__main__":
    # Pruebas con diferentes cadenas y valores de n
    print(remove_char_at("Python", 3))  # Debería imprimir: "Pyton" (elimina "h")
    print(remove_char_at("Hello, World!", 7))  # Debería imprimir: "Hello, orld!" (elimina "W")
    print(remove_char_at("Python", -1))  # Debería imprimir: "Python" (índice fuera de rango)
    print(remove_char_at("Python", 10))  # Debería imprimir: "Python" (índice fuera de rango)
    print(remove_char_at("", 0))  # Debería imprimir: "" (cadena vacía)