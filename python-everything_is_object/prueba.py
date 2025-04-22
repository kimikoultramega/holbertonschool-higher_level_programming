#!/usr/bin/python3

class Coche:
    def __init__(self, color, marca):

        self.color = color
        self.marca = marca
    
    def __str__(self):
        return f"Coche {self.marca} de color {self.color}"

mi_coche = Coche("Azul", "Ford")
print(mi_coche)