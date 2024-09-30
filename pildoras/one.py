#!/usr/bin/env python3
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Algún sonido"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau Guau"
    
mi_perro = Perro("Rex")
print(mi_perro.hacer_sonido())
